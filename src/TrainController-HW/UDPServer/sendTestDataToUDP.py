import socket
import time
import json
ip = "127.0.0.1"
port = 27000
msg = b"hello world"
counter = 0

# Dictionary for outputs to the Train Controller

trainControllerToTrainModel = {
    "id"                    : 0,         # ID number for the train
    "power"                 : 0.0,       # Power input from the Train Controller
    "leftDoorCommand"       : False,     # Left Door Command from the Train Controller, False if closed, True if open
    "rightDoorCommand"      : False,     # Right Door Command from the Train Controller, False if closed, True if open
    "serviceBrakeCommand"   : False,     # Service Brake Command from the Train Controller, True if engaged, False is disengaged
    "emergencyBrakeCommand" : False,     # Emergency Brake Command from the Train Controller, True if engaged, False is isengaged
    "externalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
    "internalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
    "stationAnnouncement"   : "The Yard", # Station Announcement from the Train Controller
    #"isAtStation"           : False
}

# def parseJson():
#     #TODO: Parse to ArduinoJsonFormat
#     json.dumps()

while True:
    msg=json.dumps(trainControllerToTrainModel)
    print(f'Sending {msg} to {ip}:{port}    Counter:{counter}')
    sock = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)
    sock.sendto(msg.encode('utf-8'), (ip, port))
    counter+=1
    time.sleep(0.1)
    trainControllerToTrainModel["power"]=counter;
