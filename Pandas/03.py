import pandas as pd

dict_datas = {
    "name": ["u", "ji", "min", "zzang"],
    "class": ["1", "2", "3", "4"],
    "Math": [40, 11, 50, 15],
    "English": [77, 88, 33, 66],
    "Korean": [88, 33, 66, 77],
}

df = pd.DataFrame(dict_datas)

newDF = df.set_index(["name", "class"])
print(newDF)
print(newDF.dtypes)

print(newDF.loc[("u", "1")])
print(newDF.loc[("ji", "2")])

newDF.loc[("hae", "2"), ["Math", "English", "Korean"]] = [77, 15, 4]
newDF.loc[("rin", "3"), ["Math", "English", "Korean"]] = [77, 77, 77]
print(newDF)
