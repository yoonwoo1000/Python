import pymysql, pymysql.cursors
con = pymysql.connect( host = 'localhost', user = 'root', password = 'ezen', db = 'boardEX', charset = 'utf8', cursorclass = pymysql.cursors.DictCursor)
# boardEX 데이터베이스의 board 테이블 정보 조회하기
# 1번부터 10개 게시글 조회 해보세요
cursor = con.cursor()
# SQL문을 수정하세요
# 문자열에 이어붙이기
sql  = ' select * from board '
sql += ' order by bIDX '
sql += ' limit 0, 10 '
# 여러줄 문자열로 작성하기
sql = ''' select * from board 
order by bIDX 
limit 0, 10 '''
print("SQL :", sql)
result = cursor.execute(sql)
if result > 0 :
    datas = cursor.fetchall()
con.close()

if datas :
    for data in datas : # board 테이블 컬럼에 맞춰서 출력하세요
        print("="*30)
        print("관리번호 : ",data['bIDX'])
        print("제목 : ",data['bTitle'])
        print("내용 : ",data['bContent'])
        print("게시판종류 : ",data['bType'])
        print("작성일자 : ",data['wDate'])
        print("수정일자 : ",data['mDate'])
        print("작성자 : ",data['uIDX'])
        print("조회수 : ",data['hits'])