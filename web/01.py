# https://beautiful-soup-4.readthedocs.io/en/latest/
# beautiful soup
# Beautiful Soup 은 HTML 및 XML 파일에서 데이터를 추출하는 Python 라이브러리입니다. 선호하는 파서와 함께 작동하여 파싱 트리를 탐색, 검색 및 수정하는 편리한 방법을 제공합니다. 

# pip install beautifulsoup4
# conda install bs4

# beautiful soup은 서버에 요청기능이 없습니다
# html 문자열을 받아서 -> 파싱 -> dom(과비슷한)트리 생성 -> 태그이름, 클래스이름, CSS 선택자 등을 통해 객체 탐색
# 파싱에 '파서'를 사용
'''
    html.parser
        기본 파서
        파이선 3.2.2 이전 버전에서는 사용할 수 없음
    html5lib
        html에 대해서는 가장 강력한 파서
        웹 브라우저와 동일한 방법으로 문서 파싱
        매우 느립니다
    lxml
        가장 빠른 파서
        외부 c에 의존
    xml
        lxml-xml / xml
        xml 을 위한 파서
'''

import requests
url = 'https://n.news.naver.com/mnews/article/138/0002208005'
agent_head = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' }
try :
    response = requests.get(url, headers=agent_head)
    # 요청에 대한 응답 코드 확인
    if response.status_code == 200 :
        print("서버가 응답했습니다")
        # 응답 헤더 정보 출력
        print(response.headers)
        # 응답 헤더중 '키'로 값 가져오기
        print(response.headers.get('content-type'))
        # 응답 본문 출력
        #print(response.text)
        print(response.text[:400])
    else :
        print(f"요청 실패 : 상태 코드\n{response.status_code}")
except Exception as e:
    print("요청 중 오류 발생 : \n",e)

html = response.text

from bs4 import BeautifulSoup
# bs4를 이용해서 html문서를 파싱 : 파서 lxml 선택
soup = BeautifulSoup(html, "html.parser")
soup = BeautifulSoup(html, "html5lib")
soup = BeautifulSoup(html, "lxml")

# 태그를 이용해서 객체 찾기
# <title>
title = soup.find('title')
if title :
    print(title)
    print(title.text)
else :
    print("객체를 찾지 못했습니다")

# find() 는 찾는 객체가 나오면 멈춥니다 -> 1개만 찾음

# 모든 객체 찾기 find_all()
items = soup.find_all('h2')
if items :
    for item in items :
        print(item)
        print(item.text)
print("찾은 h2 객체의 개수 : ", len(items))

'''
서버가 응답한 html에는 h2 태그가 5개
브라우저에서 확인 가능한 h2 태그는 6개
    -> 1개의 h2 태그는 JS를 통해서 동적으로 생성된 것입니다
requests로 요청한 웹페이지의 내용은 동적인 변화는 대응하지 못합니다
requests는 JS를 실행하지 못합니다
'''
# id로 객체 찾기
item = soup.find(id='img1')
print(item)

# class로 객체 찾기
article = soup.find('div', class_='newsct_article')
print(article)
print(article.text[:100])

# 찾은 객체의 하위 객체들 중에서 탐색하기
items = article.find_all('span')
if items :
    print('찾은 객체 개수 : ', len(items))
    for obj in items :
        print('-'*20)
        print(obj) 

items = article.find_all('div')
if items :
    print('찾은 객체 개수 : ', len(items))
    for obj in items :
        print('-'*20)
        print(obj) 

# css 선택자로 객체 찾기
# soup.select(css선택자)
# soup.select_one(css선택자)
result = soup.select('div.newsct_article span')
if result :
    print("찾은 객체 개수 : ", len(result))
    for item in result :
        print(item, '\n' ,'-'*20)

#dic_area > strong:nth-child(50)
result = soup.select('#dic_area > strong')
if result :
    print("찾은 객체 개수 : ", len(result))
    for item in result :
        print(item, '\n' ,'-'*20)

#<span class="media_end_head_info_datestamp_time _ARTICLE_DATE_TIME" data-date-time="2025-10-29 09:01:06" data-date-time-age-in-minutes="1510">2025.10.29. 오전 9:01</span>
result = soup.select('span._ARTICLE_DATE_TIME')
if result :
    print("찾은 객체 개수 : ", len(result))
    for item in result :
        print("기사 작성 시간 : ",item.text)