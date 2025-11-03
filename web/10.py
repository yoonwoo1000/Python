from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'https://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do'
start_time = time.time() # 작업 시작 시간
driver.get(url)          # 페이지 요청 -> 작업
# 지정한 시간만큼 딜레이 하지 않고,
# '페이지 로딩', 내가 찾는 객체가 검출될때 : 시간적 기준점
# https://www.selenium.dev/documentation/webdriver/waits/
# 10초간 기다리고 그동안 작업이 끝나지 않으면 오류를 반환
# 암묵적 대기
driver.implicitly_wait(10)
end_time = time.time()  # 작업 종료 시간
total_time = end_time - start_time  # 소요 시간 계산
print(f"페이지 로딩에 {total_time:.2}초가 소요되었습니다")
driver.close()