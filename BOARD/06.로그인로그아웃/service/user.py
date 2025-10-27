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
        pass
        sql = ''' insert into UserList
 ( uName, uID, uPW, uEmail ) value ( %s, %s, %s, %s ) '''
        dbm.DBOpen(host, user, passwd, dbname)
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
