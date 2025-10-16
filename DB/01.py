import pymysql, pymysql.cursors
con = pymysql.connect( host = 'localhost', user = 'root', password = 'ezen',
    db = 'boardEX', charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor # 데이터를 dict로 받아오는 커서
)
cursor = con.cursor()
sql = 'select * from UserList'
print("SQL :", sql)
result = cursor.execute(sql)
if result > 0 :
    datas = cursor.fetchall()   # 데이터 전부를 가져옴
    if datas :
        print(datas)
        for data in datas :
            #print(data) 데이터 -> 딕셔너리 { '컬럼이름' : 컬럼값 , ... }
            print('-'*20)
            # 딕셔너리 키 이름으로 값 호출하기
            print("관리번호 : ",data['uIDX'])
            print("회원성명 : ",data['uName'])
            print("아이디 : ",data['uID'])
            print("비번 : ",data['uPW'])
            print("이메일 : ",data['uEmail'])
            print("가입일자 : ",data['joinDate'])
            print("권한레벨 : ",data['level'])
            print("활성상태 : ",data['isActivate'])
con.close()