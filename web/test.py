#        0 1 2 3 4 5 6 7 8 910111213
text = '가나다라마바사아자차카타파하'
index = text.find("다라")
print(index)
# 본문
text = '...<title>인텔, AI PC...</title>...'
# 찾는 태그의 시작 인덱스
start_index = text.find('<title>')
# 필요한건 title태그가 감싸고 있는 문자열
# <title> 글자수 만큼 인덱스 번호에 더함
start_index += len('<title>')
# 닫는 태그의 시작 인덱스 찾기
end_index = text.find('</title>')
# 본문에서 시작인덱스와 잘라낼 인덱스로 슬라이싱
result = text[start_index:end_index]
print(result)