# pip install pymysql
import pymysql
# pip install python-dotenv
from dotenv import load_dotenv
# pip install flask
from flask import Flask, render_template

# Flask 객체 생성
app = Flask(__name__)

import service.board as boardService
# 라우트 지정
@app.route('/')
def index() :
    boardList = boardService.getList(1)
    print(boardList)
    return render_template('index.html',
                title='DB를 이용한 게시판', boardList = boardList )

@app.route('/login')
def login() :
    return render_template('login.html')

if __name__ == '__main__' :
    app.run(debug=True)