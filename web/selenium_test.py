import selenium
# 셀레니움 설치 확인 : 버전 출력
print(selenium.__version__)
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.naver.com')
import time
time.sleep(10)
driver.close()