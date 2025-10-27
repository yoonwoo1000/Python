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
    Date(wDate) as wDateS,
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

# 게시글 등록 메소드
def writePost(uIDX,bType,bTitle,bContent) :
    if not uIDX or not bType or not bTitle or not bContent :
        return False
    dbm.DBOpen(host, user, passwd, dbname)
    sql = ''' insert into board ( bType, bTitle, bContent, uIDX ) 
    value ( %s, %s, %s, %s ) '''
    datas = (bType, bTitle, bContent, uIDX)
    result = dbm.RunSQL(sql, datas )
    if result :
        # DBMS와의 연결이 유지된 상태에서 방금 등록한 게시글이
        # 할당받은 기본키값 : bIDX의 값을 받아와야 합니다
        sql = ' select last_insert_id() as idx '
        dbm.OpenSQL(sql)
        # last_insert_id()는 반드시 1개의 데이터를 반환함
        # 0 : 데이터 등록없음 / 숫자 : 할당받은 기본키값
        idx = dbm.getData(0)
        idx = idx.get('idx') 
        dbm.CloseSQL()
        dbm.DBClose()
        return idx
    dbm.DBClose()
    return result