''' uIDX       | int         | NULL              
    uName      | varchar(30) | NULL              
    uID        | varchar(30) | NULL              
    uPW        | varchar(30) | NULL              
    uEmail     | varchar(64) | NULL              
    joinDate   | datetime    | CURRENT_TIMESTAMP 
    level      | char(1)     | U                 
    isActivate | tinyint(1)  | 1                 '''
import pymysql, pymysql.cursors
con = pymysql.connect( host = 'localhost', user = 'root', password = 'ezen', db = 'boardEX', charset = 'utf8', cursorclass = pymysql.cursors.DictCursor)
cursor = con.cursor()
sql = f'''insert into UserList
    (uName, uID, uPW, uEmail)
    values
    ('홍길동', 'honggildong', 'hongpw', 'hong@ezen.com' ),
    ('홍길동', 'honggildong', 'hongpw', 'hong@ezen.com' ),
    ('홍길동', 'honggildong', 'hongpw', 'hong@ezen.com' ) '''
try :
    result = cursor.execute(sql)
    print("SQL문이 잘 실행되었습니다")
    if result < 3 :
        print(f"삽입된 데이터 개수는 {result}개입니다")
        print("5개가 되지 않아 되돌립니다")
        con.rollback()
    else :
        con.commit()
except Exception as e:
    print(e)
    con.rollback()
con.close()