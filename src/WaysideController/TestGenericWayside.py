from datetime import *
from distutils.cmd import Command
import sys
import os
import json
from json import JSONEncoder

class Wayside:
    def __init__(self,simTime,maintenance):
            self.simTime=simTime
            self.maintenance=maintenance
            self.gates={}
            self.suggestedAuthority={}
            self.authority={}
            self.suggestedSpeed={}
            self.commandedSpeed={}
            self.signalLights={}
            self.switches={}
            self.occupancy={}
            self.brokenRail={}
            self.WaysideToTrack={
                 "Authority" :self.authority,
                 "Gates" :self.gates,
                 "Commanded Speed":self.commandedSpeed,
                 "Switches":self.switches,
                 "SimTime":self.simTime,
                 "Lights":self.signalLights
            }
            self.WaysideToCTC={
                  "Switches":self.switches,
                  "Lights":self.signalLights,
                  "Occupancy":self.occupancy,
                  "BrokenRail":self.brokenRail,
                  "Gates":self.gates
            }
        
    def setdictionarysizes(self,start,blocks,switches):
          for i in range (start,blocks):
                self.suggestedAuthority[i] = 0
          for i in range (start,blocks):
                self.suggestedSpeed[i] = 0
          self.switches[1] = False
          self.switches[2] = False
          self.switches[3] = True
          self.switches[4] = True
          self.switches[5] = False
          self.switches[6] = False
          for i in range(start,blocks):
                self.occupancy[i] = False
          for i in range(start,blocks):
                self.signalLights[i] = True
          for i in range(start,blocks):
                self.brokenRail[i]=False
          self.gates[1] = True
        # simple error checking
    def setCommandedSpeed(self):
        for i in self.suggestedSpeed:
            if self.suggestedSpeed[i]>70 | self.suggestedSpeed[i]<0:
                self.commandedSpeed[i]=0
            else:
                self.commandedSpeed[i]=self.suggestedSpeed[i]
    def setACommandedSpeed(self,Value,block):
          self.commandedSpeed[block]=Value         
    def setAuthority(self):
        for i in self.suggestedAuthority:
            if self.suggestedAuthority[i]>150 | self.suggestedAuthority[i]<0:
                self.authority[i]=0
            else:
                self.authority[i]=self.suggestedAuthority[i]

    def setAAuthority(self,Value,block):
         self.authority[block]=Value
         
    def setOccupancy(self,occupancy,Block):
        self.occupancy[Block]=occupancy

    def setTime(self,time):
            self.time = time

    def setTrackOperational(self, trackOperational):
            self.trackOperational = trackOperational

    def setBrokenRail(self,logic,number):
            self.brokenRail[number] = logic

    def setSwitchPositions(self,logic,number):
            self.switches[number]=logic

    def setGatePositions(self,Direction):
            self.gates[1]=Direction

    def setSignalLights(self,logic,number):
            self.signalLights[number]=logic
    
    def setSuggestedSpeed(self,block,value):
            self.suggestedSpeed[block]=value

    def setSuggestedAuthority(self,block,value):
            self.suggestedAuthority[block]=value
            
    def convertTime(self):
            inputTime = stringRemove(self.time, 26)
            self.realTime = datetime.strptime(inputTime, "%Y-%m-%dT%H:%M:%S.%f%z") 
            
    def uploadPLC(self,file):
            return()     
    def WaysideToTrackInfoG1(self):
        with open(os.path.join(sys.path[0],"Green1Track.json"), "w") as filename:
            (json.dump(self.WaysideToTrack, filename, indent = 4))
    def WaysideToTrackInfoG2(self):
        with open(os.path.join(sys.path[0],"Green2Track.json"), "w") as filename:
            (json.dump(self.WaysideToTrack, filename, indent = 4))
    def WaysideToTrackInfoR1(self):
        with open(os.path.join(sys.path[0],"Red1Track.json"), "w") as filename:
            (json.dump(self.WaysideToTrack, filename, indent = 4))
    def WaysideToTrackInfoR2(self):
        with open(os.path.join(sys.path[0],"Red2Track.json"), "w") as filename:
            (json.dump(self.WaysideToTrack, filename, indent = 4))                
    def WaysideToCTCInfoG1(self):
        with open(os.path.join(sys.path[0], "Green1CTC.json"), "w") as filename:
            (json.dump(self.WaysideToCTC, filename, indent = 4))
    def WaysideToCTCInfoG2(self):
        with open(os.path.join(sys.path[0], "Green2CTC.json"), "w") as filename:
            (json.dump(self.WaysideToCTC, filename, indent = 4))          
    def WaysideToCTCInfoR1(self):
        with open(os.path.join(sys.path[0], "Red1CTC.json"), "w") as filename:
            (json.dump(self.WaysideToCTC, filename, indent = 4))
    def WaysideToCTCInfoR2(self):
        with open(os.path.join(sys.path[0], "Red2CTC.json"), "w") as filename:
            (json.dump(self.WaysideToCTC, filename, indent = 4))

    def readTrackModelToWayside(self):
        with open(os.path.join(sys.path[0], ".json"), "r") as filename:
            self.TrackToWayside = json.loads(filename.read())

        # Loading internal inputs data variable
        self.data["occupancy"]                 = self.occupancy
        self.data["brokenRail"]               = self.brokenRail

    def readCTCToWayside(self):
        with open(os.path.join(sys.path[0],".json"),"r") as filename:
            self.CTCToWayside = json.loads(filename.read())
        self.data["suggestedSpeed"] =self.suggestedSpeed
        self.data["RTC"]=self.realTime
        self.data["authority"]=self.authority

    

def stringRemove(string, n):  
        first = string[: n]   
        last = string[n+1:]  
        return first + last