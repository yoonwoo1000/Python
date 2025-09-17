# 컴퓨터가 가위,바위,보를 랜덤하게 선택하게 하기
import random
# 1. 1,2,3을 랜덤하게 선택하고 가위,바위,보로 대체
com = random.randint(1,3)   # 1,2,3 정수 선택
SRP = ["가위","바위","보"]  # 리스트 생성
com = SRP[com-1]            # 1->0,2->1,3->2 인덱스 사용
print(com)                  # 1->가위 2->바위 3->보

# 2. ['가위','바위','보'] 리스트에서 랜덤하게 선택
# random.choice(리스트)
# 리스트에서 원소를 랜덤하게 선택
com = random.choice(SRP)
print(com)
