import numpy as np

print(np.__version__)


py_list = [1, "1", "A", "Gang"]
np_arry = np.array(py_list)

print(py_list)
print(np_arry)

print(type(py_list))
print(type(np_arry))

py_list = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
np_arry = np.array(py_list)

print(py_list)
print(np_arry)
print(type(py_list))
print(type(np_arry))

np_arry = np.zeros(10)
print(np_arry)
print(np_arry.dtype)

np_arry = np.zeros(10, dtype=np.int64)
print(np_arry)
print(np_arry.dtype)


np_arry = np.ones(10)
print(np_arry)
print(np_arry.dtype)

np_arry = np.ones(10, dtype=np.int64)
print(np_arry)
print(np_arry.dtype)

np_arry = np.ones((3, 4), dtype=np.int64)
print(np_arry)
print(np_arry.dtype)


np_arry = np.ones((5, 1, 5), dtype=np.int64)
print(np_arry)
print(np_arry.dtype)

np_arry = np.full((5, 1, 5), 7, dtype=np.int64)
print(np_arry)
print(np_arry.dtype)

for i in range(5, 1, 5):
    print(i)

np_arry = np.arange(10)
print(np_arry)

np_arry = np.arange(5, 20, 3)
print(np_arry)

np_arry = np.arange(10, 0, -2)
print(np_arry)
