#    파일이름         class이름
from DBManager import DBManager
# DBManager 객체 생성
dbm = DBManager()

# DB 연결 요청
dbm.DBOpen('localhost', 'root', 'ezen', 'boardEX')
sql = 'select * from UserList'
# SQL문 실행
dbm.OpenSQL(sql)
# 조회 결과 개수 반환하는 메소드 호출
count = dbm.getTotal()
print("조회된 데이터 개수 :", count)
# 데이터 한개 행 가져오기
data = dbm.getData(0)
print(data)
# 인덱스 3 행에서 컬럼이름 uName으로 값 가져오기
uName = dbm.getValue(3, 'uName')
print(uName)

# 조회 데이터 전부 가져오기
UserList = dbm.getAll()
print(type(UserList))
print(UserList)
for item in UserList :
    print(item)
    print('-'*20)
    print("회원이름 : ", item.get('uName'))
    print("아이디 : ", item.get('uID'))
    print("이메일 : ", item.get('uEmail'))
# SQL문 실행 닫기
dbm.CloseSQL()

# delete문으로 RunSQL() 테스트하기
sql = ' delete from UserList where uIDX = %s '
targetUIDXs = (10,)
result = dbm.RunSQL(sql, targetUIDXs)
if result :
    print("10번 관리번호 회원 정보를 삭제했습니다")
else :
    print("삭제하지 못했습니다")
# 삭제되었는지 조회해보기
sql = 'select * from UserList where uIDX = 10'
dbm.OpenSQL(sql)
print(dbm.getTotal())
dbm.CloseSQL()
# DB 연결 해제
dbm.DBClose()