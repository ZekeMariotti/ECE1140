import socket
import time
import os
import sys
import json
#from datetime import *
# import datetime
sys.path.append(__file__.replace("\Integration\sendJsonToArduinoClass.py", ""))
from Integration.TimeSignals import *
from Integration.TMTCSignals import *
from PyQt6.QtCore import QRunnable

class jsonToArduino(QRunnable):
    ip = "192.168.1.101"
    port = 27000
    msg = b"hello world"
    counter = 0

    # Dictionary for outputs to the Train Controller
    trainModelToTrainController = {
        # "id"                    : 0,                                   # ID number for the train
        "cmdSpd"        : 0.0,                                 # Commanded Speed in m/s
        "curSpd"          : 0.0,                                 # Current Speed in m/s
        "auth"             : 0,                                   # Authority in Blocks
        "inT"             : "2023-03-26T19:45:19+0000", # RTC Clock in ISO 8601
        "undSt"      : False,                               # Underground State
        "spdLim"            : 0.0,                                 # Speed Limit in m/s
        "temp"           : 0.0,                                 # Temperature inside the Train in degrees Fahrenheit
        "engSt"           : True,                                # State of the Engine, True if on, False if off
        "stnNm"           : "The Yard",                          # Station Name, from the beacon
        "pltSide"          : 0,                                   # Platform Side, 0 if left, 1 if right, 2 if both, from the beacon
        "nxtStnNm"       : "",                                  # Name of the next station, from the beacon
        "isB"              : False,                               # Whether or not a beacon is active
        "extLiSt"   : False,                               # State of the External Lights, True if on, False if off
        "inLiSt"   : False,                               # State of the Internal Lights, True if on, False if off
        "lftDrSt"         : False,                               # State of the Left Doors, True if open, False if closed
        "rtDrSt"        : False,                               # State of the Right Doors, True if open, False if closed
        "sbSt"     : False,                               # State of the Service Brake, True if engaged, False if disengaged
        "ebSt"   : False,                               # State of the Emergency Brake, True if engaged, Flase if disengaged
        "sbSts"    : True,                                # Status of the Service Brake, True if operational, False if offline
        "engSts"          : True,                                # Status of the Engine, True if operational, False if offline
        "commsSts"  : True                                 # Status of the Communications with the Track, True if operational, False if offline
    }

    udpMessage=""

    def __init__(self):
        super().__init__()
        rtcSignals.rtcSignal.connect(self.catchRealTimeClock)
        TMTCSignals.commandedSpeedSignal.connect(self.commandedSpeedSignalHandler)
        TMTCSignals.currentSpeedSignal.connect(self.currentSpeedSignalHandler)
        TMTCSignals.authoritySignal.connect(self.authoritySignalHandler)
        TMTCSignals.undergroundSignal.connect(self.undergroundSignalHandler)
        TMTCSignals.temperatureSignal.connect(self.temperatureSignalHandler)
        TMTCSignals.stationNameSignal.connect(self.stationNameSignalHandler)
        TMTCSignals.platformSideSignal.connect(self.platformSideSignalHandler)
        TMTCSignals.nextStationNameSignal.connect(self.nextStationNameSignalHandler)
        TMTCSignals.isBeaconSignal.connect(self.isBeaconSignalHandler)
        TMTCSignals.externalLightCommandSignal.connect(self.externalLightsStateSignalHandler)
        TMTCSignals.internalLightCommandSignal.connect(self.internalLightsStateSignalHandler)
        TMTCSignals.leftDoorStateSignal.connect(self.leftDoorStateSignalHandler)
        TMTCSignals.rightDoorStateSignal.connect(self.rightDoorStateSignalHandler)
        TMTCSignals.serviceBrakeStateSignal.connect(self.serviceBrakeStateSignalHandler)
        TMTCSignals.emergencyBrakeStateSignal.connect(self.emergencyBrakeStateSignalHandler)
        TMTCSignals.serviceBrakeStatusSignal.connect(self.serviceBrakeStatusSignalHandler)
        TMTCSignals.engineStatusSignal.connect(self.engineStatusSignalHandler)
        TMTCSignals.communicationsStatusSignal.connect(self.communicationsStatusSignalHandler)

    #def readJsonFromFile():
    #    with open(os.path.join(sys.path[0], "TMtoTC1.json"), "r") as filename:
    #            global trainModelToTrainController
    #            try:
    #                trainModelToTrainController = json.loads(filename.read())
    #            except json.decoder.JSONDecodeError:
    #                trainModelToTrainController = trainModelToTrainController

    def parseJson(self):
        global udpMessage
        udpMessage = json.dumps(self.trainModelToTrainController)
        # print(udpMessage)

    #def findTimeInSeconds():
    #        if (trainModelToTrainController["inputTime"] != ""):
    #            clock = datetime.fromisoformat(trainModelToTrainController["inputTime"])
    #            print (float(clock.seconds))

    ################################################################################
    # FROM Traim Model
    def catchRealTimeClock(self, rtc):
        self.trainModelToTrainController["inT"] = rtc

    def commandedSpeedSignalHandler(self, id, cmdSpeed):
        if (id == 1):
            self.trainModelToTrainController["cmdSpd"] = cmdSpeed
            # print(cmdSpeed)
        
    def currentSpeedSignalHandler(self, id, currSpeed):
        if (id == 1):
            self.trainModelToTrainController["curSpd"] = currSpeed
        
    def authoritySignalHandler(self, id, authority):
        if (id == 1):
            self.trainModelToTrainController["auth"] = authority

    def undergroundSignalHandler(self, id, underground):
        if (id == 1):
            self.trainModelToTrainController["undSt"] = underground

    def temperatureSignalHandler(self, id, temp):
        if (id == 1):
           self.trainModelToTrainController["temp"] = temp 

    def stationNameSignalHandler(self, id, station):
        if (id == 1):
            self.trainModelToTrainController["stnNm"] = station

    def platformSideSignalHandler(self, id, platform):
        if (id == 1):
            self.trainModelToTrainController["pltSide"] = platform

    def nextStationNameSignalHandler(self, id, nextStation):
        if (id == 1):
            self.trainModelToTrainController["nxtStnNm"] = nextStation

    def isBeaconSignalHandler(self, id, isBeacon):
        if (id == 1):
            # if (self.trainModelToTrainController["isBeacon"] != isBeacon):
            self.trainModelToTrainController["isB"] = isBeacon
            self.beaconHold(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))


    def externalLightsStateSignalHandler(self, id, eLights):
        if (id == 1):
            self.trainModelToTrainController["extLiSt"] = eLights

    def internalLightsStateSignalHandler(self, id, iLights):
        if (id == 1):
            self.trainModelToTrainController["inLiSt"] = iLights

    def leftDoorStateSignalHandler(self, id, lDoors):
        if (id == 1):
            self.trainModelToTrainController["lftDrSt"] = lDoors
        
    def rightDoorStateSignalHandler(self, id, rDoors):
        if (id == 1):
            self.trainModelToTrainController["rtDrSt"] = rDoors
        
    def serviceBrakeStateSignalHandler(self, id, state):
        if (id == 1):
            self.trainModelToTrainController["sbSt"] = state
        
    def emergencyBrakeStateSignalHandler(self, id, state):
        if (id == 1):
            self.trainModelToTrainController["ebSt"] = state
        
    def serviceBrakeStatusSignalHandler(self, id, status):
        if (id == 1):
            self.trainModelToTrainController["sbSts"] = status
        
    def engineStatusSignalHandler(self, id, status):
        if (id == 1):
            self.trainModelToTrainController["engSts"] = status
        
    def communicationsStatusSignalHandler(self, id, status):
        if (id == 1):
            self.trainModelToTrainController["commsSts"] = status
    ################################################################################
    def beaconHold(self, sock):
        if (self.trainModelToTrainController["isB"]==1):
            self.parseJson()
            sock.sendto(udpMessage.encode('utf-8'), (self.ip, self.port))




    def run(self):
        while True:
            #readJsonFromFile()
            # print(trainModelToTrainController)
            # findTimeInSeconds();
            self.parseJson()
            #print(udpMessage)

            # print(f'Sending \n{udpMessage} to {self.ip}:{self.port}    Counter:{self.counter}\n')
            
            # print(trainModelToTrainController)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # self.beaconHold(sock)
            # self.parseJson()
            if (self.trainModelToTrainController["isB"]!=1):
                sock.sendto(udpMessage.encode('utf-8'), (self.ip, self.port))
            self.counter+=1
            time.sleep(0.2)
