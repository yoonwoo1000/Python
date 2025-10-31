import requests
import pandas as pd
# 삼성전자 일별 시세 조회 페이지
url = 'https://finance.naver.com/item/sise_day.naver?code=005930'
agent_head = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' }
response = requests.get(url, headers=agent_head)
html = response.text
print(html)
# 문서에 테이블이 두개 -> 주가테이블/페이징테이블
# 첫번째 테이블만 df에 넣기
df = pd.read_html(html)[0]
df.dropna(subset='날짜', how='any', axis=0, inplace=True)
print(df.info())
print(df)
df.to_csv('05_삼성전자주가.csv', encoding='euc-kr')

'''
<table cellspacing="0" class="type2">
    <tbody>
        # 제목 줄
        <tr>
            <th>날짜</th><th>종가</th><th>전일비</th><th>시가</th><th>고가</th><th>저가</th><th>거래량</th>
        </tr>
        # 꾸밈 줄
        <tr>
            <td colspan="7" height="8"></td>
        </tr>
        # 데이터 줄
        <tr onmouseover="mouseOver(this)" onmouseout="mouseOut(this)" style="background-color: rgb(255, 255, 255);">
            <td align="center"><span class="tah p10 gray03">2025.01.15</span></td>
            <td class="num"><span class="tah p11">53,700</span></td>
            <td class="num">
                <em class="bu_p bu_pdn"><span class="blind">하락</span></em>
                <span class="tah p11 nv01">200</span>
            </td>
            <td class="num"><span class="tah p11">54,100</span></td>
            <td class="num"><span class="tah p11">54,700</span></td>
            <td class="num"><span class="tah p11">53,500</span></td>
            <td class="num"><span class="tah p11">18,625,025</span></td>
        </tr>
        ...
        # 꾸밈 줄
        <tr>
            <td colspan="7" height="8"></td>
        </tr>
        <tr>
            <td colspan="7" height="1" bgcolor="#e1e1e1"></td>
        </tr>
        <tr>
            <td colspan="7" height="8"></td>
        </tr>
        ...
        데이터줄들
        ...
        꾸밈줄
    </table>
    # 페이징 내비게이션 테이블
    <table>
    ...
'''