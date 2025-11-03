from bs4 import BeautifulSoup
import requests
# 네이버 IT/과학 뉴스 목록 페이지
url = 'https://news.naver.com/section/105'
agent_head = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' }
response = requests.get(url, headers=agent_head)
html = response.text
soup = BeautifulSoup(html, "lxml")
selector = 'div.section_latest a[href^="https://n.news.naver.com/mnews/article"]'
linkList = soup.select(selector)

# 반복문의 진행상황을 시각화하는 라이브러리
from tqdm import tqdm
# pip install tqdm
hrefList = []
if linkList :
    for item in tqdm(linkList) :
        if item.get('href') not in hrefList:
            if 'comment' not in item.get('href'):
                hrefList.append(item.get('href'))
news_list = []
import time
for href in tqdm(hrefList) :
    time.sleep(1) # 각 작업에 1초씩 딜레이
    response = requests.get(href, headers=agent_head)
    soup = BeautifulSoup(response.text, "lxml")
    selector = 'h2.media_end_head_headline'
    title = soup.select_one(selector)
    if not title :
        title = ''
    else :
        title = title.text
    # 본문,기자이름,작성일 등등 포함 
    # 기자이름 : em.media_journalistcard_summary_name_text
    # 기자이름 : em.media_end_head_journalist_name
    # 기자이름 : span.byline_s (이메일포함)
    # 작성일 : span.media_end_head_info_datestamp_time._ARTICLE_DATE_TIME
    # 본문 : article._article_content
    selector = 'span.byline_s'
    journalist_name = soup.select_one(selector)
    # 예외처리 예시
    # CSS 선택자로 객체 탐색 결과가 없으면
    # .text 속성 접근에서 오류 발생
    if not journalist_name :
        journalist_name = ''
    else :
        journalist_name = journalist_name.text
    selector = 'span.media_end_head_info_datestamp_time._ARTICLE_DATE_TIME'
    datestamp = soup.select_one(selector)
    if datestamp :
        datestamp = datestamp.text
    else :
        datestamp = ''
    selector = 'article._article_content'
    article = soup.select_one(selector)
    if article :
        article = article.text.replace('\n\n', '\n')
    else :
        article = ''
    news = {
        'href' : href,
        'title' : title,
        'journalist_name' : journalist_name,
        'datestamp' : datestamp,
        'article' : article
    }
    news_list.append(news)
#print(news_list)
import pandas as pd
df = pd.DataFrame(news_list)
df.to_csv('news.csv',encoding='utf-8')