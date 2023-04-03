from datetime import *
from math import exp
import time
import sys
import os
sys.path.append(__file__.replace("\TrainModelFolder\Testing.py", ""))

from Integration.Conversions import ISO8601ToHumanTime

#testTime = datetime.now()
#time.sleep(0.5)
#testTime2 = datetime.now()
#print(testTime)
#print(testTime2)
##print(timedelta(testTime2, testTime))
#timeDiff = timedelta
#timeDiff = testTime2 - testTime
#totalSeconds = timeDiff.total_seconds()
#print(totalSeconds * 1)
#print(testTime.isoformat() + "-05:00")
#print(ISO8601ToHumanTime("2023-02-22T11:00:00.0000000-05:00"))

x = 68 * exp(-5 * 2)
print(x)
x = 68 * exp(-5 * .1)
print(x)

os.path.join(sys.path[0], "")
print(sys.path[0])