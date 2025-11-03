from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import requests
import io
import time
agent_head = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' }

'''
유저에게 종목명과 코드를 보여주고
주가 정보를 수집할 종목 코드를 입력 받아
종목명.csv / 종목명.xlsx 파일로
주가 시세 정보를 저장
// 혹은, 종목명, 코드 목록으로 일괄처리
'''
# item_names = ['SK하이닉스','현대차',...]
# item_codes = ['000660','0053800',...]

dict_items ={
    '000660' : 'SK하이닉스',
    '005380' : '현대차',
    '005930' : '삼성전자',
    '373220' : 'LG에너지솔루션',
    '329180' : 'HD현대중공업',
    '012450' : '한화에어로스페이스',
    '035420' : 'NAVER',
    '035720' : '카카오',
    '259960' : '크래프톤',
    '036570' : '엔씨소프트',
    '000000' : '일괄처리'
}

# 마지막 페이지 번호를 찾는 함수
def findMaxNum(code) :
    url = f'https://finance.naver.com/item/sise_day.naver?code={code}'
    html = requests.get(url, headers=agent_head).text
    soup = BeautifulSoup(html,'lxml')
    target = soup.select_one('td.pgRR > a')
    if target :
        try :
            maxNum = target.get('href').split('page=')[1]
            maxNum = int(maxNum) + 1
            return maxNum
        except Exception as e :
            print(e)
            return False

# 종목 코드로 시세 정보 받아오는 함수
def getDatas(code) :
    maxNum = findMaxNum(code)
    if not maxNum :
        print('마지막 페이지 번호를 찾지 못했습니다')
        return False
    all_df = None
    maxNum = 3      # 테스트용으로 2페이지까지만 수집
    for i in tqdm(range(1,maxNum)) :
        time.sleep(1)
        url = f'https://finance.naver.com/item/sise_day.naver?code={code}&page={i}'
        html = requests.get(url, headers=agent_head).text
        tables = pd.read_html(io.StringIO(html))
        if tables :
            df = tables[0]
        else :
            return False
        if df is not None :
            df.dropna(subset='날짜', how='any', axis=0, inplace=True)
        if all_df is None :
            all_df = df
        else :
            all_df = pd.concat([all_df,df])
    all_df.sort_values(by='날짜', ascending=True, inplace=True)
    all_df.drop_duplicates(inplace=True)
    all_df.set_index('날짜',inplace=True)
    return all_df

def saveToFile(df,item_name) :
    # 날짜 다루는 라이브러리에서 오늘 날짜 정보 가져옴
    date = '2025-11-03'
    try :
        df.to_csv(f'{item_name}_{date}.csv',encoding='euc-kr')
    except Exception as e:
        print(e)
    try :
        df.to_excel(f'{item_name}_{date}.xlsx')
    except Exception as e :
        print(e)

print('일별 시세 정보를 수집할 종목의 코드를 입력하세요')
print('''
코드    종목명
000660  SK하이닉스
005380  현대차
005930  삼성전자
373220  LG에너지솔루션
329180  HD현대중공업
012450  한화에어로스페이스
035420  NAVER
035720  카카오
259960  크래프톤
036570  엔씨소프트

일괄 처리 : 000000
''')
input_str = input("코드 : \n")
# 입력이 유효한지 확인
if not input_str or len(input_str) < 6 :
    print('잘못 입력하셨습니다')
    exit()
# 입력 코드가 목록에 있는지 확인
'''switch(input_str) :
        case '000660' :
            item_name = SK하이닉스;
            flage = True
            break;
        case '005380' :
            ....
    '''
if input_str not in dict_items :
    print("목록에 없는 코드를 입력하셨습니다")
    exit()

if input_str == '000000' :
    print('일괄 처리를 시작합니다')
    # 종목 코드 목록 -> dict_items의 키 목록
    for code in dict_items :
        if code != '000000' :
            # 종목명
            item_name = dict_items.get(code)
            df = getDatas(code)
            if df is not None :
                saveToFile(df,item_name)
else :
    item_code = input_str
    item_name = dict_items.get(input_str)
    print(f'{item_name} 종목의 시세 정보를 수집합니다')
    df = getDatas(item_code)
    if df is not None :
        saveToFile(df,item_name)