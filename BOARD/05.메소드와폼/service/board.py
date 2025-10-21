import os
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get('host')
user = os.environ.get('user')
passwd = os.environ.get('passwd')
dbname = os.environ.get('dbname')

from service.DBManager import DBManager
dbm = DBManager()

# 페이지당 게시글 수
perPage = 10
# 게시글 목록을 가져오는 함수
def getList(pageNum, type):
    dbm.DBOpen(host,user,passwd,dbname)
    # 총 게시글 수 가져오기
    sql = 'select * from board where bType = %s '
    datas = (type,)
    dbm.OpenSQL(sql, datas)
    total = dbm.getTotal()
    dbm.CloseSQL()
    print("총 게시글 수 : ", total)
    # 총 페이지 개수 
    MAXPAGE = (total-1)//perPage + 1
    if 0 < pageNum <= MAXPAGE :
        # 해당 페이지의 게시글 목록 불러오기
        sql = ''' select *,
    ( select uName from UserList where uIDX = board.uIDX ) as uName,
    ( select count(*) from Replys where bIDX = board.bIDX ) as reply_count
    from board
    where bType = %s
    order by bIDX DESC
    limit %s, %s    '''
        offset = (pageNum-1)*perPage
        datas = (type, offset, perPage)
        dbm.OpenSQL(sql, datas)
        boardList = dbm.getAll()
        dbm.CloseSQL()
        dbm.DBClose()
        return (boardList, MAXPAGE)
    else :
        return (None, 0)

def getMAXPAGE():
    dbm.DBOpen(host,user,passwd,dbname)
    # 총 게시글 수 가져오기
    sql = 'select * from board '
    dbm.OpenSQL(sql)
    total = dbm.getTotal()
    dbm.CloseSQL()
    print("총 게시글 수 : ", total)
    # 총 페이지 개수 
    MAXPAGE = (total-1)//perPage + 1
    dbm.DBClose()
    return MAXPAGE

def view(bIDX) :
    if not dbm.DBOpen(host,user,passwd,dbname) :
        print("DB에 연결하지 못했습니다")
        return
    # 게시글 정보 조회
    sql = ''' select *,
    ( select uName from UserList where uIDX = board.uIDX ) as uName
    from board where bIDX = %s '''
    dbm.OpenSQL(sql, (bIDX,))
    # 게시글 정보를 변수에 담기
    content = dbm.getData(0)
    dbm.CloseSQL()
    # 해당 게시글의 댓글 목록 가져오기
    sql = '''select *, 
    ( select uName from UserList where uIDX = Replys.uIDX) as uName 
    from Replys where bIDX = %s '''
    dbm.OpenSQL(sql, (bIDX,))
    replys = dbm.getAll()
    dbm.CloseSQL()
    dbm.DBClose()
    result = {
        'content' : content,
        'replys' : replys
    }
    return result
