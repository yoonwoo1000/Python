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

