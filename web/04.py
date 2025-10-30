# https://finance.naver.com/marketindex/

# 미국 USD
# 일본 JPY
# 선택사항으로 여러분들이 찍고 싶은 환율

# 콘솔에 출력해보세요


from bs4 import BeautifulSoup
import requests
url = 'https://finance.naver.com/marketindex/'
agent_head = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' }
response = requests.get(url, headers=agent_head)
html = response.text
soup = BeautifulSoup(html, "lxml")
# 환율 문자열
selector = 'a.head > h3.h_lst > span.blind'
selector = 'div.data h3.h_lst'
result = soup.select_one(selector)
if result :
    print(result.text)
# 달러 환율
selector = 'a.head > div.head_info > span.value'
result = soup.select_one(selector)
if result :
    print(result.text)

'''
<div class='market_data'>
    <div class='market1'>
        div.data > ul > li
            a.head > h3.h_lst > span.blind -> 아이템 이름
            a.head > div.head_info > span.value -> 가격
    </div>
    <div class='market2'></div>
    <div class='market3'></div>
</div>
┏━━━━━━━━━━━━━━━━━━━┓┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ 환전고시환율      ┃┃ 국제시장환율      ┃ 유가금시세        ┃
┣━━━━━━━━━━━━━━━━━━━┫┣━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ USD 금액 단위 증감┃┃ 달러/엔           ┃ WTI               ┃
┣━━━━━━━━━━━━━━━━━━━┫┣━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ JPY 금액 단위 증감┃┃ 유로/달러         ┃ 휘발유            ┃
┣━━━━━━━━━━━━━━━━━━━┫┣━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ EUR 금액 단위 증감┃┃ 파운드/달러       ┃ 국제금            ┃
┣━━━━━━━━━━━━━━━━━━━┫┣━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━┫
┃ CNY 금액 단위 증감┃┃ 달러인덱스        ┃ 국내금            ┃
┗━━━━━━━━━━━━━━━━━━━┛┗━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━┛
'''
# 상위 카테고리를 찾음 : market1, market2, market3 
markets = soup.select('div.market_data > div[class^="market"]')
result_list = []
if markets :
    for market in markets : # 각각의 마켓에 대해서
        market_name = market.select_one("div.title").text
        print(f"{market_name}에서 정보를 찾습니다")
        items = market.select('div.data > ul > li')
        for item in items : # 각 마켓을 4개 아이템들에 대해
            item_name = item.select_one('a.head > h3.h_lst').text
            selector = 'a.head > div.head_info > span.value'
            item_value = item.select_one(selector).text
            item = { 'market' : market_name, 'item_name' : item_name, 'item_value' : item_value }
            result_list.append(item)
print(result_list)