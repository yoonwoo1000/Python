import pandas as pd

# 데이터 가공하기
df = pd.read_csv("06.csv", encoding="euc-kr")
print(df)
print(df.dtypes)
# 세자리수 표기 문자를 지정
df = pd.read_csv("06.csv", encoding="euc-kr", thousands=",")
print(df)
print(df.dtypes)

# '1,234명'으로 작성된 데이터는 세자리수 표기 처리로 대응하지 못함
# df = pd.read_csv('06-1.csv', encoding='euc-kr', thousands=',')
# print(df)
# print(df.dtypes)

# 임실군의 읍면들의 남자 인구 평균
print(df["남"])
print("남성 인구 평균 : ", df["남"].mean())
# 임실군 읍면의 인구수중 최대값, 최소값
print("최대값 : ", df["합계"].max())
print("최소값 : ", df["합계"].min())
# 중간값
print("중간값 : ", df["합계"].median())

# 데이터 프레임에서 특정 값을 갖는 데이터 찾기
# df.loc['인덱스']
# df.loc[조건식을 만족하는 인덱스] -> 데이터
# 인구 합계가 600명이 안되는 모든 데이터
print(df.loc[df["합계"] < 600])
# 인구 합계가 600명이 안되는 지역은?
print(df.loc[df["합계"] < 600]["읍면"])
# 임실군 읍면의 인구수중 최대,최소인 지역은?
print(df.loc[df["합계"] == df["합계"].max()]["읍면"])
print(df.loc[df["합계"] == df["합계"].min()]["읍면"])
print(df.loc[df["합계"] == df["합계"].max()][["읍면", "합계"]])
print(df.loc[df["합계"] == df["합계"].min()][["읍면", "합계"]])

# 값이 최대/최소인 데이터의 인덱스 반환
print("값이 최대인 인덱스 : ", df["합계"].idxmax())
print("값이 최소인 인덱스 : ", df["합계"].idxmin())
# 인덱스로 데이터 조회
print(df.loc[df["합계"].idxmax()])
print(df.loc[df["합계"].idxmin()])

# '1,234명'으로 작성된 데이터는 세자리수 표기 처리로 대응하지 못함
df = pd.read_csv("06-1.csv", encoding="euc-kr", thousands=",")
# 읍면을 인덱스로 지정
df.set_index("읍면", inplace=True)
print(df)
print(df.dtypes)
print("-" * 20)


# 문자열 데이터를 정수로 변경하는 함수
# '명' -> '' / ',' -> ''  '1000원' '원' '$1,000' $/,
def ToInteger(data):
    # 제거해야 할 문자열 처리
    data = data.replace("명", "")
    data = data.replace(",", "")
    # 정수 변환
    try:
        data = int(data)
    except Exception as e:
        print(e)
    # 결과 반환
    return data


# 함수 동작 확인
print("-" * 20)
result = ToInteger("1,234,567명")
print(result, type(result))
print("-" * 20)

# 복사본 생성
copy_df = df.copy()
print(df)
print(copy_df)
print("-" * 20)

# 시리즈에 함수 적용하기
# 시리즈.apply(함수이름)
# 시리즈의 데이터에 함수를 적용해라!!!
# '함수 이름' O : 함수() X
copy_df["합계"] = copy_df["합계"].apply(ToInteger)
copy_df["남"] = copy_df["남"].apply(ToInteger)
copy_df["여"] = copy_df["여"].apply(ToInteger)
print(df)
print(df.dtypes)
print("-" * 20)
print(copy_df)
print(copy_df.dtypes)
print("-" * 20)

# 복사본 생성
copy_df = df.copy()
# 데이터 프레임에 함수 적용하기
# 데이터프레임.applymap(함수이름)   # 제거예정
# 데이터프레임.map(함수이름)        # 새 버전
copy_df = copy_df.applymap(ToInteger)
print(copy_df)
print(copy_df.dtypes)
print("-" * 20)

# 복사본 생성
copy_df = df.copy()
copy_df["남"] = copy_df["남"].map(ToInteger)
print(copy_df)
print(copy_df.dtypes)
print("-" * 20)

# 복사본 생성
copy_df = df.copy()
copy_df[["남", "여"]] = copy_df[["남", "여"]].map(ToInteger)
print(copy_df)
print(copy_df.dtypes)
print("-" * 20)
