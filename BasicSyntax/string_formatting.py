PI = 3.141592
name = "Hello"
age = 30
year = 2025
month = 9
day = 10

strData = f"this is {PI}"
print(strData)
strData = f"{name} is {age}"
print(strData)
strData = f"{year}. {month:2}. {day:4}"
print(strData)
strData = f"{year}. {month:0<4}. {day:0^4}"
print(strData)

strData = f"pi is {PI:10.4f}"
print(strData)
strData = f"pi is {PI:010.4f}"
print(strData)
strData = f"pi is {PI:0<10.4f}"
print(strData)
strData = f"pi is {PI:A>10.4f}"
print(strData)
