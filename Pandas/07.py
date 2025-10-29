import pandas as pd

df = pd.read_csv("07.csv", encoding="euc-kr")
print(df)
print(df.dtypes)

print(df.info())
print("-" * 30)

print(df.head())
print("-" * 30)

print(df.tail())
print("-" * 30)

print(df.head(10))
print("-" * 30)
print(df.tail(1))
print("-" * 30)

result = df.isnull()
print(result)
print("-" * 30)

count = df["읍면"].isnull().sum()
print(count)

count = df["남"].isnull().sum()
print(count)
count = df["여"].isnull().sum()
print(count)

copy_df = df.copy()

if copy_df["합계"].isnull().sum() > 0:
    print("have null data")
    copy_df["합계"] = copy_df["합계"].where(copy_df["합계"].notnull(), 0)
else:
    print("no not null data")

print(copy_df)
print("-" * 30)

copy_df = df.copy()

copy_df.dropna(subset=["합계"], how="any", axis=0, inplace=True)
print(copy_df)
print("-" * 30)
copy_df.dropna(subset=["남", "여"], how="any", axis=0, inplace=True)
print(copy_df)
print("-" * 30)
print(copy_df.info())
print("-" * 30)

copy_df = df.copy()

copy_df.drop_duplicates(inplace=True)
print(copy_df)
print("-" * 30)
print(copy_df.info())
print("-" * 30)

copy_df.sort_values(by="읍면", inplace=True)
print(copy_df)
print("-" * 30)


count = copy_df["읍면"].value_counts()

print(count)
print("-" * 30)
print(count["지사면"])
for index_num in range(count.size):
    value = count.iloc[index_num]
    if value > 1:
        index_str = count.index[index_num]
        print(index_str)
