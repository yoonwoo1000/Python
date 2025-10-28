import pandas as pd


datas = [[15, "Male", "Middle"], [16, "Male", "High"], [17, "Female", "High"]]

index_str = ["Gang", "Hae", "Rin"]
columns = ["age", "gender", "School"]

df = pd.DataFrame(data=datas, index=index_str, columns=columns)
print(df)

dict_datas = {
    "name": ["u", "ji", "min"],
    "age": [25, 12, 21],
    "gender": ["Female", "Female", "male"],
    "school": ["High", "middle", "low"],
}
df = pd.DataFrame(dict_datas)
print(df)

newDf = df.set_index("name")
print(newDf)
print(df)

df.set_index("name", inplace=True)
print(df)

series = df["age"]
print(series)
print("-" * 20)
series = df["gender"]
print(series)
print("-" * 20)
series = df["school"]
print(series)
print("-" * 20)

newDF = df[["age", "school"]]
print(newDF)

result = df.loc["u"]
print(result)

result = df.iloc[1]
print(result)

print(df.columns)
print("-" * 20)

df.columns = ["age", "gen", "sc"]
print(df)
print(df.index)

df.index = ["gang", "hae", "rin"]
print(df)
print(df.index)


print(df["gen"]["gang"])

print(df.loc["gang"])
print(df.loc["gang"]["gen"])

result = df.drop("age", axis=1, inplace=True)
print(result)
result = df.drop("gang", axis=0, inplace=True)
print(result)

print(df)
