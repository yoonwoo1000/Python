import numpy as np
import time

size = 100_000_000

py_list = []
print("Processing Python list...")
start = time.time()
py_result = []
for item in py_list:
    py_result.append(item * 13)
end = time.time()
py_time = end - start
print(f"Python list processing time: {py_time:.9f} seconds")


np_array = np.arange(size)
print(np_array.size)
start = time.time()
np_array = np_array * 13
end = time.time()
np_time = end - start
print(f"Numpy array processing time: {np_time:.9f} seconds")

print(py_list[:10])
print(np_array[:10])
print(py_list[-10:])
print(np_array[-10:])

py_array = []
py_array = [1, 2, "1", "A", "ezen", True]

import sys

sum = 0
for item in py_array:
    sum += sys.getsizeof(item)

print(sum)
print(sys.getsizeof(py_array))


sum = sys.getsizeof(py_list)
for item in py_list:
    sum += sys.getsizeof(item)

print(f"py_list size: {sum//1024/1024} MB")
print(f"np_array size: {np_array.nbytes//1024/1024} MB")
