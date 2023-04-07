from TestGenericWayside import Wayside
from PLC import PLC
import sys
import os

File1 = os.path.join(sys.path[0], "GreenLine.txt")
File2 = os.path.join(sys.path[0], "GreenLine2.txt")
#test 1 Check switch change
def testPLCSwitchChange():
        TestWayside = Wayside(1,2)
        PLCMain = PLC(TestWayside,TestWayside,"Green")
        TestWayside.setdictionarysizes(1,151,7)
        TestWayside.setOccupancy(14,True)
        PLCMain.GloadValues1(File1)
        PLCMain.setswitches()
        assert TestWayside.switches[1]==False
        print("First Test passed")
        TestWayside.setOccupancy(14,False)
        TestWayside.setOccupancy(1,True)
        PLCMain.GloadValues1(File1)
        PLCMain.setswitches()        
        assert TestWayside.switches[1]==True
        print("Second Test passed")
testPLCSwitchChange()
    

