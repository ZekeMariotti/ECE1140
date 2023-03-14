from datetime import *
from distutils.cmd import Command
import sys
import os
import json
from json import JSONEncoder
#dictionary of suggested speeds
suggestedSpeed = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    19: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0,
    26: 0,
    27: 0,
    28: 0,
    29: 0,
    30: 0,
    31: 0,
    32: 0,
    33: 0,
    34: 0,
    35: 0,
    36: 0,
    37: 0,
    38: 0,
    39: 0,
    40: 0,
    41: 0,
    42: 0,
    43: 0,
    44: 0,
    45: 0,
    46: 0,
    47: 0,
    48: 0,
    49: 0,
    50: 0,
    51: 0,
    52: 0,
    53: 0,
    54: 0,
    55: 0,
    56: 0,
    57: 0,
    58: 0,
    59: 0,
    60: 0,
    61: 0,
    62: 0,
    63: 0,
    64: 0,
    65: 0,
    66: 0,
    67: 0,
    68: 0,
    69: 0,
    70: 0,
    71: 0,
    72: 0,
    73: 0,
    74: 0,
    75: 0,
    76: 0
}
#dictionary of commanded speeds
commandedSpeed = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    19: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0,
    26: 0,
    27: 0,
    28: 0,
    29: 0,
    30: 0,
    31: 0,
    32: 0,
    33: 0,
    34: 0,
    35: 0,
    36: 0,
    37: 0,
    38: 0,
    39: 0,
    40: 0,
    41: 0,
    42: 0,
    43: 0,
    44: 0,
    45: 0,
    46: 0,
    47: 0,
    48: 0,
    49: 0,
    50: 0,
    51: 0,
    52: 0,
    53: 0,
    54: 0,
    55: 0,
    56: 0,
    57: 0,
    58: 0,
    59: 0,
    60: 0,
    61: 0,
    62: 0,
    63: 0,
    64: 0,
    65: 0,
    66: 0,
    67: 0,
    68: 0,
    69: 0,
    70: 0,
    71: 0,
    72: 0,
    73: 0,
    74: 0,
    75: 0,
    76: 0,
}
#dictionary of authority
authority = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
    17: 0,
    18: 0,
    19: 0,
    20: 0,
    21: 0,
    22: 0,
    23: 0,
    24: 0,
    25: 0,
    26: 0,
    27: 0,
    28: 0,
    29: 0,
    30: 0,
    31: 0,
    32: 0,
    33: 0,
    34: 0,
    35: 0,
    36: 0,
    37: 0,
    38: 0,
    39: 0,
    40: 0,
    41: 0,
    42: 0,
    43: 0,
    44: 0,
    45: 0,
    46: 0,
    47: 0,
    48: 0,
    49: 0,
    50: 0,
    51: 0,
    52: 0,
    53: 0,
    54: 0,
    55: 0,
    56: 0,
    57: 0,
    58: 0,
    59: 0,
    60: 0,
    61: 0,
    62: 0,
    63: 0,
    64: 0,
    65: 0,
    66: 0,
    67: 0,
    68: 0,
    69: 0,
    70: 0,
    71: 0,
    72: 0,
    73: 0,
    74: 0,
    75: 0,
    76: 0,
}
#dictionary of Light states
signalLights = {
    1: "R",
    2: "R",
    3: "R",
    4: "R",
    5: "R",
    6: "R",
    7: "R",
    8: "R",
    9: "R",
    10: "R",
    11: "R",
    12: "R",
    13: "R",
    14: "R",
    15: "R",
    16: "R",
    17: "R",
    18: "R",
    19: "R",
    20: "R",
    21: "R",
    22: "R",
    23: "R",
    24: "R",
    25: "R",
    26: "R",
    27: "R",
    28: "R",
    29: "R",
    30: "R",
    31: "R",
    32: "R",
    33: "R",
    34: "R",
    35: "R",
    36: "R",
    37: "R",
    38: "R",
    39: "R",
    40: "R",
    41: "R",
    42: "R",
    43: "R",
    44: "R",
    45: "R",
    46: "R",
    47: "R",
    48: "R",
    49: "R",
    50: "R",
    51: "R",
    52: "R",
    53: "R",
    54: "R",
    54: "R",
    55: "R",
    56: "R",
    57: "R",
    58: "R",
    59: "R",
    60: "R",
    61: "R",
    62: "R",
    63: "R",
    64: "R",
    65: "R",
    66: "R",
    67: "R",
    68: "R",
    69: "R",
    70: "R",
    71: "R",
    72: "R",
    73: "R",
    74: "R",
    75: "R",
    76: "R",
}
#Dictionary of block occupancy
occupancy = {
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    8: True,
    9: True,
    10: True,
    11: True,
    12: True,
    13: True,
    14: True,
    15: True,
    16: True,
    17: True,
    18: True,
    19: True,
    20: True,
    21: True,
    22: True,
    23: True,
    24: True,
    25: True,
    26: True,
    27: True,
    28: True,
    29: True,
    30: True,
    31: True,
    32: True,
    33: True,
    34: True,
    35: True,
    36: True,
    37: True,
    38: True,
    39: True,
    40: True,
    41: True,
    42: True,
    43: True,
    44: True,
    45: True,
    46: True,
    47: True,
    48: True,
    49: True,
    50: True,
    51: True,
    52: True,
    53: True,
    54: True,
    55: True,
    56: True,
    57: True,
    58: True,
    59: True,
    60: True,
    61: True,
    62: True,
    63: True,
    64: True,
    65: True,
    66: True,
    67: True,
    68: True,
    69: True,
    70: True,
    71: True,
    72: True,
    73: True,
    74: True,
    75: True,
    76: True
}
brokenrail = {
     1: False,
     2: False,
     3: False,
     4: False,
     5: False,
     6: False,
     7: False,
     8: False,
     9: False,
    10: False,
    11: False,
    12: False,
    13: False,
    14: False,
    15: False,
    16: False,
    17: False,
    18: False,
    19: False,
    20: False,
    21: False,
    22: False,
    23: False,
    24: False,
    25: False,
    26: False,
    27: False,
    28: False,
    29: False,
    30: False,
    31: False,
    32: False,
    33: False,
    34: False,
    35: False,
    36: False,
    37: False,
    38: False,
    39: False,
    40: False,
    41: False,
    42: False,
    43: False,
    44: False,
    45: False,
    46: False,
    47: False,
    48: False,
    49: False,
    50: False,
    51: False,
    52: False,
    53: False,
    54: False,
    55: False,
    56: False,
    57: False,
    58: False,
    59: False,
    60: False,
    61: False,
    62: False,
    63: False,
    64: False,
    65: False,
    66: False,
    67: False,
    68: False,
    69: False,
    70: False,
    71: False,
    72: False,
    73: False,
    74: False,
    75: False,
    76: False
}
switches = {
       1: True,
       2: True,
       3: True,
       4: True,
       5: True,
       6: True,
       7: True
}
gates = {
       1: True
}
class WaysideControllerRed:
    def __init__(self,inputTime,trackOperational):
            self.realTime=None
            self.currentTime=None
            self.previousTime=None
            self.trackOperational=trackOperational
            
   
    def getCommandedSpeed(self,x):
            return(suggestedSpeed.get(x))
        
    def getAuthority(self,x):
            return(authority.get(x))
        
    def getOccupancy(self,x):
            return(occupancy.get(x))
        
    def getTime(self):
            return(self.inputTime)
        
    def getTrackOperational(self):
            return(self.trackOperational)
        
    def getBrokenRail(self,x):
            return(brokenrail.get(x))
        
    def getSwitchPositions(self,x):
            return(switches.get(x))
        
    def getGatePositions(self):
            return(gates.get(1))
        
    def getSignalLights(self,x):
            return(signalLights.get(x))
        
    def setSuggestedSpeed(self,suggestedSpeed,Block):
           if suggestedSpeed[Block]>70 | suggestedSpeed[Block]<0:
                  suggestedSpeed[Block]=0
           else:
                  suggestedSpeed[Block]=suggestedSpeed

    def setCommandedSpeed(self,suggestedSpeed,Block):
        commandedSpeed=suggestedSpeed*0.621371
        commandedSpeed[Block]=commandedSpeed

    def setAllCommandedSpeed(self):
           for i in range (1,77):
            commandedSpeed[i]=suggestedSpeed[i]*0.621371

    def setAuthority(self,authority,Block):
        authority[Block]=authority

    def setOccupancy(self,occupancy,Block):
        occupancy[Block]=occupancy

    def setTime(self,time):
            self.time = time

    def setTrackOperational(self, trackOperational):
            self.trackOperational = trackOperational

    def setBrokenRail(self,brokenRail):
            self.brokenrail = brokenRail

    def setSwitchPositions(self,logic,number):
            switches[number]=logic

    def setGatePositions(self,Direction):
            gates[1]=Direction

    def setSignalLights(self,Color):
            self.signalLights = Color

    def convertTime(self):
            inputTime = stringRemove(self.time, 26)
            self.realTime = datetime.strptime(inputTime, "%Y-%m-%dT%H:%M:%S.%f%z")  
    #unfinishedPLC
    def uploadPLC(self,file):
            return()     
           
def stringRemove(string, n):  
        first = string[: n]   
        last = string[n+1:]  
        return first + last

