import sys
import datetime

print("Hello world")

print("Current version: ", sys.version)

now = datetime.datetime.now()

print("Current time: ", now)
print("Formatted: ", now.strftime("%m-%d-%Y %H:%M:%S"))
