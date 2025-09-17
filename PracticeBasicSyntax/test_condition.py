# 사람이 이길 조건
win_conditions = {
    # 사람 : 컴
    "가위" : "보",
    "바위" : "가위",
    "보"   : "바위",
    "1"    : "보",
    "2"    : "가위",
    "3"    : "바위"
}

user = input("유저 : 1.가위, 2.바위, 3.보\n")
user = user.strip()

if user not in win_conditions.keys() :
    print("잘못된 입력입니다")

com = input("컴 : 가위, 바위, 보\n")
com = com.strip()

if com not in win_conditions.values() :
    print("잘못된 입력입니다")

if user == com :
    print("비겼습니다")
else :
    if win_conditions[user] == com :
        print("승리")
    else :
        print("패배")