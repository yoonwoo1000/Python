# SRP.py
# 가위 바위 보 게임
import random
wins, losses, draws = 0, 0, 0
# 사용자가 이길 컴퓨터 선택의 조건
win_confitions = {
    #사용자 선택 : 컴퓨터 선택
    "가위" : "보",
    "바위" : "가위",
    "보"   : "바위"
}
choice = { "1" : "가위", "2" : "바위", "3" : "보" }

def userChoice() :
    while True :
        print("-"*30)
        print("1.가위, 2.바위, 3.보 ")
        uInput = input("선택 : [1,2,3,가위,바위,보]\n")
        uInput = uInput.strip()
        if uInput in choice.keys() :   # 1,2,3
            # 1,2,3 -> 가위, 바위, 보
            uInput = choice[uInput]
        if uInput not in win_confitions.keys() :
            # 가위, 바위, 보 이외의 입력
            print("잘못된 입력입니다")
            continue
        return uInput   # 가위, 바위, 보 중 하나의 문자열

def comChoice() :
    return random.choice(["가위","바위","보"])

# 재귀호출을 이용한 함수의 예
# def userChoice() :
#     print("-"*20)
#     print("1.가위, 2.바위, 3.보 ")
#     uInput = input("선택 : [1,2,3,가위,바위,보]\n")
#     uInput = uInput.strip()
#     if uInput in choice.keys() :   # 1,2,3
#         # 1,2,3 -> 가위, 바위, 보
#         uInput = choice[uInput]
#     if uInput not in win_confitions.keys() :
#         # 가위, 바위, 보 이외의 입력
#         print("잘못된 입력입니다")
#         return userChoice()
#     return uInput   # 가위, 바위, 보 중 하나의 문자열

def showMenu() :    # 사용자에게 메뉴를 보여주는 함수
    print("-"*30)
    print("1. 게임 시작")
    print("2. 전적 보기")
    print("3. 게임 종료")

def showStats() :
    total = wins + losses + draws
    if total == 0 :
        print("아직 게임 기록이 없습니다")
        return
    print("-"*30)
    print(f"총 게임수 {total}회")
    print(f"승리 {wins}회")
    print(f"패배 {losses}회")
    print(f"무승부 {draws}회")

def whoIsWinner(userChoice, comChoice) :
    # 전역변수 : 전적 통계용 
    global wins, losses, draws
    if userChoice == comChoice : # 유저와 컴의 선택이 같음
        draws += 1
        return "draw"
    else :
        if win_confitions[userChoice] == comChoice :
            # win_confitions[유저선택값] -> 컴 패배 조건
            # 컴의 선택이 컴 패배 조건과 같음
            wins += 1
            return "win"
        else :  # 남은 경우의 수는 유저 패배
            losses +=1
            return "lose"

def showResult(useChoice, comChoice, result) :
    print("-"*30)
    print(f"유저 : {useChoice} vs 컴 : {comChoice} ")
    if result == "draw" :
        print("🤝🤝무승부입니다")
    elif result == "win" :
        print("🎉🎊유저 승리!!!")
    else :
        print("💻💻컴 승리!!!")

def playGame() :
    print("-"*30)
    print("게임을 시작")
    # 유저 입력
    user = userChoice()
    # 컴 선택
    com = comChoice()
    # 승부 판정
    result = whoIsWinner(user, com)
    # 게임 결과 출력
    showResult(user, com, result)

def main() :
    print("가위바위보 게임")
    while True :
        showMenu()  # 메뉴 출력 함수를 호출
        uInput = input("메뉴를 선택하세요\n")
        if uInput == '3' :
            print("종료를 선택하셨습니다")
            break
        if uInput == '2' :
            showStats() # 게임 전적 출력 함수 호출
            continue
        if uInput == '1' :
            playGame()  # 게임 진행 함수 호출
            continue
        # 1,2,3 이외의 입력
        print("잘못입력하셨습니다")

if __name__ == "__main__" :
    main()