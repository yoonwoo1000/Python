from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = '세션 저장시 보안용으로 사용할 키를 문자열로 작성하세요'

@app.route('/set')
def set() :
    # 세션에 정보 저장하기
    session['uName'] = '홍길동'
    return '세션에 사용자 이름을 저장했습니다'

@app.route('/get')
def get() :
    # 세션에서 정보 가져오기
    uName = session.get('uName')
    if uName :
        return f"사용자 이름 : {uName}"
    else :
        return '세션에 사용자 이름이 없습니다'

@app.route('/del')
def del_session() :
    # None으로 덮어 씌움
    #session['uName'] = None
    # 세션에 있는 데이터중 키로 값을 가져옴 : pop -> 삭제효과
    #session.pop('uName')
    # 세션에 있는 모든 키값쌍을 지움
    session.clear()
    return '세션에서 사용자 이름을 삭제했습니다'

@app.route('/')
def index() :
    return render_template( 'login.html')

if __name__ == '__main__' :
    app.run(debug=True,port=8080)