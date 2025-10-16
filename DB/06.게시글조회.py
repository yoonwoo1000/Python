import pymysql, pymysql.cursors
con = pymysql.connect( host = 'localhost', user = 'root', password = 'ezen', db = 'boardEX', charset = 'utf8', cursorclass = pymysql.cursors.DictCursor)
cursor = con.cursor()
# bIDX로 게시글 조회하기
bIDX = input('조회할 게시글의 번호를 입력하세요')
sql = f'''select *, 
    ( select uName from UserList where uIDX = board.uIDX) as uName
from board where bIDX = {bIDX} '''
result = cursor.execute(sql)
if result < 1 :
    print(f'{bIDX}번 게시글을 조회하지 못했습니다')
    con.close()
    exit()
data = cursor.fetchone()
# 게시글 데이터 조회 성공 -> 조회수 증가
try :
    sql = f'update board set hits = hits + 1 where bIDX = {bIDX}'
    result = cursor.execute(sql)
    con.commit()    # 변경 적용
except Exception as e:
    # SQL문 실행 실패 
    con.rollback()  # 롤백
if result < 1 :
    # SQL문이 실행되었으나, 조회수 업데이트 실패
    print("조회수 수정을 실패했습니다")

# 선택된 게시글에 달린 댓글 목록 조회하기
sql = f'''select *, 
( select uName from UserList where uIDX = Replys.uIDX) as uName 
from Replys where bIDX = {bIDX}'''
result = cursor.execute(sql)
replys = None
if result < 1 :
    print(f"{bIDX}번 게시글에는 댓글이 없습니다")
else :
    replys = cursor.fetchall()

con.close()
# 비교용으로 수정일자 업데이트
# update board set mDate = now() where bIDX = 10;
# 있는 게시글 번호를 입력하세요

# 수정일자가 없을 경우 ---------
if data['mDate'] is None :
    mDate = ''
else :
    mDate = f"\n수정일자 : {data['mDate']}"
# bType fb / nb : 자유게시판 / 공지게시판 -----------
if data['bType'] == 'fb' :
    bType = '/ 게시판 종류 : 자유게시판'
elif data['bType'] == 'nb' :
    bType = '/ 게시판 종류 : 공지게시판'
else :
    bType = ''

# 게시글 출력할 템플릿
contents = f'''
--------------------------------------------------
게시글 번호 : {data['bIDX']} {bType}
--------------------------------------------------
제목 : {data['bTitle']}
작성자 : {data['uName']}
--------------------------------------------------
{data['bContent']}
--------------------------------------------------
작성일자 : {data['wDate']} {mDate}
조회수 : {data['hits']+1}
--------------------------------------------------
'''
print(contents)
if replys :
    print("댓글들----------")
    for reply in replys :
        print(f'''------------------------------------
작성자 이름 : {reply['uName']}
내용 : {reply['rText']}
작성일자 : {reply['wDate']} ''')
    print("------------------------------------")