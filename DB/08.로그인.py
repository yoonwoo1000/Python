''' uIDX       | int         | NULL              
    uName      | varchar(30) | NULL              
    uID        | varchar(30) | NULL              
    uPW        | varchar(30) | NULL              
    uEmail     | varchar(64) | NULL              
    joinDate   | datetime    | CURRENT_TIMESTAMP 
    level      | char(1)     | U                 
    isActivate | tinyint(1)  | 1                 '''
'''     +-------------+------------+
        | uID         | uPW        |
        +-------------+------------+
        | honggd      | pw$hong123 |
        | junwoo      | pw$jun456  |
        | imkj        | pw$im789   |
        | seongch     | pw$sc012   |
        | leemr       | pw$lm345   |
        | kongj       | pw$kj678   |
        | patj        | pw$pj901   |
        | honggildong | hongpw     |
        +-------------+------------+    '''
import pymysql, pymysql.cursors
con = pymysql.connect( host = 'localhost', user = 'root', password = 'ezen', db = 'boardEX', charset = 'utf8', cursorclass = pymysql.cursors.DictCursor)
cursor = con.cursor()
''' 테스트할 계정과 비번
honggd | pw$hong123
junwoo | pw$jun456
update UserList set uPW = 'ezen' where uIDX in (1,2);
'''
uID = input('아이디 : \n')
if uID.strip() == '' :
    print('아이디가 올바르지 않습니다')
    exit()
uPW = input('비번 : \n')
if uPW.strip() == '' :
    print('비번이 올바르지 않습니다')
    exit()
sql = f"select * from UserList where uID = '{uID}' and uPW = '{uPW}' "
# SQL 삽입 공격 예시
"select * from UserList where uID = 'honggd' and uPW = '1234' or '1' = '1' "
print('sql : ', sql)
result = cursor.execute(sql)
if result < 1 :
    print('아이디 혹은 비번이 올바르지 않습니다')
else :
    uName = cursor.fetchone()['uName']
    print(f"{uName}님 반갑습니다")
con.close()