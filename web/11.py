from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'https://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do'
start_time = time.time()
driver.get(url)
# https://www.selenium.dev/documentation/webdriver/waits/
# https://www.selenium.dev/documentation/webdriver/support_features/expected_conditions/
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 명시적 대기
# <div class="board_tit">... / div 객체가 존재할때까지 대기
# 특정 객체가 존재하는것을 기다리는 이유
# -> 찾아서 객체를 이용하기 위해
# 대기를 마치면 특정 객체를 탐색하여 반환합니다
obj = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.board_tit')))
end_time = time.time()
total_time = end_time - start_time  # 소요 시간 계산
print(f"페이지 로딩에 {total_time:.2}초가 소요되었습니다")
# 찾은 객체의 텍스트 정보 출력
print(obj.text)
driver.close()

# https://www.selenium.dev/selenium/docs/api/py/selenium_webdriver_support/selenium.webdriver.support.expected_conditions.html
