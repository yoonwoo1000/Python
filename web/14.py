# 네이버 블로그 게시글 검색 목록 페이지
# https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={input_keyword}

# &startDate=2025-10-01
# &endDate=2025-10-02

"https://section.blog.naver.com/Search/Post.naver?keyword=파이썬&startDate=2025-10-01&endDate=2025-10-02"

# 네이버 블로그 게시글 검색 결과가 몇건이 되든
# 572페이지 약 3000개 이후로는 링크를 제공하지 않습니다
# 시작일, 종료일 제약 조건으로 검색 결과를 3000건 이하로 제한하는게 좋습니다

keyword = "jeonju"
start_date = "2025-11-02"
end_date = "2025-11-03"
pageNum = 1
url = f"https://section.blog.naver.com/Search/Post.naver?keyword={keyword}&startDate={start_date}&endDate={end_date}&pageNo={pageNum}"

keyword = input("search keyword : ")
if not keyword:
    print("wrong")
    exit()
else:
    keyword = keyword.strip()
    if keyword == "":
        print("wrong keyword")
        exit()

from datetime import date

start_date = date.today()
end_date = date.today()

url = f"https://section.blog.naver.com/Search/Post.naver?keyword={keyword}&startDate={start_date}&endDate={end_date}"

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

import time

time.sleep(3)

selector = "em"

try:
    search_number = driver.find_element(By.CSS_SELECTOR, selector)
    search_number = search_number.text[:-1]
    if "," in search_number:
        search_number = search_number.replace(",", "")
        search_number = int(search_number)
except Exception as e:
    print("can no find search number")
    exit()
if search_number < 1:
    print("no search")
    exit()
print("search number : ", search_number)

lastPageNum = (search_number - 1) // 7 + 1

for pageNum in lastPageNum:
    print(f"{pageNum}page link")

print(lastPageNum)

driver.close()
