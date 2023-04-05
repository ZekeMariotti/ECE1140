import socket
import json
import os
import sys
import time

sys.path.append(__file__.replace("\Integration\\receiveJsonFromArduinoClass.py", ""))
from Integration.TMTCSignals import *
from PyQt6.QtCore import QRunnable

class arduinoToJson(QRunnable):

    ip = "192.168.1.2"
    port = 27001

    def __init__(self):
        super().__init__()

        # UNCOMMENT IF WORKING WITH REAL HARDWARE
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.ip, self.port))

        print(f'Start listening to {self.ip}:{self.port}')


        self.trainControllerToTrainModel = {
            "power"                 : 0.0,       # Power input from the Train Controller
            "leftDoorCommand"       : False,     # Left Door Command from the Train Controller, False if closed, True if open
            "rightDoorCommand"      : False,     # Right Door Command from the Train Controller, False if closed, True if open
            "serviceBrakeCommand"   : False,     # Service Brake Command from the Train Controller, True if engaged, False is disengaged
            "emergencyBrakeCommand" : False,     # Emergency Brake Command from the Train Controller, True if engaged, False is isengaged
            "externalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
            "internalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
            "stationAnnouncement"   : "The Yard", # Station Announcement from the Train Controller
            "isAtStation"           : False
        }

    # JSON function to write outputs to a JSON file for the Train Controller
    def writeToJson(self):
        self.trainControllerToTrainModel["emergencyBrakeCommand"]=0
        with open(os.path.join(sys.path[0], "TCtoTM1.json"), "w") as filename:
                (json.dump(self.trainControllerToTrainModel, filename, indent = 4))

    # # def getDataFromTrainController():


    # def parseToJson():
    #     #TODO: parse the ArduinoJSON here to a python dictionary
    def getDataFromTrainController(self):
        with open(os.path.join(sys.path[0], "TrainControllerToTrainModel.json"), "w") as filename:
                (json.dump(self.trainControllerToTrainModel, filename, indent = 4))

    def parseToJson():
        #TODO: parse the ArduinoJSON here to a python dictionary
        pass

    # # def getDataFromTrainController():


    # def parseToJson():
    #     #TODO: parse the ArduinoJSON here to a python dictionary

    def emitSignals(self):
        # EMITTING SIGNALS TO TRAIN MODEL
        #TMTCSignals.commandedPowerSignal.emit(1, trainControllerToTrainModel["power"])
        TMTCSignals.commandedPowerSignal.emit(1, self.trainControllerToTrainModel["power"])
        TMTCSignals.leftDoorCommandSignal.emit(1, self.trainControllerToTrainModel["leftDoorCommand"])
        TMTCSignals.rightDoorCommandSignal.emit(1, self.trainControllerToTrainModel["rightDoorCommand"])
        TMTCSignals.serviceBrakeCommandSignal.emit(1, self.trainControllerToTrainModel["serviceBrakeCommand"])
        TMTCSignals.emergencyBrakeCommandSignal.emit(1, self.trainControllerToTrainModel["emergencyBrakeCommand"])
        TMTCSignals.externalLightCommandSignal.emit(1, self.trainControllerToTrainModel["externalLightCommand"])
        TMTCSignals.internalLightCommandSignal.emit(1, self.trainControllerToTrainModel["internalLightCommand"])
        TMTCSignals.stationAnnouncementSignal.emit(1, self.trainControllerToTrainModel["stationAnnouncement"])
        TMTCSignals.stationStateSignal.emit(1, self.trainControllerToTrainModel["isAtStation"])

    def run(self):
        while True:
            self.data, self.addr = self.sock.recvfrom(1024) # buffer
            #print(f"received message: {data}")
            #print(type(data))
            self.trainControllerToTrainModel = json.loads(self.data)

            print("Recieve")
            print(self.trainControllerToTrainModel)

            #parseToJson()
            #self.trainControllerToTrainModel["emergencyBrakeCommand"] = 0
            #writeToJson()
            self.emitSignals()
            time.sleep(0.5)
            #print(f"received message: {data}")