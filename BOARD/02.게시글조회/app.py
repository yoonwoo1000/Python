from flask import Flask, render_template, request

app = Flask(__name__)

import service.board as boardService


@app.route("/")  # 메인페이지는 게시판 목록 페이지
def index():
    # 페이지 번호와 함께 요청받기 http://ip:port/?page=페이지번호
    paraPage = request.args.get("page")
    # print('page : ',parameta)
    if paraPage is None:
        # 파라메타로 페이지번호가 넘어오지 않음
        page = 1
    else:
        try:
            page = int(paraPage)
        except Exception as e:
            # 파라메타로 페이지번호가 숫자가 아닌게 넘어옴
            page = 1
    # http://ip:port/?type=nb / http://ip:port/?type=fb
    paraType = request.args.get("type")
    if paraType is None or paraType.strip() == "":
        type = "fb"  # 기본 게시판은 'fb(자유게시판)'
    else:
        type = paraType.strip()
    # type의 값에 따른 유효성 검사
    (boardList, MAXPAGE) = boardService.getList(page, type)
    # print(boardList)
    return render_template(
        "index.html", boardList=boardList, MPNUM=MAXPAGE, curPage=page, type=type
    )


@app.route("/view")  # 게시글 번호와 함께 게시글 조회 페이지 요청
def view():
    # board service를 이용하여, 게시글 내용 조회
    # 게시글 번호는 어떻게 받아옴???
    bIDX = request.args.get("bIDX")
    if bIDX is None or bIDX.strip() == "":
        # 잘못된 요청
        pass
    try:
        bIDX = int(bIDX)
    except Exception as e:
        # 잘못된 파라메타 값 : 글번호가 아님
        pass
    # 파라메타로 넘어온 게시글 번호로 DBMS에서 게시글 내용 조회
    datas = boardService.view(bIDX)
    # print(datas)
    content = datas.get("content")
    replys = datas.get("replys")
    return render_template("view.html", content=content, replys=replys)


if __name__ == "__main__":
    app.run(debug=True)
