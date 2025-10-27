import numpy as np

np_arry = np.arange(1, 101)
print(np_arry[3:7])
print(np_arry[:7])
print(np_arry[3:])
print(np_arry[:])

print(np_arry[::2])
print(np_arry[1::2])
print(np_arry[2::3])


np_arry = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
)

print(np_arry)

print(np_arry[0, 0])


print(np_arry[0, :])

print(np_arry[0:2, :], "-" * 10)
print(np_arry[0:2], "-" * 10)
print(np_arry[:, 0:1], "-" * 10)
print(np_arry[:, 0], "-" * 10)

print(np_arry[1:3, 1:3], "-" * 10)
