import socket
import time
ip = "127.0.0.1"
port = 27000
msg = b"hello world"
counter = 0

# # Dictionary for outputs to the Train Controller
# trainModelToTrainController = {
#     "id"                    : 0,                                   # ID number for the train
#     "commandedSpeed"        : 0.0,                                 # Commanded Speed in m/s
#     "currentSpeed"          : 0.0,                                 # Current Speed in m/s
#     "authority"             : 0,                                   # Authority in Blocks
#     "inputTime"             : "2023-02-22T11:00:00.0000000-05:00", # RTC Clock in ISO 8601
#     "undergroundState"      : False,                               # Underground State
#     "speedLimit"            : 0.0,                                 # Speed Limit in m/s
#     "temperature"           : 0.0,                                 # Temperature inside the Train in degrees Fahrenheit
#     "engineState"           : True,                                # State of the Engine, True if on, False if off
#     "stationName"           : "The Yard",                          # Station Name, from the beacon
#     "platformSide"          : 0,                                   # Platform Side, 0 if left, 1 if right, 2 if both, from the beacon
#     "nextStationName"       : "",                                  # Name of the next station, from the beacon
#     "isBeacon"              : False,                               # Whether or not a beacon is active
#     "externalLightsState"   : False,                               # State of the External Lights, True if on, False if off
#     "internalLightsState"   : False,                               # State of the Internal Lights, True if on, False if off
#     "leftDoorState"         : False,                               # State of the Left Doors, True if open, False if closed
#     "rightDoorState"        : False,                               # State of the Right Doors, True if open, False if closed
#     "serviceBrakeState"     : False,                               # State of the Service Brake, True if engaged, False if disengaged
#     "emergencyBrakeState"   : False,                               # State of the Emergency Brake, True if engaged, Flase if disengaged
#     "serviceBrakeStatus"    : True,                                # Status of the Service Brake, True if operational, False if offline
#     "engineStatus"          : True,                                # Status of the Engine, True if operational, False if offline
#     "communicationsStatus"  : True                                 # Status of the Communications with the Track, True if operational, False if offline
# }

# def readJsonFromFile():
#     with open(os.path.join(sys.path[0], "TrainControllerSWToTrainModel.json"), "r") as filename:
#             trainModelToTrainController = json.loads(filename.read())

# def parseJson():
#     #TODO: Parse to ArduinoJsonFormat
#     json.dumps()

while True:
    print(f'Sending {msg} to {ip}:{port}    Counter:{counter}')
    sock = socket.socket(socket.AF_INET,
                        socket.SOCK_DGRAM)
    sock.sendto(msg, (ip, port))
    counter+=1
    # time.sleep(1)
