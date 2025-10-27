from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ai.service.3rd.503'

import service.board as boardService

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

    datas   = boardService.view(bIDX)
    return  render_template(
                'view.html',
                content=datas.get('content'),
                replys=datas.get('replys')
            )

import service.user as userService
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

if __name__ == '__main__' :
    app.run(debug=True)