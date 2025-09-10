string = "abcdefghijklmnopqrstuvwxyz"
print(string[0])
print(string[16])
print(string[25])

print(len(string))

# 0 1 2 3 4 5 ... 23 24 25 : 

print(string[-1])
print(string[-26])

print(string[0:4])
print(string[:])

newString = string[:]
print(newString == string)
print(newString is string)

print(string[-3:])

string = "01:12"
hour = int(string[:2])
minuate = int(string[3:])
print(hour)
print(minuate)
totalMin = (hour * 60) + minuate
print(totalMin)


