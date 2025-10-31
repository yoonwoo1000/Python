import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

# 일별 시세 1페이지에 방문하여 '마지막페이지 번호'를 추출 하기

# 일별 시세 페이지 주소
url = 'https://finance.naver.com/item/sise_day.naver?code=005930'

# 요청 헤더 설정
agent_head = { "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36' }

# requests를 이용한 요청
response = requests.get(url, headers=agent_head)

# 응답에서 html 문서 추출
html = response.text

# bs4로 파싱
soup = BeautifulSoup(html)

# 페이지 내비게이션 테이블의 '맨뒤' 버튼 찾기
target = soup.select_one('td.pgRR > a')

# 버튼 객체를 찾았으면
if target :
    print('마지막 버튼 객체를 찾았습니다')
    # 버튼의 href 속성에서 마지막 페이지 번호를 찾아옴
    # href 속성값의 마지막 ...&page=숫자 / 'page='으로 자름
    maxNum = target.get('href').split('page=')[1]
    try :
        # 마지막 페이지 번호 + 1 이 필요 -> 정수 변환
        maxNum = int(maxNum)
        print(f'마지막 페이지 번호는 {maxNum}입니다')
        maxNum += 1
    except Exception as e :
        print(e)
        # 페이지 번호를 제대로 변환하지 못하면, 프로그램 중단
        exit()

# 검출된 마지막 페이지 번호를 이용하여 마지막 페이지까지 요청

# 각 페이지 주소 예시
# 'https://finance.naver.com/item/sise_day.naver?code=005930&page=735'

# 결과를 담을 df 선언
all_df = None

# 테스트를 위해 10페이지로 제한
#maxNum = 11 

# pandas의 read_html 요청방식 대응
import io

# 1페이지부터 마지막 페이지까지 반복문 실행
for i in tqdm(range(1,maxNum)) :
    print(f'\n{i}번 페이지에 요청을 보냅니다')

    # f-string formatting을 이용해 url 주소 완성
    url = f'https://finance.naver.com/item/sise_day.naver?code=005930&page={i}'
    print(url)

    # url로 요청을 보내 html을 받아옴
    html = requests.get(url, headers=agent_head).text

    # 응답을 파싱 / pandas를 이용해서 df으로 변환
    # read_html() 함수는 파일 혹은 url을 요구
    # 문자열 객체(html변수 내용)을 유사 파일객체로 변환 처리
    tables = pd.read_html(io.StringIO(html))
    if tables :
        # 각 페이지의 첫번째 테이블이 주가 정보
        df = tables[0]
    else :
        exit()

    # df가 생성되면 na행 제거
    if df is not None :
        print('테이블을 데이터 프레임으로 변환했습니다')
        df.dropna(subset='날짜', how='any', axis=0, inplace=True)
    
    # 데이터 수집 현황 출력
    print(f'{i}번 페이지에서 {df.size}개의 데이터를 추출했습니다')

    # 앞 페이지의 df와 이번 페이지의 df를 병합
    # result = pd.concat([df1,df2])
    # 병합한적이 없으면(처음 작업이면)
    if all_df is None :
        print('첫 데이터프레임입니다')
        all_df = df
    else :
        print('기존 데이터프레임과 병합합니다')
        all_df = pd.concat([all_df,df])

# 이 종목의 모든 주가 정보 수집

# 날짜로 정렬
all_df.sort_values(by='날짜', ascending=True, inplace=True)

# 중복 제거
all_df.drop_duplicates(inplace=True)

# '날짜' 컬럼을 인덱스로 지정
all_df.set_index('날짜',inplace=True)

# 수집 결과 출력
print(f'수집한 데이터 총 개수는 {all_df.size}입니다')

# 파일로 저장하기
try :
    print('csv 파일로 저장을 시도합니다')
    all_df.to_csv('06.csv',encoding='euc-kr')
    print('csv 파일로 저장을 완료했습니다')
except Exception as e:
    print(e)
    print('csv 파일로 저장을 실패했습니다')

# 엑셀 파일로 저장할때에는 openpyxl 라이브러리 필요
# pip install openpyxl
try :
    print('엑셀 파일로 저장을 시도합니다')
    all_df.to_excel('06.xlsx')
    print('엑셀 파일로 저장을 완료했습니다')
except Exception as e :
    print(e)
    print('엑셀 파일로 저장을 실패했습니다')