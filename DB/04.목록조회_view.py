import pymysql, pymysql.cursors
con = pymysql.connect( host = 'localhost', user = 'root', password = 'ezen', db = 'boardEX', charset = 'utf8', cursorclass = pymysql.cursors.DictCursor)
cursor = con.cursor()
# 게시글 목록 조회용 SQL문 : view table 이용 boardlist
sql = ' select * from boardlist order by bIDX limit 0, 10 '
print("SQL :", sql)
result = cursor.execute(sql)
if result > 0 :
    datas = cursor.fetchall()
con.close()

if datas :
    for data in datas :
        print("="*30)
        print("관리 번호 : ",data['bIDX'])
        print("제목 : ",data['bTitle'])
        print("작성 일자 : ",data['wDate'])
        print("작성자 이름 : ",data['uName'])
        print("조회수 : ",data['hits'])
        print("댓글 개수 : ",data['reply_count'])