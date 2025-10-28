import pandas as pd

# pandas의 데이터 자료형 : dataframe
# 2차원 구조를 갖습니다
# 열 : 컬럼 컬럼이름 타입
# 행 : 데이터들 인덱스번호 / 인덱스(이름표)

# 데이터프레임은 1차원 구조인 시리즈의 집합

# Series
# pandas의 1차원 자료 구조
# 인덱스-값 으로 구성
# 인덱스 != 인덱스번호
# 이름표

py_list = ["A", "B", 1, 2, True]
pd_series = pd.Series(py_list)
print(pd_series)

py_lsit = [1, 2, 3, 4, 5]
pd_series = pd.Series(py_list)
print(pd_series)

py_lsit = [1, 2, 3.14, 4, 5]
pd_series = pd.Series(py_list)
print(pd_series)

index_str = ["name", "age", "student", "address"]
data_list = ["Gang", "20", "False", "Seoul"]
pd_series = pd.Series(index=index_str, data=data_list)
print(pd_series)

dict_data = {"name": "Haerin", "age": 20, "student": False, "address": "Seoul"}
pd_series = pd.Series(dict_data)
print(pd_series)

print(pd_series.loc["name"])
print(pd_series.loc["age"])
print(pd_series.loc["student"])
print(pd_series.loc["address"])

print(pd_series.index)
if "gender" in pd_series.index:
    print(pd_series.loc["gender"])
else:
    print("no genders")

print(pd_series["name"])
print(pd_series["age"])
print(pd_series["student"])
print(pd_series["address"])

print(pd_series.iloc[0])
print(pd_series.iloc[1])
print(pd_series.iloc[2])
print(pd_series.iloc[3])

print("Series data : ", pd_series.size)
print("Series data : ", len(pd_series))

for i in range(pd_series.size):
    print(pd_series.iloc[i])


for value in pd_series:
    print(value)

for index in pd_series.index:
    print(index)
    print(pd_series.loc[index])

for index_num in range(pd_series.size):
    print("index number", index_num)
    print("index ", pd_series.index[index_num])
    print("value ", pd_series.iloc[index_num])
    print("value ", pd_series.loc[pd_series.index[index_num]])

pd_series["age"] = 21
print(pd_series)

pd_series["gender"] = "Female"
print(pd_series)

del pd_series["address"]
print(pd_series)

result = pd_series.drop(["student"])
print(pd_series)
print(result)
