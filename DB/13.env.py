import os


uID = os.environ["DBUSERID"]
uPW = os.environ["DBUSERPW"]
dbname = os.environ["DBNAME"]
print(f"DBUSERID: {uID} DBUSERPW: {uPW} DBNAME: {dbname}")

varName = "PYHTON_HOME"

if varName in os.environ:
    result = os.environ[varName]
    print(f"{varName} = {result}")
else:
    print(f"{varName} not found in environment variables.")


result = os.environ.get("PYHTON_HOME")
print(f"PYHTON_HOME = {result}")

result = os.environ.get("PYTHON_HOME", "C:/conda.evns/ezen")
print(f"PYHTON_HOME = {result}")

result = os.environ.get("JAVA_HOME", "C:/Program Files/Java")
print(f"JAVA_HOME = {result}")

result = os.environ.get("AICLASS", "DEFAULT VALUE")
print(f"AICLASS = {result}")


