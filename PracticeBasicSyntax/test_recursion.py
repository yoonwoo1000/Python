import random
def MyFun() :
    # num이 짝수가 나올때 종료
    while True :
        print("MyFun()이 호출되었습니다")
        num = random.randint(1,10)
        print("생성된 숫자 : ", num)
        if num % 2 == 0 :
            return num

def MyFun() :
    print("MyFun()이 호출되었습니다")
    num = random.randint(1,10)
    print("생성된 숫자 : ", num)
    if num % 2 == 0 :
        return num
    else :
        # 함수의 재귀호출
        return MyFun()

if __name__ == "__main__" :
    result = MyFun()
    print("함수의 반환 값 : ",result)