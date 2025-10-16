# 파이썬에서 mysql 연결하기 : 라이브러리 사용
# pip install pymysql
import pymysql
# DBMS 서버의 정보로 DBMS와의 연결을 담당하는 객체 생성 / 연결
con = pymysql.connect(
    host = 'localhost',         # 서버주소
    user = 'root',              # 접속에 사용할 계정
    password = 'ezen',          # 계정의 비번
    db = 'boardEX',             # 사용할 DB이름
    charset = 'utf8'            # SQL문과 결과를 주고 받을때 사용할 인코딩
)
# DB 연결 객체로부터 커서 객체를 생성
cursor = con.cursor()
# 커서 객체는, 결과 테이블을 받아오는 역할 / SQL문을 DBMS에 전달 기능
# sql = 'select * from UserList'
# 커서 객체에게 SQL문을 전달해서 '실행'요청 -> SQL문 실행결과를 result에 담기
# 실행 결과 -> 성공한 레코드 개수 / select, update, insert, delete
# result = cursor.execute(sql)
# 출력
# print(result)
# SQL문 실행 요청의 결과
# 1. 실행 성공
sql = 'select * from UserList'
print("SQL :", sql)
result = cursor.execute(sql)
print(result)       # 회원 데이터가 7건 -> 7 출력
sql = 'select * from UserList where uIDX > 100'
print("SQL :", sql)
result = cursor.execute(sql)
print(result)       # 회원번호가 100을 넘어가는 회원 데이터 없음 -> 0
# 2. 실행 오류
try :
    sql = 'select * from User'      # User 이름의 테이블이 없음
    print("SQL :", sql)
    result = cursor.execute(sql)
    print(result)
except Exception as e :
    print(e)
try :
    sql = 'select * fron User'      # 문법오류
    print("SQL :", sql)
    result = cursor.execute(sql)
    print(result)
except Exception as e :
    print(e)

# 실행한 결과객체 확인하기
sql = 'select * from UserList'
print("SQL :", sql)
result = cursor.execute(sql)
# 조회 결과가 있으면
if result > 0 :
    # 테이블 정보를 출력하고
    print(cursor.description)
    # ((1번컬럼정보),(2번컬럼정보),...(마지막컬럼정보))
    # ('uIDX', 3, None, 11, 11, 0, False)
    # (컬럼이름, 타입, 크기, 내부크기, 정밀도, 스케일, null허용여부)
    # 조회된 데이터 개수만큼 반복문
    for i in range(result) :
        # 커서 객체에게 데이터를 하나 꺼내달라고 요청
        data = cursor.fetchone()
        # 컬럼 개수 : len(cursor.description) / len(data)
        print('-'*30)
        for j in range(len(data)) :
            # 인덱스j인 컬럼의 이름
            # cursor.description[j][0]
            # 인덱스j인 컬럼의 데이터
            # data[j]
            print(cursor.description[j][0], " : ", data[j])
        #print('인덱스',i,' 데이터 : ',data)
# DBMS와의 연결 종료
con.close()