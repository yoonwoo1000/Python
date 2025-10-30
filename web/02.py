from bs4 import BeautifulSoup
import requests

# 네이버 IT/과학 뉴스 목록 페이지
url = 'https://news.naver.com/section/105'
agent_head = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' }

try :
    response = requests.get(url, headers=agent_head)
    if response.status_code == 200 :
        print("서버가 응답했습니다")
    else :
        print(f"요청 실패 : 상태 코드\n{response.status_code}")
except Exception as e:
    print("요청 중 오류 발생 : \n",e)

# 서버 응답 내용 중 html 문서만 가져오기
html = response.text
# bs4에 파싱
soup = BeautifulSoup(html, "lxml")

# 속성 선택자
# [속성이름]
# [href]
# 속성이름과 속성값
# [속성이름=값]
# [align='center']

# 값이 특정 문자열로 시작하는 객체
# [속성이름^=문자열]

# 값이 특정 문자열을 포함하는 객체
# [속성이름*=문자열]

# 값이 특정 문자열로 종료하는 객체
# [속성이름$=문자열]

# 특정 단어로 검색 : 빈칸으로 구분되는 문자열
# [class~="cancel"]
#<button class="btn cancel big">버튼입니다</button>

# 특정 단어로 검색 (단어 뒤에 -로 구분되며 단어로 시작)
# [class|="btn"]
#<button class="btn-cancel-big">버튼입니다</button>

# <button class="btn_cancel_big">버튼입니다</button>
# [class="btn_cancel_big"]

# 기사 목록 페이지에서 링크들 수집
selector = 'div.section_article._TEMPLATE a[href^="https://n.news.naver.com/mnews/article"]'
linkList = soup.select(selector)

if linkList :
    for item in linkList :
        print('-'*20)
        print(item)
print(f'''--------------------
찾은 객체 개수 : {len(linkList)}
--------------------''')

# 일반 뉴스 목록 객체 선택자
selector = 'div.section_latest'
# 하나만 찾을때에는 soup결과 객체
result = soup.select_one(selector)
# 객체의 하위 탐색
selector = 'a[href^="https://n.news.naver.com/mnews/article"]'
linkList = result.select(selector)
hrefList = []
if linkList :
    for item in linkList :
        # 찾은 뉴스 링크의 href 속성값을 리스트에 추가
        # href 속성값 : 뉴스 주소
        hrefList.append(item.get('href'))
print(f'찾은 객체 개수 : {len(linkList)}')
# 수집된 뉴스 기사들의 주소 목록
print(hrefList)