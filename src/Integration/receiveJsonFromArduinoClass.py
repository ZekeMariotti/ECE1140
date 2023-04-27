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
            "pwr"                 : 0.0,       # Power input from the Train Controller
            "lftDrCmd"       : False,     # Left Door Command from the Train Controller, False if closed, True if open
            "rtDrCmd"      : False,     # Right Door Command from the Train Controller, False if closed, True if open
            "sbCmd"   : False,     # Service Brake Command from the Train Controller, True if engaged, False is disengaged
            "ebCmd" : False,     # Emergency Brake Command from the Train Controller, True if engaged, False is isengaged
            "extLiCmd"  : False,     # External Light Command from the Train Controller, True if on, False if off
            "intLiCmd"  : False,     # External Light Command from the Train Controller, True if on, False if off
            "stAnn"   : "The Yard", # Station Announcement from the Train Controller
            "isAtStn"           : False
        }

    # JSON function to write outputs to a JSON file for the Train Controller
    # def writeToJson(self):
    #     self.trainControllerToTrainModel["emergencyBrakeCommand"]=0
    #     with open(os.path.join(sys.path[0], "TCtoTM1.json"), "w") as filename:
    #             (json.dump(self.trainControllerToTrainModel, filename, indent = 4))

    # # def getDataFromTrainController():


    # def parseToJson():
    #     #TODO: parse the ArduinoJSON here to a python dictionary
    # def getDataFromTrainController(self):
    #     with open(os.path.join(sys.path[0], "TrainControllerToTrainModel.json"), "w") as filename:
    #             (json.dump(self.trainControllerToTrainModel, filename, indent = 4))

    def parseToJson():
        #TODO: parse the ArduinoJSON here to a python dictionary
        pass

    # # def getDataFromTrainController():


    # def parseToJson():
    #     #TODO: parse the ArduinoJSON here to a python dictionary

    def emitSignals(self):
        # EMITTING SIGNALS TO TRAIN MODEL
        #TMTCSignals.commandedPowerSignal.emit(1, trainControllerToTrainModel["power"])
        TMTCSignals.commandedPowerSignal.emit(1, self.trainControllerToTrainModel["pwr"])
        TMTCSignals.leftDoorCommandSignal.emit(1, self.trainControllerToTrainModel["lftDrCmd"])
        TMTCSignals.rightDoorCommandSignal.emit(1, self.trainControllerToTrainModel["rtDrCmd"])
        TMTCSignals.serviceBrakeCommandSignal.emit(1, self.trainControllerToTrainModel["sbCmd"])
        TMTCSignals.emergencyBrakeCommandSignal.emit(1, self.trainControllerToTrainModel["ebCmd"])
        TMTCSignals.externalLightCommandSignal.emit(1, self.trainControllerToTrainModel["extLiCmd"])
        TMTCSignals.internalLightCommandSignal.emit(1, self.trainControllerToTrainModel["intLiCmd"])
        TMTCSignals.stationAnnouncementSignal.emit(1, self.trainControllerToTrainModel["stAnn"])
        TMTCSignals.stationStateSignal.emit(1, self.trainControllerToTrainModel["isAtStn"])

    def run(self):
        while True:
            self.data, self.addr = self.sock.recvfrom(1024) # buffer
            #print(f"received message: {data}")
            #print(type(data))
            self.trainControllerToTrainModel = json.loads(self.data)

            # print("Recieve")
            # print(self.trainControllerToTrainModel)

            #parseToJson()
            #self.trainControllerToTrainModel["emergencyBrakeCommand"] = 0
            #writeToJson()
            self.emitSignals()
            time.sleep(0.05)
            #print(f"received message: {data}")