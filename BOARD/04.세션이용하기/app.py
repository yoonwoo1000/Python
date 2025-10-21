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

@app.route('/list')
def list() :
    # '/'가 게시글 목록(list)역할
    # '/'로 되돌려보냄
    return redirect('/info')

if __name__ == '__main__' :
    app.run(debug=True)