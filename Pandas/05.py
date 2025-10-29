import pandas as pd

# CSV 파일 읽어오기
df = pd.read_csv("05.csv", encoding='utf-8')
#df = pd.read_csv("05.csv", encoding='euc-kr')
print(df)
# 첫번째 줄 데이터를 컬럼 이름으로 사용하지 않기
#df = pd.read_csv("05.csv", encoding='utf-8', header=None)
#print(df)
# 컬럼이름 목록, 인덱스 목록을 출력하세요
print(df.columns)
print(df.index)
# 이름 컬럼을 인덱스로 지정
df.set_index('이름',inplace=True)
print(df)
print(df.index)

# 데이터프레임의 내용을 가공했다고 합시다

# 파일로 저장하겠습니다
df.to_csv('05-1.csv', encoding='utf-8')
df.to_csv('05-2.csv', encoding='euc-kr')

# 판다스에서 df을 excel 파일로 저장할때는
# 외부 라이브러리 openpyxl을 사용합니다
# conda install openpyxl
# pip install openpyxl
df.to_excel('05.xlsx')

# 저장이 잘 되어있는지 엑셀에서 데이터프레임 가져오기
result = pd.read_excel('05.xlsx')
print(result)