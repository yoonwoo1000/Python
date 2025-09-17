user = input("유저 : 가위, 바위, 보\n")
user = user.strip()
if user == "가위" or user == "바위" or user == "보" :
    print("가위, 바위, 보 중 하나를 골랐습니다")
else :
    print("잘못된 입력입니다")

com = input("컴 : 가위, 바위, 보\n")
com = com.strip()
if com == "가위" or com == "바위" or com == "보" :
    print("가위, 바위, 보 중 하나를 골랐습니다")
else :
    print("잘못된 입력입니다")

if user == com :    # 둘의 선택이 같음
    print("비겼습니다")
else :  # 이기거나 져야 함
    if user == "가위" :
        # 컴은 바위, 보 : 가위는 비기는 조건에서 처리되었음
        if com == "바위" :
            print("패배")
        else :  # 컴이 보
            print("승리")
    elif user == "바위" :
        # 컴은 가위, 보
        if com == "가위" :
            print("승리")
        else :
            print("패배")
    else :  # user == "보"
        # 컴은 가위 바위
        if com == "가위" :
            print("패배")
        else :
            print("승리")