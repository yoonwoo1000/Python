import requests

url = "https://n.news.naver.com/mnews/article/138/0002208005"
# 우리 요청이 브라우저인것처럼 User-Agent 정보를 같이 보냅니다
# 브라우저에서 요청헤드 부분에 "User_Agent"키의 값을 가져옵니다
agent_head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}
# 설정된 URL에 설정된 키:값을 head에 담아 요청함
try:
    response = requests.get(url, headers=agent_head)
    # 요청에 대한 응답 코드 확인
    if response.status_code == 200:
        print("서버가 응답했습니다")
        # 응답 헤더 정보 출력
        print(response.headers)
        # 응답 헤더중 '키'로 값 가져오기
        print(response.headers.get("content-type"))
        # 응답 본문 출력
        # print(response.text)
        print(response.text[:400])
    else:
        print(f"요청 실패 : 상태 코드\n{response.status_code}")
except Exception as e:
    print("요청 중 오류 발생 : \n", e)

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")

title = soup.find("title")

if title:
    print(title)
    print(title.text)
else:
    print("can not find text")
