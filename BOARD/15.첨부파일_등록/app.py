from flask import Flask, render_template, request, redirect, session
import service.board as boardService
import service.user as userService

app = Flask(__name__)
app.secret_key = 'ai.service.3rd.503'
# 첨부파일 저장할 폴더 이름
app.config['UPLOAD_FOLDER'] = 'upload'
# 첨부파일 저장 폴더가 있는지 확인하고 없으면 생성
import os
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# 첨부파일 크기 제한
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# 커스텀 필터 정의
@app.template_filter('nl2br')
def nl2br_filter(s) :
    return s.replace('\n','<br>')

@app.route('/')
def index() :
    paraPage = request.args.get('page')
    if paraPage is None or paraPage.strip() == '' :
        page = 1
    else :
        try :
            page = int(paraPage.strip())
        except Exception as e:
            page = 1
    paraType = request.args.get('type')
    if paraType is None or paraType.strip() == '' :
        type = 'fb'
    else :
        type = paraType.strip()
    (boardList, MAXPAGE) = boardService.getList(page, type)
    return render_template( 'index.html',
        type    = type, boardList = boardList, 
        curPage = page, MPNUM     = MAXPAGE     )

@app.route('/view')
def view() :
    bIDX = request.args.get('bIDX')
    if bIDX is None or bIDX.strip() == '' :
        # 잘못된 요청
        return redirect('/')
    try :
        bIDX = int(bIDX.strip())
    except Exception as e :
        # 잘못된 파라메타 값 : 글번호가 아님
        return redirect('/')
    if 'uIDX' in session :
        datas   = boardService.view(bIDX, session.get('uIDX'))
    else :
        datas   = boardService.view(bIDX)
    return  render_template(
                'view.html',
                content = datas.get('content'),
                files   = datas.get('files'  ),
                replys  = datas.get('replys' )
            )

@app.route('/modify', methods=['GET','POST'])
def edit() :
    if 'uIDX' not in session : # 로그인한 유저에게만 허용
        return redirect('/')
    if request.method == 'GET' :
        bIDX = request.args.get('bIDX') # 대상 게시글 번호
        if bIDX is None or bIDX.strip() == '' :
            return redirect('/')
        try :
            bIDX = int(bIDX.strip())
        except Exception as e :
            return redirect('/')
        # 게시글 정보 가져오기
        datas   = boardService.view(bIDX, session.get('uIDX'))
        # datas 가 None -> 게시글 조회가 안됨
        if not datas :
            return redirect('/')
        # 게시글 작성자와, 로그인 유저가 같은가 / 관리자인가
        author = datas.get('content').get('uIDX')
        uIDX = session.get('uIDX')
        content = datas.get('content')
        if author == uIDX : # 작성자가 로그인유저임
            return render_template('edit.html',content=content)
        if session.get('level') == 'A' : # 로그인 유저가 관리자
            return render_template('edit.html',content=content)
        return redirect('/')
        # if (author != uIDX) and (session.get('level') != 'A') :
        #     return redirect('/')
    else:
        # POST로 /modify에 form 데이터를 submit한 상황
        # form 데이터 받기
        # bIDX, bType, bTitle, bContent
        bIDX     = request.form.get('bIDX',     '').strip()
        bType    = request.form.get('bType',    '').strip()
        bTitle   = request.form.get('bTitle',   '').strip()
        bContent = request.form.get('bContent', '').strip()
        # 데이터 유효성 검사
        if not bIDX or not bType or not bTitle or not bContent :
            return redirect('/')
        # bType이 nb이면 -> 로그인 유저가 관리자인지 체크
        if bType == 'nb' :  # 게시글이 공지게시판 글임
            if session.get('level') != 'A' : # 관리자가 아님
                return redirect(f'/modify?bIDX={bIDX}')
        # 자유게시판이거나, 관리자임
        result = boardService.updatePost(bIDX,bType,bTitle,bContent)
        if result : # 수정됨 -> 조회 페이지로
            return redirect(f'/view?bIDX={bIDX}')
        else : # 수정못함 -> 수정페이지로
            return redirect(f'/modify?bIDX={bIDX}')

