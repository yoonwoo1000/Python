from DBManager import DBManager
dbm = DBManager()
dbm.DBOpen('localhost', 'root', 'ezen', 'boardEX')
# uIDX가 2인 전우치의 level을 'A' (관리자)로 변경
sql = 'update UserList set level = %s where uIDX = %s '
datas = ('A', 2) # 플레이스홀더 순서대로 작성
dbm.RunSQL(sql, datas)
# 데이터 변경사항 확인하기
sql = 'select * from UserList where uIDX = %s'
datas = (2,)
dbm.OpenSQL(sql,datas)
result = dbm.getAll()
print(result)
dbm.CloseSQL()
dbm.DBClose()