import requests
url = 'https://blog.naver.com/gilgilit/223804089491'
agent_head = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' }
response = requests.get(url, headers=agent_head)
html = response.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
selector = 'span.se_publishDate'
result = soup.select_one(selector)
if result :
    print(result.text)
else :
    print('객체를 찾지 못했습니다')

#--------------------------------------------------
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(url)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
time.sleep(5)
html = driver.page_source

html = driver.page_source
print(html)

with open("12.txt", "w", encoding="UTF-8") as f :
    f.write(html)

driver.close()
exit()

try :
    obj = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    print(obj.text)
except Exception as e :
    print('시간내에, 객체를 찾지 못하는 오류가 발생했습니다')
driver.close()