@app.route('/delete')
def delete() :
    # 로그인 유저 확인
    if 'uIDX' not in session :
        return redirect('/')
    # /delete?bIDX=글번호
    bIDX = request.args.get('bIDX','').strip()
    if not bIDX :
        return redirect('/')
    try :
        bIDX = int(bIDX)
    except Exception as e:
        return redirect('/')
    # bIDX로 게시글 조회
    result = boardService.checkOwner(bIDX)
    bType  = result.get('bType')    # 게시글의 게시판 종류
    author = result.get('uIDX')     # 게시글 작성자 번호
    uIDX   = session.get('uIDX')    # 로그인 유저 번호
    # 관리자 -> 그냥 지움 -> 해당 게시판 목록으로 이동
    if session.get('level') == 'A' :
        if boardService.deletePost(bIDX) :
            return redirect(f'/?type={bType}')
    # 일반유저 -> 작성자일때 지움 -> 해당 게시판 목록으로 이동
    if author == uIDX :
        if boardService.deletePost(bIDX) :
            return redirect(f'/?type={bType}')
    # 작성자와 로그인유저가 다름
    return redirect(f'/view?bIDX={bIDX}')

@app.route('/login', methods=['GET','POST'])
def login() :
    if request.method == 'GET' :    # get으로 요청받으면
        return render_template('login.html') # id, pw를 입력할수 있는 html
    else : # post로 요청받으면
        print("POST 요청을 받았습니다")
        # post 방식의 form 데이터 받기
        uID = request.form.get('uID')
        uPW = request.form.get('uPW')
        print(uID, uPW)
        if uID is None or uID.strip() == '' or uPW is None or uPW.strip() == '' :
            # 제대로 된 form 데이터가 아님
            print('아이디 비번이 넘어오지 않음')
            return render_template(
                'login.html',
                error = '아이디와 비번을 입력하세요')
        # id,pw로 db에 유효한 사용자인지 확인
        userInfo = userService.login(uID, uPW)
        if userInfo :
            # ok : 세션에 정보 저장
            # '/'로 돌려보냄
            session.clear()
            session['uIDX']  = userInfo.get('uIDX')
            session['uName'] = userInfo.get('uName')
            session['level'] = userInfo.get('level')
            return redirect('/')
        else :
            # no : 아이디 비번이 다름 -> 통보
            # '/login'로 돌려보냄
            return render_template(
                'login.html',
                error = '아이디 혹은 비번이 올바르지 않습니다' )

# 구현 안할 거임
# 메소드 지정 post
@app.route('/loginOk')
def loginOk() :
    #login.html의 form에 입력된 값을 전달받아(submit)
    # id,pw로 db에 유효한 사용자인지 확인
    # ok : 세션에 정보 저장
    # no : 아이디 비번이 다름 -> 통보
    # '/'로 돌려보냄
    return

@app.route('/logout')
def logout() :
    session.clear()
    return redirect('/')

@app.route('/join', methods=['GET','POST'])
def join() :
    if request.method == 'POST' :
        # POST 요청 -> form 데이터로 DBMS에 회원 정보 삽입
        uName = request.form.get('uName','').strip()
        uID = request.form.get('uID','').strip()
        uPW = request.form.get('uPW','').strip()
        uEmail = request.form.get('uEmail','').strip()
        print('이름 : ', uName)
        print('아이디 : ', uID)
        print('비번 : ', uPW)
        print('이메일 : ', uEmail)
        if not uName or not uID or not uPW or not uEmail :
            return render_template(
                'join.html',
                error = '모든 항목을 입력해주세요')
        result = userService.join(uName,uID,uPW,uEmail)
        if result :
            # 회원가입 완료 -> 로그인 페이지로 이동
            return redirect('/login')
        else :
            return render_template(
                'join.html',
                error = '회원 가입에 실패했습니다')
    # GET 요청 -> html
    return render_template('join.html')

# 내 회원 정보 조회
@app.route('/mypage')
def mypage() :
    # 로그인 유저인가?
    if 'uIDX' not in session : # 세션에 로그인 정보가 없으면
        return redirect('/')
    # uIDX -> DBMS에 회원 정보 조회
    result = userService.getUserInfo(session.get('uIDX'))
    if result :
        return render_template('mypage.html', user=result)
    else :
        # 세션에 uIDX 정보가 있음
        # DBMS에 uIDX로 조회 요청을 했는데 없음
        session.clear()         # 세션 정보를 초기화 하고
        return redirect('/')    # 메인으로 보냄


