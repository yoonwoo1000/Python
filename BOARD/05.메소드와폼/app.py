from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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

# 메소드, 1개만 지정 X 
@app.route('/login', methods=['GET','POST'])
def login() :
    if request.method == 'GET' :    # get으로 요청받으면
        return render_template('login.html') # id, pw를 입력할수 있는 html
    else : # post로 요청받으면
        print("POST 요청을 받았습니다")
        # get 방식의 파라메타를 받는 방법
        uID = request.args.get('uID')
        uPW = request.args.get('uPW')
        print(uID, uPW)
        # post 방식의 form 데이터 받기
        uID = request.form.get('uID')
        uPW = request.form.get('uPW')
        print(uID, uPW)
        # 로그인 처리 진행
        #login.html의 form에 입력된 값을 전달받아(submit)
        # id,pw로 db에 유효한 사용자인지 확인
        # ok : 세션에 정보 저장
        # no : 아이디 비번이 다름 -> 통보
        # '/'로 돌려보냄
        return 'post'

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
    return

if __name__ == '__main__' :
    app.run(debug=True)