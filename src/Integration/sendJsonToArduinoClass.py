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
        "commandedSpeed"        : 0.0,                                 # Commanded Speed in m/s
        "currentSpeed"          : 0.0,                                 # Current Speed in m/s
        "authority"             : 0,                                   # Authority in Blocks
        "inputTime"             : "2023-03-26T19:45:19+0000", # RTC Clock in ISO 8601
        "undergroundState"      : False,                               # Underground State
        "speedLimit"            : 0.0,                                 # Speed Limit in m/s
        "temperature"           : 0.0,                                 # Temperature inside the Train in degrees Fahrenheit
        "engineState"           : True,                                # State of the Engine, True if on, False if off
        "stationName"           : "The Yard",                          # Station Name, from the beacon
        "platformSide"          : 0,                                   # Platform Side, 0 if left, 1 if right, 2 if both, from the beacon
        "nextStationName"       : "",                                  # Name of the next station, from the beacon
        "isBeacon"              : False,                               # Whether or not a beacon is active
        "externalLightsState"   : False,                               # State of the External Lights, True if on, False if off
        "internalLightsState"   : False,                               # State of the Internal Lights, True if on, False if off
        "leftDoorState"         : False,                               # State of the Left Doors, True if open, False if closed
        "rightDoorState"        : False,                               # State of the Right Doors, True if open, False if closed
        "serviceBrakeState"     : False,                               # State of the Service Brake, True if engaged, False if disengaged
        "emergencyBrakeState"   : False,                               # State of the Emergency Brake, True if engaged, Flase if disengaged
        "serviceBrakeStatus"    : True,                                # Status of the Service Brake, True if operational, False if offline
        "engineStatus"          : True,                                # Status of the Engine, True if operational, False if offline
        "communicationsStatus"  : True                                 # Status of the Communications with the Track, True if operational, False if offline
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
        self.trainModelToTrainController["inputTime"] = rtc

    def commandedSpeedSignalHandler(self, id, cmdSpeed):
        if (id == 1):
            self.trainModelToTrainController["commandedSpeed"] = cmdSpeed
            # print(cmdSpeed)
        
    def currentSpeedSignalHandler(self, id, currSpeed):
        if (id == 1):
            self.trainModelToTrainController["currentSpeed"] = currSpeed
        
    def authoritySignalHandler(self, id, authority):
        if (id == 1):
            self.trainModelToTrainController["authority"] = authority

    def undergroundSignalHandler(self, id, underground):
        if (id == 1):
            self.trainModelToTrainController["undergroundState"] = underground

    def temperatureSignalHandler(self, id, temp):
        if (id == 1):
           self.trainModelToTrainController["temperature"] = temp 

    def stationNameSignalHandler(self, id, station):
        if (id == 1):
            self.trainModelToTrainController["stationName"] = station

    def platformSideSignalHandler(self, id, platform):
        if (id == 1):
            self.trainModelToTrainController["platformSide"] = platform

    def nextStationNameSignalHandler(self, id, nextStation):
        if (id == 1):
            self.trainModelToTrainController["nextStationName"] = nextStation

    def isBeaconSignalHandler(self, id, isBeacon):
        if (id == 1):
            self.trainModelToTrainController["isBeacon"] = isBeacon

    def externalLightsStateSignalHandler(self, id, eLights):
        if (id == 1):
            self.trainModelToTrainController["externalLightsState"] = eLights

    def internalLightsStateSignalHandler(self, id, iLights):
        if (id == 1):
            self.trainModelToTrainController["internalLightsState"] = iLights

    def leftDoorStateSignalHandler(self, id, lDoors):
        if (id == 1):
            self.trainModelToTrainController["leftDoorState"] = lDoors
        
    def rightDoorStateSignalHandler(self, id, rDoors):
        if (id == 1):
            self.trainModelToTrainController["rightDoorState"] = rDoors
        
    def serviceBrakeStateSignalHandler(self, id, state):
        if (id == 1):
            self.trainModelToTrainController["serviceBrakeState"] = state
        
    def emergencyBrakeStateSignalHandler(self, id, state):
        if (id == 1):
            self.trainModelToTrainController["emergencyBrakeState"] = state
        
    def serviceBrakeStatusSignalHandler(self, id, status):
        if (id == 1):
            self.trainModelToTrainController["serviceBrakeStatus"] = status
        
    def engineStatusSignalHandler(self, id, status):
        if (id == 1):
            self.trainModelToTrainController["engineStatus"] = status
        
    def communicationsStatusSignalHandler(self, id, status):
        if (id == 1):
            self.trainModelToTrainController["communicationsStatus"] = status
    ################################################################################

    def run(self):
        while True:
            #readJsonFromFile()
            # print(trainModelToTrainController)
            # findTimeInSeconds();
            self.parseJson()
            #print(udpMessage)

            print(f'Sending \n{udpMessage} to {self.ip}:{self.port}    Counter:{self.counter}\n')
            
            # print(trainModelToTrainController)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            

            sock.sendto(udpMessage.encode('utf-8'), (self.ip, self.port))
            self.counter+=1
            time.sleep(0.5)