# 내 회원 정보 수정
@app.route('/mypage/modify', methods=['GET','POST'])
def mypage_modify() :
    if 'uIDX' not in session :
        return redirect('/')
    uIDX = session.get('uIDX')
    userData = userService.getUserInfo(uIDX)
    if not userData :
        session.clear()
        return redirect('/')
    if request.method == 'GET' :
        if userData :
            return render_template('mypage_form.html', user=userData)
    else :
        uName  = request.form.get('uName','').strip()
        uID    = request.form.get('uID','').strip()
        uEmail = request.form.get('uEmail','').strip()
        uPW    = request.form.get('uPW','').strip()
        if not uName or not uID or not uEmail or not uPW :
            return redirect('/')
        # uIDX와 uPW로 DBMS에 요청한 사용자가 권한이 있는지 확인
        if userService.validateUser(uIDX, uPW) :
            # 사용자가 수정 페이지에서 입력한 pw가 올바름
            # DBMS에 변경 요청
            if userService.updateUserInfo(uIDX,uName,uID,uEmail) :
                # 회원 정보가 수정되었으면 회원 정보 조회 페이지로 이동
                session['uName'] = uName
                return redirect('/mypage')
            else :
                return render_template('mypage_form.html',
                error='회원 정보를 수정하지 못했습니다', user=userData)
        else :
            # 사용자가 수정 페이지에서 입력한 pw가 틀렸음
            return render_template('mypage_form.html',
                error='비번이 올바르지 않습니다', user=userData)

# 내 비번 변경
@app.route('/mypage/passwd', methods=['GET','POST'])
def mypage_passwd() :
    if request.method == 'POST' :
        uPW = request.form.get('uPW')
        newPW = request.form.get('newPW')
        print("기존 비번 : ", uPW, "\n새 비번 : ", newPW)
        # 1. 기본 비번이, 현재 로그인한 유저의 비번이 맞는가?
        uIDX = session.get('uIDX')  # 로그인한 유저의 관리번호
        result = userService.validateUser(uIDX, uPW)
        if not result :
            # 현재 비번이 맞지 않음
            return render_template(
                'mypage_pw.html',
                error='비번이 맞지 않습니다' )
        # 2. 새 비번으로 변경 요청
        result = userService.updatePassWord(uIDX, newPW)
        if not result :
            # 2-2 : 실행이 안되었음 -> 오류발생 안내
            return render_template(
                'mypage_pw.html',
                error='비번호를 변경하지 못했습니다' )
        else :
            # 2-1 : 실행이 잘되었음
            if result == 'duplicate' :
                # 2-1-2 : 데이터 변경 발생없음 -> 기존 비번과 같음
                return render_template(
                'mypage_pw.html',
                error='기존 비번과 동일합니다' )
            else :
                # 2-1-1 : 데이터 변경이 발생되었음 -> 비번 변경
                session.clear()
                return redirect('/login')
    # GET 요청일때에
    return render_template('mypage_pw.html')

@app.route('/write', methods=['GET','POST'])
def write() :
    # 1. 로그인했는지
    if 'uIDX' not in session :
        return redirect('/')
    if request.method == 'POST' :
        bType = request.form.get('bType','').strip()
        if not bType :
            return redirect('/')
        if bType == 'nb' :
            # 글 작성 권한자인지 확인
            if session.get('level') != 'A' :
                # 2. 권한이 있는지 : 공지게시판은 관리자만 작성
                return redirect('/')
        # form 데이터 받고,
        # 제목, 내용, 게시판종류 
        bTitle = request.form.get('bTitle','').strip()
        bContent = request.form.get('bContent','').strip()
        uIDX = session.get('uIDX')
        if not bTitle or not bContent :
            return render_template(
                'write.html',
                error='게시글 내용이 올바르지 않습니다')
        
        # form으로 파일 데이터가 넘어왔는지 확인
        if 'attach' in request.files :
            # 파일객체 리스트를 가져옴
            files = request.files.getlist('attach')

        # DBMS에 게시글 작성 요청
        result = boardService.writePost(uIDX,bType,bTitle,bContent)
        # 요청 결과에 따른 이동
        if result : # 성공 -> 조회페이지
            # 발급받은 게시글 번호로 조회

            # 첨부파일이 있으면, 발급받은 게시글 번호를 참조하여
            # 첨부파일을 DBMS에 등록
            if files :
                # result : 게시글 번호
                # app.config['UPLOAD_FOLDER'] : 저장할 폴더
                # file.filename
                # path = 저장할폴더문자열+파일명
                # 파일명 -> uuid를 사용 생성
                # file.save(path)
                boardService.saveFiles(files, result, app.config['UPLOAD_FOLDER'])

            return redirect(f'/view?bIDX={result}')
        else : # 실패 -> 작성페이지로 보내기
            return render_template(
                'write.html',
                error='게시글 등록에 실패했습니다')
        
    # GET 요청
    # 게시판 종류를 파라메타로 받아오기
    btype = request.args.get('bType','fb').strip()
    if btype == 'nb' :
        if session.get('level') != 'A' :
            # 관리자가 아닌데, 공지게시판 글쓰기 요청
            return redirect(f'/?type={btype}')
    return render_template('write.html',bType=btype)

