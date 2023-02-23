from datetime import *
from distutils.cmd import Command
import sys
import os
import json
from json import JSONEncoder

class WaysideController:
    def __init__(self, commandedSpeed, authority,occupancy,inputTime,realTime,trackOperational,brokenRail,switchPositions,gatePosition,PLC,signalLights):
        #
        redSwitches = [False,False,False,False,False,False,False]
        #get methods
        def getCommandedSpeed(self):
            return(commandedSpeed)
        def getAuthority(self):
            return(authority)
        def getOccupancy(self):
            return(occupancy)
        def getTime(self):
            return(time)
        def getTrackOperational(self):
            return(trackOperational)
        def getbrokenRail(self):
            return(brokenRail)
        def getswitchPositions(self):
            return(switchPositions)
        def getGatePositions(self):
            return(gatePosition)
        def getSignalLights(self):
            return(signalLights)
        #no need to return PLC 
        #set methods
        def setCommandedSpeed(self,commandedSpeed):
            self.commandedSpeed = commandedSpeed
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
        def setGatePositions(self):
            return(gatePosition)
        def setSignalLights(self):
            return(signalLights)
        #Unfinished methods
        def uploadPLC(self):
            return()
        def sendDataCTC(self):
            return()
        def sendDataTrackModel(self):
            return()

        