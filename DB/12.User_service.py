from DBManager import DBManager

dbm = DBManager()

# 회원가입 메소드
# -> 이름, 아이디, 비번, 이메일
# -> uIDX, 가입일자, 권한, 활성상태
def join(uName, uID, uPW, uEmail):
    if uName and uID and uPW and uEmail :
        # 모든 매개변수가 입력됨
        pass
        sql = ''' insert into UserList
 ( uName, uID, uPW, uEmail ) value ( %s, %s, %s, %s ) '''
        dbm.DBOpen('localhost', 'root', 'ezen', 'boardEX')
        result = dbm.RunSQL(sql, (uName,uID,uPW,uEmail))
        dbm.DBClose()
        return result
    else :  # 하나라도 누락되었음
        return False
'''
name, uID, pw, email = '이젠', 'ezen', '1234', 'ezen@ezen.com'
result = join(name,uID, pw, email)
if result :
    print('회원가입이 진행되었습니다')
else :
    print('회원가입이 실패했습니다')
'''