# .py들과 DBMS를 연결해줄 클래스 작성
import pymysql, pymysql.cursors
class DBManager :
    # 생성자
    def __init__(self):
        self.con    = None
        self.cursor = None
    # DBMS 연결 메소드
    def DBOpen(self, host, id, pw, dbName):
        try:
            self.con = pymysql.connect( host = host, db = dbName,
                user = id, password = pw, charset = 'utf8',
                cursorclass = pymysql.cursors.DictCursor )
            return True
        except Exception as e:
            print(e)
            return False
    # DBMS 연결을 종료하는 메소드
    def DBClose(self) :
        self.con.close()
    
    # sql문 작성 -> 실행 -> 트랜잭션  O / X
    # select -> fetchone() / fetchall()
    # insert, update, delete -> commit() / rollback()
    def RunSQL(self, sql, datas):
        print(f"sql : {sql}")
        if datas :
            try :
                self.cursor = self.con.cursor()
                count = self.cursor.execute(sql, datas)
                if count < 1 :
                    print("데이터를 변경하지 못했습니다")
                    self.con.rollback()
                    self.cursor.close()
                    return False
                else :
                    print("데이터를 변경했습니다")
                    self.con.commit()
                    self.cursor.close()
                    # insert 일때에 할당 받은 pk???
                    return True
            except Exception as e :
                print(e)
                return False
        else :
            print("데이터 변경사항이 누락되었습니다")
            return False
    
    # select 
    # select sql문 실행 메소드  -> OpenSQL
    # 데이터를 가져오는 메소드  -> GetData / GetAll ...
    # 연결을 종료하는 메소드    -> CloseSQl
    def OpenSQL(self, sql, datas=None) :
        print(f"sql : {sql}")
        # 'select * from UserList '
        # 'select * from UserList where level = 'A' and isActivate = fasle'
        # 'select * from UserList where level = 'U' and isActivate = fasle'
        try :
            self.cursor = self.con.cursor()
            # datas가 있느냐?
            if datas :
                self.cursor.execute(sql, datas)
            else :
                self.cursor.execute(sql)
            # 조회된 데이터가 있든 없든, fetchall() 
            self.datas = self.cursor.fetchall() # [] / [원소들]
            return True
        except Exception as e :
            print(e)
            return False
    def CloseSQL(self) :
        self.cursor.close()
    # 조회된 데이터 개수를 반환하는 메소드
    # getTotal() -> 정수
    def getTotal(self) :
        if self.datas :
            return len(self.datas) # -> [] 0 / [원소들] 개수
        else :
            return False
    # getData(index) -> 지정된 인덱스의 행을 반환
    def getData(self, index) :
        if not self.datas : # 조회 결과 객체 자체가 없을때
            return None
        if index < 0 or index >= len(self.datas) :
            # 매개변수로 받은 index가 유효 범위가 아님
            return None
        return self.datas[index]
        if self.datas :
            if 0 <= index < len(self.datas) :
                return self.datas[index]
            else :
                return None
        else :
            return None
    # getAll() -> 데이터 전체를 dict의 list로 반환
    def getAll(self) :
        if self.datas :
            return self.datas
        else :
            return None
    # getValue(index,column) -> 인덱스와 컬럼이름을 지정 -> 값을 반환
    def getValue(self, index, column) :
        if self.con is None :
            print("DB에 연결되어있지 않습니다")
            return None
        if self.cursor is None :
            print("데이터 조회 요청이 없었습니다")
            return None
        if not self.datas :
            print("조회된 데이터가 없습니다")
            return None
        if index < 0 or index >= len(self.datas) :
            print("인덱스 범위가 올바르지 않습니다 ")
            return None
        if column is None or column.strip() == "" :
            print("컬럼 이름이 올바르지 않습니다")
            return None
        #if column in self.datas[index].keys() :
        if column in self.datas[index] :
            # dict 키 목록 비교
            return self.datas[index][column]
            #return self.datas[index].get(column,'기본값')
        else :
            print("입력된 컬럼이름은 테이블에 없습니다")
            return None
