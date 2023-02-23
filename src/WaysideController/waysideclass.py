from datetime import *
from distutils.cmd import Command
import sys
import os
import json
from json import JSONEncoder
#dictionary of suggested speeds
suggestedSpeed = {
    "Block 1": 0,
    "Block 2": 0,
    "Block 3": 0,
    "Block 4": 0,
    "Block 5": 0,
    "Block 6": 0,
    "Block 7": 0,
    "Block 8": 0,
    "Block 9": 0,
    "Block 10": 0,
    "Block 11": 0,
    "Block 12": 0,
    "Block 13": 0,
    "Block 14": 0,
    "Block 15": 0
}
#dictionary of commanded speeds
commandedSpeed = {
    "Block 1": 0,
    "Block 2": 0,
    "Block 3": 0,
    "Block 4": 0,
    "Block 5": 0,
    "Block 6": 0,
    "Block 7": 0,
    "Block 8": 0,
    "Block 9": 0,
    "Block 10": 0,
    "Block 11": 0,
    "Block 12": 0,
    "Block 13": 0,
    "Block 14": 0,
    "Block 15": 0
}
#dictionary of authority
authority = {
    "Block 1": 0,
    "Block 2": 0,
    "Block 3": 0,
    "Block 4": 0,
    "Block 5": 0,
    "Block 6": 0,
    "Block 7": 0,
    "Block 8": 0,
    "Block 9": 0,
    "Block 10": 0,
    "Block 11": 0,
    "Block 12": 0,
    "Block 13": 0,
    "Block 14": 0,
    "Block 15": 0
}
#dictionary of Light states
signalLights = {
    "Block 1": "R",
    "Block 2": "R",
    "Block 3": "R",
    "Block 4": "R",
    "Block 5": "R",
    "Block 6": "R",
    "Block 7": "R",
    "Block 8": "R",
    "Block 9": "R",
    "Block 10": "R",
    "Block 11": "R",
    "Block 12": "R",
    "Block 13": "R",
    "Block 14": "R",
    "Block 15": "R"
}
#Dictionary of block occupancy
occupancy = {
    "Block 1": False,
    "Block 2": False,
    "Block 3": True,
    "Block 4": True,
    "Block 5": True,
    "Block 6": False,
    "Block 7": False,
    "Block 8": False,
    "Block 9": False,
    "Block 10": False,
    "Block 11": False,
    "Block 12": False,
    "Block 13": False,
    "Block 14": False,
    "Block 15": False
}
brokenrail = {
    "Block 1": False,
    "Block 2": False,
    "Block 3": False,
    "Block 4": False,
    "Block 5": False,
    "Block 6": False,
    "Block 7": True,
    "Block 8": False,
    "Block 9": False,
    "Block 10": False,
    "Block 11": False,
    "Block 12": False,
    "Block 13": False,
    "Block 14": False,
    "Block 15": False
}
# should have dictionaries of switch for red and green but blue only has one so this will wait

class WaysideController:
    def __init__(self,givenTime,trackOperational,switchPositions,gatePosition,PLC):
            self.time=givenTime
            self.trackOperational=trackOperational
            #change in future installents
            self.switchPositions=switchPositions
            #should probaly make dictionary of red and green line gate to differentiatse in future builds
            self.gatePosition=gatePosition
            #file name
            self.PLC=PLC
   
    def getCommandedSpeed(self,x):
            return(commandedSpeed.get(x))
        
    def getAuthority(self,x):
            return(authority.get(x))
        
    def getOccupancy(self,x):
            return(occupancy.get(x))
        
    def getTime(self):
            return(self.givenTime)
        
    def getTrackOperational(self):
            return(self.trackOperational)
        
    def getBrokenRail(self,x):
            return(brokenrail.get(x))
        
    def getswitchPositions(self):
            return(self.switchPositions)
        
    def getGatePositions(self):
            return(self.gatePosition)
        
    def getSignalLights(self,x):
            return(signalLights.get(x))
        
        #no need to return PLC 
        #set methods
    def setCommandedSpeed(self,suggestedSpeed,x):
        if suggestedSpeed > 70:
            pass
        else:
            pass 

    def setAuthority(self,authority):
            self.authority = authority

    def setOccupancy(self,occupancy):
            self.occupancy = occupancy

    def setTime(self,time):
            self.time = time

    def setTrackOperational(self, trackOperational):
            self.trackOperational = trackOperational

    def setBrokenRail(self,brokenRail):
            self.brokenrail = brokenRail

    def setswitchPositionsGreen(self,logic):
            pass
        
    def setGatePositions(self,Direction):
            self.gatePosition=Direction
    def setSignalLights(self,Color):
            self.signalLights = Color
        #Unfinished methods
    def uploadPLC(self):
            return()
    def sendDataCTC(self):
            return()
    def sendDataTrackModel(self):
            return()
