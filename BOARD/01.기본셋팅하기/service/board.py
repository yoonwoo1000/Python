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
def getList(pageNum):
    dbm.DBOpen(host,user,passwd,dbname)
    # 총 게시글 수 가져오기
    sql = 'select * from board '
    dbm.OpenSQL(sql)
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
    order by bIDX DESC
    limit %s, %s    '''
        offset = (pageNum-1)*perPage
        datas = (offset, perPage)
        dbm.OpenSQL(sql, datas)
        boardList = dbm.getAll()
        dbm.CloseSQL()
        dbm.DBClose()
        return boardList
    else :
        return None