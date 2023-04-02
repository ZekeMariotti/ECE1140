import socket
import json
import os
import sys
import time

# ip = "127.0.0.1"
# port = 27000

ip = "192.168.1.3"
port = 27001
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind((ip, port))
print(f'Start listening to {ip}:{port}')


trainControllerToTrainModel = {
    "power"                 : 0.0,       # Power input from the Train Controller
    "leftDoorCommand"       : False,     # Left Door Command from the Train Controller, False if closed, True if open
    "rightDoorCommand"      : False,     # Right Door Command from the Train Controller, False if closed, True if open
    "serviceBrakeCommand"   : False,     # Service Brake Command from the Train Controller, True if engaged, False is disengaged
    "emergencyBrakeCommand" : False,     # Emergency Brake Command from the Train Controller, True if engaged, False is isengaged
    "externalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
    "InternalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
    "stationAnnouncement"   : "The Yard", # Station Announcement from the Train Controller
    "isAtStation"           : False
}




# JSON function to write outputs to a JSON file for the Train Controller
def writeToJson():
    trainControllerToTrainModel["emergencyBrakeCommand"]=0
    with open(os.path.join(sys.path[0], "TCtoTM1.json"), "w") as filename:
            (json.dump(trainControllerToTrainModel, filename, indent = 4))

# # def getDataFromTrainController():


# def parseToJson():
#     #TODO: parse the ArduinoJSON here to a python dictionary
def getDataFromTrainController():
    with open(os.path.join(sys.path[0], "TrainControllerToTrainModel.json"), "w") as filename:
            (json.dump(trainControllerToTrainModel, filename, indent = 4))

def parseToJson():
    #TODO: parse the ArduinoJSON here to a python dictionary
    pass

# # def getDataFromTrainController():


# def parseToJson():
#     #TODO: parse the ArduinoJSON here to a python dictionary


while True:
    data, addr = sock.recvfrom(1024) # buffer
    print(f"received message: {data}")
    # print(type(data))
    trainControllerToTrainModel = json.loads(data)
    print(trainControllerToTrainModel)
    parseToJson()
    trainControllerToTrainModel["emergencyBrakeCommand"]=0
    writeToJson()
    time.sleep(0.5)
    print(f"received message: {data}")