# view.html에 있는 댓글 작성 form으로부터 post 요청을 받는 함수
@app.route('/reply', methods=['POST'])
def reply():
    if 'uIDX' not in session :      # 로그인 확인
        return redirect('/')
    bIDX  = request.form.get('bIDX')    # 게시글 번호
    rText = request.form.get('rText')   # 댓글 내용
    if not bIDX or not rText :
        return redirect('/')
    uIDX = session.get('uIDX')          # 댓글작성자번호
    # boardService에 댓글 작성 함수 구현하기
    boardService.writeReply(bIDX,rText,uIDX)
    return redirect(f'/view?bIDX={bIDX}')
    # 비동기요청 AJAX -> JS에서 비동기요청 -> 브라우저에서 동적처리
'''    if result :                         # 댓글 작성여부에 따라 
        # 게시글 조회페이지로 이동(페이지 갱신)
    else :
        # 에러 메세지를 표시 -> view() 수정 필요
        return redirect(f'/view?bIDX={bIDX}')   '''

# view.html에 있는 댓글 수정 form으로부터 post 요청
@app.route('/reply/modify', methods=['POST'])
def replyModify():
    # 로그인 확인
    if 'uIDX' not in session :
        return redirect('/')
    # form 데이터 확인
    rIDX   = request.form.get('rIDX')  # 댓글번호
    uIDX_f = request.form.get('uIDX')  # 댓글작성자번호
    rText  = request.form.get('rText') # 변경할 댓글 내용
    if not rIDX or not uIDX_f or not rText :
        return redirect('/')
    # 댓글 삭제 권한 확인
    level  = session.get('level','')       # 로그인 유저의 권한
    uIDX_s = session.get('uIDX','')        # 로그인 유저의 회원번호
    # DBMS에서 댓글번호로 댓글작성자 번호 
    (uIDX_d, bIDX) = boardService.checkReply(rIDX)
    # 관리자면 수정 요청
    if level == 'A' :
        boardService.modifyReply(rIDX, rText)
        return redirect(f'/view?bIDX={bIDX}')
    # form 데이터로 넘어온 작성자번호와, 로그인유저 정보 비교
    # form 데이터는 기본적으로 문자열
    if uIDX_f != str(uIDX_s) :
        return redirect('/')
    # DBMS에서 조회한 댓글 작성자와, 로그인 유저 번호 비교
    if uIDX_d != uIDX_s :
        return redirect('/')
    # 댓글 수정 요청
    boardService.modifyReply(rIDX, rText)
    # 게시글 조회 페이지로 이동
    return redirect(f'/view?bIDX={bIDX}')

# view.html에 있는 댓글 삭제 버튼의 a태그 href로부터 get 요청
@app.route('/reply/delete')
def replyDelete():
    if 'uIDX' not in session :      # 로그인 확인
        return redirect('/')
    rIDX = request.args.get('rIDX')
    # 댓글 삭제 권한 확인 : uIDX(로그인유저) / author(댓글작성자)
    uIDX = session.get('uIDX')
    # 댓글 번호로 댓글 작성자 반환하는 함수 작성 필요
    (author, bIDX) = boardService.checkReply(rIDX)
    # (0,0) -> 댓글번호로 댓글 조회를 못했음 
    if author == 0 or bIDX == 0 :
        return redirect('/')
    if session.get('level') == 'A' :    # 관리자
        # 댓글 삭제 요청
        result = boardService.deleteReply(rIDX)
    if uIDX == author :                 # 작성자 == 로그인유저
        # 댓글 삭제 요청
        result = boardService.deleteReply(rIDX)
    return redirect(f'/view?bIDX={bIDX}')

if __name__ == '__main__' :
    app.run(debug=True)