import pymysql, pymysql.cursors

con = pymysql.connect(
    host="localhost",
    user="root",
    password="ezen",
    db="boardEX",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)
cursor = con.cursor()
# 게시글 목록 조회 / 조건 : 페이지당 10개 게시글 조회, 1페이지
perPage = 10
pageNum = 1
# limit 오프셋, 개수
# 1페이지 조회 / # limit 0 ,10     -> (1-1)*10, 10
# 2페이지 조회 / # limit 10 ,10    -> (2-1)*10, 10
# 3페이지 조회 / # limit 20 ,10    -> (3-1)*10, 10
# n페이지 조회 / # limit (n-1)*10 , 10
# 수식과 변수 활용 -> limit ((pageNum - 1) * perPage), perPage
sql = """
select bIDX, bTitle, bType, wDate, hits,
    ( select uName
         from UserList where uIDX = board.uIDX ) as uName,
    ( select count(*)
         from Replys where bIDX = board.bIDX ) as reply_count
from board 
order by bIDX desc 
limit """
offset = (pageNum - 1) * perPage
sql += str(offset) + ", " + str(perPage) + " "
print("SQL :", sql)

pageNum = input("페이지번호를 입력하세요")
pageNum = int(pageNum)
offset = (pageNum - 1) * perPage
sql = f"""
select bIDX, bTitle, bType, wDate, hits,
    ( select uName
         from UserList where uIDX = board.uIDX ) as uName,
    ( select count(*)
         from Replys where bIDX = board.bIDX ) as reply_count
from board 
order by bIDX desc 
limit {offset}, {perPage}"""

print("SQL :", sql)

result = cursor.execute(sql)
if result > 0:
    datas = cursor.fetchall()
con.close()

if datas:
    for data in datas:
        print("=" * 30)
        print("관리 번호 : ", data["bIDX"])
        print("제목 : ", data["bTitle"])
        print("게시판 종류 : ", data["bType"])
        print("작성 일자 : ", data["wDate"])
        print("작성자 이름 : ", data["uName"])
        print("조회수 : ", data["hits"])
        print("댓글 개수 : ", data["reply_count"])
