from service.DBManager import DBManager
import os
from dotenv import load_dotenv
load_dotenv()
host = os.environ.get('host')
user = os.environ.get('user')
passwd = os.environ.get('passwd')
dbname = os.environ.get('dbname')

dbm = DBManager()

# 가입
# 로그인 / 로그아웃
# 조회 
# 회원정보 수정 / 비번 수정
# 탈퇴

# 회원가입 메소드
# -> 이름, 아이디, 비번, 이메일
# -> uIDX, 가입일자, 권한, 활성상태
def join(uName, uID, uPW, uEmail):
    if uName and uID and uPW and uEmail :
        # 모든 매개변수가 입력됨
        dbm.DBOpen(host, user, passwd, dbname)

        # 입력된 id가 이미 사용중인지 확인
        sql = 'select * from UserList where uID = %s '
        dbm.OpenSQL(sql, (uID,))
        result = dbm.getTotal()
        if result > 0 :
            # 이미 사용된 ID
            dbm.CloseSQL()
            dbm.DBClose()
            return False
        dbm.CloseSQL()

        sql = ''' insert into UserList
 ( uName, uID, uPW, uEmail ) value ( %s, %s, %s, %s ) '''
        result = dbm.RunSQL(sql, (uName,uID,uPW,uEmail))
        dbm.DBClose()
        return result
    else :  # 하나라도 누락되었음
        return False

# id,pw를 받아서 DBMS에게 일치 여부를 물어보고
# 일치하면 사용자 정보를 반환
def login(uID, uPW) :
    if not uID or not uPW :
        return None
    dbm.DBOpen(host, user, passwd, dbname)
    # isActivate : 정지상태
    # level : 'A' 관리자 / 'U' 일반유저 / 'D' 탈퇴유저
    sql = ''' select * from UserList 
where 
    uID = %s and uPW = %s
    and isActivate = True
    and level != 'D'
'''
    datas = (uID, uPW)
    dbm.OpenSQL(sql, datas)
    result = dbm.getData(0)
    dbm.CloseSQL()
    dbm.DBClose()
    return result

def getUserInfo(uIDX) : # uIDX를 입력받아 해당하는 회원의 정보 조회
    if not uIDX :
        return False
    dbm.DBOpen(host, user, passwd, dbname)
    sql = ' select * from UserList where uIDX = %s '
    dbm.OpenSQL( sql, (uIDX,) )
    result = dbm.getData(0)
    dbm.CloseSQL()
    dbm.DBClose()
    return result

# 회원 번호와 비번으로 인증하기
def validateUser(uIDX, uPW) :
    if not uIDX or not uPW :
        return False
    dbm.DBOpen(host, user, passwd, dbname)
    sql = ' select * from UserList where uIDX = %s and uPW = %s '
    dbm.OpenSQL(sql, (uIDX, uPW) )
    result = dbm.getData(0)
    dbm.CloseSQL()
    dbm.DBClose()
    return result

# uIDX를 기준으로 회원정보 중 이름, ID, email 업데이트
def updateUserInfo(uIDX,uName,uID,uEmail):
    if not uIDX or not uName or not uID or not uEmail:
        return False
    dbm.DBOpen(host, user, passwd, dbname)
    sql = ''' update UserList set
    uName = %s, uID = %s, uEmail = %s where uIDX = %s '''
    datas = (uName,uID,uEmail,uIDX)
    result = dbm.RunSQL(sql, datas)
    dbm.DBClose()
    return result

# 모든 service의 메소드들은 같은 흐름을 따릅니다
def temlate(uIDX) :
    if not uIDX :
        return False
    dbm.DBOpen(host, user, passwd, dbname)
    sql = ''
    datas = ()
    dbm.OpenSQL(sql, datas )
    result = dbm.getData(0)
    result = dbm.getAll()
    dbm.CloseSQL()
    dbm.DBClose()
    return result