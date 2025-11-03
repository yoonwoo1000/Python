from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# URL로 웹페이지 열기
url = 'https://www.kobis.or.kr'
driver.get(url)

# 페이지 로딩 기다리기
time.sleep(3)

# '박스오피스' 버튼 객체 찾기
selector = 'li.depth1.nav2.headerWidth'
btn = driver.find_element(By.CSS_SELECTOR, selector)

# 찾은 버튼을 클릭합니다
btn.click()

# 로딩 기다리기
time.sleep(5)

# 드라이버에게 현재 시점에서 브라우저가 해석한 문서 내용을 요청
html = driver.page_source

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# 어제자 박스오피스 테이블 id table_0
table = soup.select_one('#table_0')

import pandas as pd
import io
# 테이블을 문자열 -> 파일객체 -> 데이터프레임
tables = pd.read_html(io.StringIO(str(table)))

if tables :
    df = tables[0]
    # 엑셀 파일로 저장
    df.set_index('순위',inplace=True)
    df.to_excel('09.xlsx')

time.sleep(5)
driver.close()