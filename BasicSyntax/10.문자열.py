# 문자열 : 문자들이 순서대로 연결된 원소가 여러개인 객체
#         01234567890123456789012345 : 26개 문자
string = "abcdefghijklmnopqrstuvwxyz"
print(string[0])    # a
print(string[16])   # q
# 원소의 개수 len(객체이름)
print(len(string))
# 0 1 2 3 4 5 ... 23 24 25 : 인덱스 번호
#                 -3 -2 -1 : 음수 인덱스
print(string[-1])
# 인덱스 범위 사용하기 : 슬라이싱
# [시작인덱스:잘라낼시작인덱스]
print(string[0:4])   # abcd
print(string[12:15]) # mno
print(string[18:26])
print(string[18:])   # 끝까지
print(string[:4])    # 처음부터
print(string[:])     # 처음부터 끝까지
print(string)
# 슬라이싱 : 원본은 유지 : 새로운 객체 생성
# [:] 전체 : 객체를 생성하지 않음
newString = string[:]
print(newString == string)
print(newString is string)
# string을 슬라이싱해서 xyz를(끝 3글자만) 출력하세요
print(string[-3:])
# 2025-09-10 17:23:12
#           0123456789012345678
timeData = "2025-09-10 17:23:12"
date = timeData[:10]
time = timeData[-8:]
print(f"오늘 날짜는 {date}입니다")
print(f"현재 시간은 {time}입니다")

string = "     hello, ezen!!!     "
# 앞 뒤, 공백 제거하기
print(string.strip())   # 원본은 유지됨
print(string)