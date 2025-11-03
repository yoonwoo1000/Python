from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 드라이버 객체 생성
driver = webdriver.Chrome()

# 페이지 요청
url = "https://blog.naver.com/gilgilit/223804089491"
driver.get(url)

# 로딩 기다리기
driver.implicitly_wait(5)

# iframe 객체를 찾아서
iframe = driver.find_element(By.ID, "mainFrame")
# iframe = driver.find_element(By.CSS_SELECTOR,'#mainFrame')

# selenium에게 iframe 객체로 포커스를 이동
driver.switch_to.frame(iframe)

"""
html = driver.page_source
with open("13.txt", "w", encoding="UTF-8") as f :
    f.write(html)
driver.close()
exit()
"""
# 객체 선택자 지정
try:
    selector = "div.se-title-text"
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    selector = "span.se_publishDate"
    wDate = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    selector = "#commentCount"
    replys = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    selector = "div.se-main-container"
    contents = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )
    print("게시글 제목 :", title.text)
    print("게시글 작성일 : ", wDate.text)
    print("댓글 개수 : ", replys.text)
    print("본문 글자 수 : ", len(contents.text))
except Exception as e:
    print("시간내에, 객체를 찾지 못하는 오류가 발생했습니다")

driver.close()
