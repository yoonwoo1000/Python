import numpy

print(numpy.__version__)

arry = [1, 2, 3, 4, 5]
print(arry)

arry = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(arry)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = []
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print(result)


data1 = numpy.array(list1)
print(data1)
data2 = numpy.array(list2)
print(data2)
datas = numpy.array(arry)
print(datas)

result = data1 + data2
print(result)
