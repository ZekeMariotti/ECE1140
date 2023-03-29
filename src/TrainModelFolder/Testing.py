from datetime import *
from Conversions import ISO8601ToHumanTime

testTime = datetime.fromisoformat("2023-02-22T23:59:59.10210000-05:00")
testTime2 = datetime.fromisoformat("2023-02-23T00:00:00.19211000-05:00")
print(testTime)
print(testTime2)
tempTime = testTime2 - testTime
print(int((testTime2 - testTime).seconds))
tempInt = int(tempTime.seconds)
print(tempInt)
print(ISO8601ToHumanTime("2023-02-22T11:00:00.0000000-05:00"))