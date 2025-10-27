import numpy as np

array_a = [1, 2, 3, 4]
array_b = [5, 6, 7, 8]
print(array_a + array_b)
result = []

if len(array_b) != len(array_a):
    print("can not op")
else:
    for index in range(len(array_a)):
        result.append(array_a[index] + array_b[index])
print(result)


np_a = np.array(array_a)
np_b = np.array(array_b)

print("sum", "-" * 20)
np_result = np_a + np_b
print(np_result)
print("-")
np_result = np_a - np_b
print(np_result)


np_A = np.array([[1, 2, 3], [4, 5, 6]])
np_B = np.array([[1, 2], [3, 4], [5, 6]])
np_result = np.dot(np_A, np_B)
print(np_result)

np_result = np.dot(np_B, np_A)
print(np_result)
