# 웹크롤링 : 웹페이지의 정보를 가져오는 것

# 웹스크래핑 : 웹페이지에서 원하는 정보를 가져오는것
# 특정 / 편집

# 새로운 콘다 환경 생성
# conda create -n 환경이름 python[=버전] 라이브러리이름 ... -y
# 콘다 환경 목록 확인
# conda env list
# conda create -n web python=3.10 numpy pandas html5lib lxml -y
# 콘다 환경 삭제
# conda env remove --name flask_ex

# 콘솔(터미널)
# curl 주소
# curl https://n.news.naver.com/mnews/article/138/0002208005

# 서버에 '요청'을 보내서 '응답'을 받는 라이브러리
# pip install requests      /    conda install requests

import requests

# 요청 대상 주소
url = 'https://n.news.naver.com/mnews/article/138/0002208005'
# 우리 요청이 브라우저인것처럼 User-Agent 정보를 같이 보냅니다
# 브라우저에서 요청헤드 부분에 "User_Agent"키의 값을 가져옵니다
agent_head = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
# 설정된 URL에 설정된 키:값을 head에 담아 요청함
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

# response.text
# 기사의 제목을 출력하세요
html = response.text
# 기사 제목은 <title>제목</title> 의 구조
# 제목이 시작하는 인덱스 찾기
# 먼저 <title> 문자열이 시작하는 인덱스 찾기
tag = "<title>"
start_index  = html.find(tag)
# '<title>'문자열 글자수 만큼 인덱스를 밀면 제목의 시작 인덱스
start_index += len(tag)
# </title>의 위치 찾기
tag = "</title>"
# 닫는 태그는 시작 태그 뒤에 있는것을 찾아야 함
# 문자열 데이터를 제목 시작 인덱스로 뒷부분만 가져옴
target = html[start_index:]
# 닫는 태그 시작 인덱스 가져오기
end_index = target.find(tag)
result = target[:end_index]
#result = html[start_index:(start_index+end_index)]
print("기사 제목 : ", result)

# 기자 이름을 출력하세요
#<em class="media_end_head_journalist_name">김문기 기자</em>
tag = '<em class="media_end_head_journalist_name">'
start_index  = html.find(tag)
start_index += len(tag)
tag = "</em>"
target = html[start_index:]
end_index = target.find(tag)
result = target[:end_index]
print("기자 이름 : ", result)

# 기사 본문에 있는 기사 제목을 출력하세요

tag = '<h2 id="title_area" class="media_end_head_headline"><span>'
start_index  = html.find(tag)
start_index += len(tag)
tag = "</span></h2>"
target = html[start_index:]
end_index = target.find(tag)
result = target[:end_index]
print("기사 제목 : ", result)

'''
<h2 id="title_area" class="media_end_head_headline"><span>인텔, AI PC 혁신 허브로 韓 서울 낙점…아시아 유일 팝업스토어 개소</span></h2>
'''