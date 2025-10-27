import numpy as np

py_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
np_array = np.array(py_list)
print(np_array)

print(f"array dimension : {np_array.ndim}")
tmp = np.array([1, 2, 3])
print(f"dimension : {tmp.ndim}")

print(f"dimension {np_array.shape}")
print(f"dimension {tmp.shape}")

print(f"dimension : {np_array.size}")
print(f"dimension : {tmp.size}")
