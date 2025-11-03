# 셀레니움
# 브라우저 테스트 자동화 툴
# 직접 크롬 브라우저를 실행하고
# 브라우저를 컨트롤
# 동적 사이트에 대응할 수 있음
# 브라우저 이외의 접속을 감지하는 서버 대응
# 사람의 입력을 감지하는 서버에는 랜덤 요소를 추가할 필요가 있음

# 셀레니움 라이브러리 설치
# pip install selenium
import selenium

print(selenium.__version__)
# 크롬 브라우저를 컨트롤하는 드라이버
from selenium import webdriver

# 드라이버 객체 생성 - 크롬 브라우저 지정
driver = webdriver.Chrome()
# 드라이버 객체에게 특정 주소로 연결 요청
driver.get("https://www.naver.com")

import time

time.sleep(3)

# 네이버 검색창 객체 찾기 : id query
# 객체를 찾기위한 수단 : CSS 선택자
# CSS 선택자를 사용할 수 있게 하는 라이브러리
from selenium.webdriver.common.by import By

selector = "#query"
input_obj = driver.find_element(By.CSS_SELECTOR, selector)
# print(input_obj)
# 찾은 객체에 문자열을 보냄
input_obj.send_keys("s")
input_obj.send_keys("e")
input_obj.send_keys("l")
input_obj.send_keys("e")
input_obj.send_keys("nium")
# input_obj.send_keys('셀레니움')
time.sleep(5)

# 찾은 객체에 '엔터키'를 보냄
# https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_common/selenium.webdriver.common.keys.html
from selenium.webdriver.common.keys import Keys

input_obj.send_keys(Keys.ENTER)

time.sleep(5)

# 검색 버튼 객체 찾기
selector = ".btn_search"
btn = driver.find_element(By.CSS_SELECTOR, selector)
# 찾은 버튼을 클릭합니다
btn.click()

# 웹브라우저를 종료 - 드라이버 객체 닫기
time.sleep(5)
driver.close()
