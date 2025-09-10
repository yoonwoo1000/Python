age = 20
strData = "age" + str(age) + "!"
print(strData)

strData = "age is %d" % age
print(strData)

pi = 3.14

strData = "pi's value is %d" % pi 
print(strData)
strData = "pi's value is %.2f" % pi
print(strData)

pi = 123456789.123456789
strData = "pi's value is %10.2f" % pi
print(strData)
year = 2025
month = 9
day = 10
strData = "year:%02d month:%02d day:%02d" % (year, month, day)
print(strData)

year = "2025"
month = "9"
day = "10"
strData = "year:%s month:%s day:%s" % (year, month, day)
print(strData)