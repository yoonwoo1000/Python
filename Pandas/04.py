import pandas as pd

dict_datas = {
    "name": ["u", "ji", "min", "zzang"],
    "class": ["1", "2", "3", "4"],
    "Math": [40, 11, 50, 15],
    "English": [77, 88, 33, 66],
    "Korean": [88, 33, 66, 77],
}

df = pd.DataFrame(dict_datas)

df.set_index(["name", "class"], inplace=True)
print(df)

result = df + 5

print(result)
print(df)

result = df + 10

result = df["Math"] + 10
print(result)
