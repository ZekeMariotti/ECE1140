# Train Model Test UI

# Importing all required modules
import sys
from sys import argv
import os
import json
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from TrainModelMainUI import TrainModelUI
from TrainModelSignals import *


# Class for the Train Model Test UI
class TrainModelTestUI(QWidget):

    testDataInputs = {
        "rtc"                   : "",
        "authority"             : 0,
        "commandedSpeed"        : 0.0,
        "passengersEntering"    : 0,
        "speedLimit"            : 0.0,
        "undergroundState"      : False,
        "beacon"                : [True, "", 0],
        "id"                    : 0,
        "power"                 : 0.0,
        "leftDoorCommand"       : False,
        "rightDoorCommand"      : False,
        "serviceBrakeCommand"   : False,
        "emergencyBrakeCommand" : False,
        "externalLightCommand"  : False,
        "internalLightCommand"  : False,
        "stationAnnouncement"   : "",
        "switch"                : True,
        "switchState"           : 0
    }

    testDataOutputs = {
        "id"                   : 0,
        "commandedSpeed"       : 0.0,
        "currentSpeed"         : 0.0,
        "authority"            : 0,
        "inputTime"            : "",
        "undergroundState"     : False,
        "speedLimit"           : 0.0,
        "temperature"          : 0.0,
        "engineState"          : True,
        "stationState"         : False,
        "stationName"          : "",
        "platformSide"         : 0,
        "externalLightsState"  : False,
        "internalLightsState"  : False,
        "leftDoorState"        : False,
        "rightDoorState"       : False,
        "serviceBrakeState"    : False,
        "emergencyBrakeState"  : False,
        "serviceBrakeStatus"   : True,
        "engineStatus"         : True,
        "communicationsStatus" : True,
        "currBlock"            : 0,
        "prevBlock"            : 0,
        "passengersOff"        : 0
    }

    # Dictionary for inputs from the Train Controller JSON File
    trainControllerToTrainModel = {
        "id"                    : 0,         # ID number for the train
        "power"                 : 0.0,       # Power input from the Train Controller
        "leftDoorCommand"       : False,     # Left Door Command from the Train Controller, False if closed, True if open
        "rightDoorCommand"      : False,     # Right Door Command from the Train Controller, False if closed, True if open
        "serviceBrakeCommand"   : False,     # Service Brake Command from the Train Controller, True if engaged, False is disengaged
        "emergencyBrakeCommand" : False,     # Emergency Brake Command from the Train Controller, True if engaged, False is isengaged
        "externalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
        "InternalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
        "stationAnnouncement"   : "The Yard" # Station Announcement from the Train Controller
    }

    # Dictionary for outputs to the Train Controller
    trainModelToTrainController = {
        "id"                    : 0,                                   # ID number for the train
        "commandedSpeed"        : 0.0,                                 # Commanded Speed in m/s
        "currentSpeed"          : 0.0,                                 # Current Speed in m/s
        "authority"             : 0,                                   # Authority in Blocks
        "inputTime"             : "2023-02-22T11:00:00.0000000-05:00", # RTC Clock in ISO 8601
        "undergroundState"      : False,                               # Underground State
        "speedLimit"            : 0.0,                                 # Speed Limit in m/s
        "temperature"           : 0.0,                                 # Temperature inside the Train in degrees Fahrenheit
        "engineState"           : True,                                # State of the Engine, True if on, False if off
        "stationState"          : False,                               # Station State, True if at a station, False otherwise
        "stationName"           : "The Yard",                          # Station Name
        "platformSide"          : 0,                                   # Platform Side, 0 if left, 1 if right, 2 if both
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

    # Dictionary for inputs from the Track Model
    trackModelToTrainModel = {
        "rtc"                : "2023-02-22T11:00:00.0000000-05:00",    # Real Time Clock in ISO 8601 Format
        "authority"          : 0,                                      # Authority of the train to be passed to the train controller in blocks
        "commandedSpeed"     : 0.0,                                    # Commanded speed of the train in m/s
        "passengersEntering" : 0,                                      # Number of passengers entering the train
        "speedLimit"         : 0.0,                                    # Speed limit of the current block that the train is on in m/s
        "undergroundState"   : False,                                  # State of whether the train is underground or not
        "beacon"             : [False, "The Yard", 0],                 # Array to store the beacon inputs [Station State, Station Name, Platform Side]
        "switch"             : True,                                   # True if the block the train is currently on is a switch, false otherwise                      
        "switchState"        : 1                                       # 0 if the switch is in a default position, 1 otherwise
    }

    # Dictionary for outputs to the Track Model
    trainModelToTrackModel = {
        "currBlock"     : 0, # Current Block of the train
        "prevBlock"     : 0, # Block the train is exiting
        "passengersOff" : 0  # Passengers getting off of the train
    }

    # Initialize the GUI
    def __init__(self):

        # Initializing the layout of the UI
        super().__init__()
        self.setWindowTitle("Train Model Test UI")
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFixedSize(600, 750)
        orientation = self.frameGeometry()
        self.move(orientation.topLeft())

        # Setting up all the inputs

        # Adding the Track Model Label
        trackModelLabel = QLabel("Track Model Inputs")
        layout.addWidget(trackModelLabel, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Add the Real Time Clock Input
        realTimeClockLabel = QLabel("Real Time Clock")
        layout.addWidget(realTimeClockLabel, 1, 0)
        self.realTimeClockInput = QLineEdit()
        self.realTimeClockInput.editingFinished.connect(self.getRealTimeClockInput)
        layout.addWidget(self.realTimeClockInput, 1, 1)

        # Add the Authority Input
        authorityLabel = QLabel("Authority")
        layout.addWidget(authorityLabel, 2, 0)
        self.authorityInput = QLineEdit()
        self.authorityInput.editingFinished.connect(self.getAuthorityInput)
        layout.addWidget(self.authorityInput, 2, 1)

        # Add the Commanded Speed Input
        commandedSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(commandedSpeedLabel, 3, 0)
        self.commandedSpeedInput = QLineEdit()
        self.commandedSpeedInput.editingFinished.connect(self.getCommandedSpeedInput)
        layout.addWidget(self.commandedSpeedInput, 3, 1)

        # Add the Passengers Entering Input
        passengersEnteringLabel = QLabel("Passengers Entering")
        layout.addWidget(passengersEnteringLabel, 4, 0)
        self.passengersEnteringInput = QLineEdit()
        self.passengersEnteringInput.editingFinished.connect(self.getPassengersEnteringInput)
        layout.addWidget(self.passengersEnteringInput, 4, 1)

        # Add the Speed Limit Input
        speedLimitLabel = QLabel("Speed Limit")
        layout.addWidget(speedLimitLabel, 5, 0)
        self.speedLimitInput = QLineEdit()
        self.speedLimitInput.editingFinished.connect(self.getSpeedLimitInput)
        layout.addWidget(self.speedLimitInput, 5, 1)

        # Add the Underground State Input
        undergroundStateLabel = QLabel("Underground State")
        layout.addWidget(undergroundStateLabel, 6, 0)
        self.undergroundStateInput = QComboBox()
        self.undergroundStateInput.addItems(["False", "True"])
        self.undergroundStateInput.currentIndexChanged.connect(self.getUndergroundStateInput)
        layout.addWidget(self.undergroundStateInput, 6, 1)

        # Add the Beacon Inputs [Station State, Next Station Name, Platform Side]
        beaconLabel = QLabel("Beacon Inputs")
        layout.addWidget(beaconLabel, 7, 0)
        beaconLabel2 = QLabel("[Station State, Next Station Name, Platform Side]")
        beaconLabel2.setWordWrap(True)
        layout.addWidget(beaconLabel2, 7, 1)

        # Station State Beacon Switch
        stationStateLabel = QLabel("Station State")
        layout.addWidget(stationStateLabel, 8, 0)
        self.stationStateInput = QComboBox()
        self.stationStateInput.addItems(["False", "True"])
        self.stationStateInput.currentIndexChanged.connect(self.getStationStateInput)
        layout.addWidget(self.stationStateInput, 8, 1)

        # Next Station Name Beacon Input
        nextStationLabel = QLabel("Next Station Name")
        layout.addWidget(nextStationLabel, 9, 0)
        self.nextStationInput = QLineEdit()
        self.nextStationInput.editingFinished.connect(self.getNextStationInput)
        layout.addWidget(self.nextStationInput, 9, 1)

        # Platform Side Beacon Selector
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 10, 0)
        self.platformSideInput = QComboBox()
        self.platformSideInput.addItems(["Left", "Right", "Both"])
        self.platformSideInput.currentIndexChanged.connect(self.getPlatformSideInput)
        layout.addWidget(self.platformSideInput, 10, 1)

        # Add the Switch Input
        switchLabel = QLabel("Switch")
        layout.addWidget(switchLabel, 11, 0)
        self.switchInput = QComboBox()
        self.switchInput.addItems(["False", "True"])
        self.switchInput.currentIndexChanged.connect(self.getSwitchInput)
        layout.addWidget(self.switchInput, 11, 1)

        # Add the Switch State Input
        switchStateLabel = QLabel("Switch State")
        layout.addWidget(switchStateLabel, 12, 0)
        self.switchStateInput = QComboBox()
        self.switchStateInput.addItems(["0", "1"])
        self.switchStateInput.currentIndexChanged.connect(self.getSwitchStateInput)
        layout.addWidget(self.switchStateInput, 12, 1)

        # Adding the Train Controller Label
        trainControllerLabel = QLabel("Train Controller Inputs")
        layout.addWidget(trainControllerLabel, 13, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Train ID Input
        idLabel = QLabel("Train ID")
        layout.addWidget(idLabel, 14, 0)
        self.idLabelInput = QLineEdit()
        self.idLabelInput.editingFinished.connect(self.getIDLabelInput)
        layout.addWidget(self.idLabelInput, 14, 1)

        # Add the Power Input
        powerLabel = QLabel("Power Input")
        layout.addWidget(powerLabel, 15, 0)
        self.powerInput = QLineEdit()
        self.powerInput.editingFinished.connect(self.getPowerInput)
        layout.addWidget(self.powerInput, 15, 1)

        # Add the Left Door Switch
        leftDoorLabel = QLabel("Left Doors")
        layout.addWidget(leftDoorLabel, 16, 0)
        self.leftDoorInput = QComboBox()
        self.leftDoorInput.addItems(["Closed", "Open"])
        self.leftDoorInput.currentIndexChanged.connect(self.getLeftDoorInput)
        layout.addWidget(self.leftDoorInput, 16, 1)

        # Add the Right Door Switch
        rightDoorLabel = QLabel("Right Doors")
        layout.addWidget(rightDoorLabel, 17, 0)
        self.rightDoorInput = QComboBox()
        self.rightDoorInput.addItems(["Closed", "Open"])
        self.rightDoorInput.currentIndexChanged.connect(self.getRightDoorInput)
        layout.addWidget(self.rightDoorInput, 17, 1)

        # Add the Service Brake Switch
        serviceBrakeLabel = QLabel("Service Brake")
        layout.addWidget(serviceBrakeLabel, 18, 0)
        self.serviceBrakeInput = QComboBox()
        self.serviceBrakeInput.addItems(["Disengaged", "Engaged"])
        self.serviceBrakeInput.currentIndexChanged.connect(self.getServiceBrakeInput)
        layout.addWidget(self.serviceBrakeInput, 18, 1)

        # Add the Emergency Brake Switch
        emergencyBrakeLabel = QLabel("Emergency Brake")
        layout.addWidget(emergencyBrakeLabel, 19, 0)
        self.emergencyBrakeInput = QComboBox()
        self.emergencyBrakeInput.addItems(["Disengaged", "Engaged"])
        self.emergencyBrakeInput.currentIndexChanged.connect(self.getEmergencyBrakeInput)
        layout.addWidget(self.emergencyBrakeInput, 19, 1)

        # Add the External Lights Switch
        externalLightLabel = QLabel("External Lights")
        layout.addWidget(externalLightLabel, 20, 0)
        self.externalLightInput = QComboBox()
        self.externalLightInput.addItems(["Off", "On"])
        self.externalLightInput.currentIndexChanged.connect(self.getExternalLightInput)
        layout.addWidget(self.externalLightInput, 20, 1)

        # Add the Internal Lights Switch
        internalLightLabel = QLabel("Internal Lights")
        layout.addWidget(internalLightLabel, 21, 0)
        self.internalLightInput = QComboBox()
        self.internalLightInput.addItems(["Off", "On"])
        self.internalLightInput.currentIndexChanged.connect(self.getInternalLightInput)
        layout.addWidget(self.internalLightInput, 21, 1)

        # Add the Station Announcement Input
        stationLabel = QLabel("Station Announcement")
        layout.addWidget(stationLabel, 22, 0)
        self.stationInput = QLineEdit()
        self.stationInput.editingFinished.connect(self.getStationInput)
        layout.addWidget(self.stationInput, 22, 1)


        # Setting up all the outputs

        # Adding the Track Model Label
        trackModelOutputLabel = QLabel("Track Model Outputs")
        layout.addWidget(trackModelOutputLabel, 0, 2, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Adding the Current Block Output
        currBlockLabel = QLabel("Current Block")
        layout.addWidget(currBlockLabel, 1, 2)
        self.currBlockOutput = QLineEdit()
        self.currBlockOutput.setReadOnly(True)
        self.currBlockOutput.setText("0")
        layout.addWidget(self.currBlockOutput, 1, 3)

        # Adding the Previous Block Output
        prevBlockLabel = QLabel("Previous Block")
        layout.addWidget(prevBlockLabel, 2, 2)
        self.prevBlockOutput = QLineEdit()
        self.prevBlockOutput.setReadOnly(True)
        self.prevBlockOutput.setText("0")
        layout.addWidget(self.prevBlockOutput, 2, 3)

        # Adding the Passengers Exiting
        passengersExitingLabel = QLabel("Passengers Exiting")
        layout.addWidget(passengersExitingLabel, 3, 2)
        self.passengersExitingOutput = QLineEdit()
        self.passengersExitingOutput.setReadOnly(True)
        self.passengersExitingOutput.setText("0")
        layout.addWidget(self.passengersExitingOutput, 3, 3)

        # Adding the Train Controller Label
        trainControllerOutputLabel = QLabel("Train Controller Outputs")
        layout.addWidget(trainControllerOutputLabel, 4, 2, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Adding the Train ID Output
        idOutputLabel = QLabel("Train ID")
        layout.addWidget(idOutputLabel, 5, 2)
        self.idOutput = QLineEdit()
        self.idOutput.setReadOnly(True)
        self.idOutput.setText("0")
        layout.addWidget(self.idOutput, 5, 3)

        # Adding the Commanded Speed
        commandedSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(commandedSpeedLabel, 6, 2)
        self.commandedSpeedOutput = QLineEdit()
        self.commandedSpeedOutput.setReadOnly(True)
        self.commandedSpeedOutput.setText("0 m/s")
        layout.addWidget(self.commandedSpeedOutput, 6, 3)

        # Adding the Velocity
        velocityLabel = QLabel("Current Speed")
        layout.addWidget(velocityLabel, 7, 2)
        self.velocityOutput = QLineEdit()
        self.velocityOutput.setReadOnly(True)
        self.velocityOutput.setText("0 m/s")
        layout.addWidget(self.velocityOutput, 7, 3)

        # Adding the Authority
        authorityLabel = QLabel("Authority")
        layout.addWidget(authorityLabel, 8, 2)
        self.authorityOutput = QLineEdit()
        self.authorityOutput.setReadOnly(True)
        self.authorityOutput.setText("0 Blocks")
        layout.addWidget(self.authorityOutput, 8, 3)

        # Adding the Real Time Clock
        realTimeClockLabel = QLabel("Real Time Clock")
        layout.addWidget(realTimeClockLabel, 9, 2)
        self.realTimeClockOutput = QLineEdit()
        self.realTimeClockOutput.setReadOnly(True)
        self.realTimeClockOutput.setText("12:00:00 am")
        layout.addWidget(self.realTimeClockOutput, 9, 3)

        # Adding the Underground State
        undergroundStateLabel = QLabel("Underground State")
        layout.addWidget(undergroundStateLabel, 10, 2)
        self.undergroundStateOutput = QLineEdit()
        self.undergroundStateOutput.setReadOnly(True)
        self.undergroundStateOutput.setText("0")
        layout.addWidget(self.undergroundStateOutput, 10, 3)

        # Adding the Speed Limit
        speedLimitLabel = QLabel("Speed Limit")
        layout.addWidget(speedLimitLabel, 11, 2)
        self.speedLimitOutput = QLineEdit()
        self.speedLimitOutput.setReadOnly(True)
        self.speedLimitOutput.setText("0 km/hr")
        layout.addWidget(self.speedLimitOutput, 11, 3)

        # ADD THE TEMPERATURE OUTPUT
        temperatureLabel = QLabel("Temperature")
        layout.addWidget(temperatureLabel, 12, 2)
        self.temperatureOutput = QLineEdit()
        self.temperatureOutput.setReadOnly(True)
        self.temperatureOutput.setText("68 F")
        layout.addWidget(self.temperatureOutput, 12, 3)

        # ADD THE ENGINE STATE OUTPUT
        engineStateLabel = QLabel("Engine State")
        layout.addWidget(engineStateLabel, 13, 2)
        self.engineStateOutput = QLineEdit()
        self.engineStateOutput.setReadOnly(True)
        self.engineStateOutput.setText("Operational")
        layout.addWidget(self.engineStateOutput, 13, 3)

        # Adding the Station State
        stationStateLabel = QLabel("Station State")
        layout.addWidget(stationStateLabel, 14, 2)
        self.stationStateOutput = QLineEdit()
        self.stationStateOutput.setReadOnly(True)
        self.stationStateOutput.setText("0")
        layout.addWidget(self.stationStateOutput, 14, 3)

        # Adding the Next Station Name
        nextStationLabel = QLabel("Station Name")
        layout.addWidget(nextStationLabel, 15, 2)
        self.nextStationOutput = QLineEdit()
        self.nextStationOutput.setReadOnly(True)
        self.nextStationOutput.setText("")
        layout.addWidget(self.nextStationOutput, 15, 3)

        # Adding the Platform Side
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 16, 2)
        self.platformSideOutput = QLineEdit()
        self.platformSideOutput.setReadOnly(True)
        self.platformSideOutput.setText("Left")
        layout.addWidget(self.platformSideOutput, 16, 3)

        # Adding the External Light State
        externalLightLabel = QLabel("External Lights")
        layout.addWidget(externalLightLabel, 17, 2)
        self.externalLightOutput = QLineEdit()
        self.externalLightOutput.setReadOnly(True)
        self.externalLightOutput.setText("Off")
        layout.addWidget(self.externalLightOutput, 17, 3)

        # Adding the Internal Light State
        internalLightLabel = QLabel("Internal Lights")
        layout.addWidget(internalLightLabel, 18, 2)
        self.internalLightOutput = QLineEdit()
        self.internalLightOutput.setReadOnly(True)
        self.internalLightOutput.setText("Off")
        layout.addWidget(self.internalLightOutput, 18, 3)

        # Adding the Left Door State
        leftDoorLabel = QLabel("Left Doors")
        layout.addWidget(leftDoorLabel, 19, 2)
        self.leftDoorOutput = QLineEdit()
        self.leftDoorOutput.setReadOnly(True)
        self.leftDoorOutput.setText("Closed")
        layout.addWidget(self.leftDoorOutput, 19, 3)

        # Adding the Right Door State
        rightDoorLabel = QLabel("Right Doors")
        layout.addWidget(rightDoorLabel, 20, 2)
        self.rightDoorOutput = QLineEdit()
        self.rightDoorOutput.setReadOnly(True)
        self.rightDoorOutput.setText("Closed")
        layout.addWidget(self.rightDoorOutput, 20, 3)

        # Adding the Service Brake State
        serviceBrakeLabel = QLabel("Service Brake")
        layout.addWidget(serviceBrakeLabel, 21, 2)
        self.serviceBrakeOutput = QLineEdit()
        self.serviceBrakeOutput.setReadOnly(True)
        self.serviceBrakeOutput.setText("Disengaged")
        layout.addWidget(self.serviceBrakeOutput, 21, 3)

        # Adding the Emergency Brake State
        emergencyBrakeLabel = QLabel("Emergency Brake")
        layout.addWidget(emergencyBrakeLabel, 22, 2)
        self.emergencyBrakeOutput = QLineEdit()
        self.emergencyBrakeOutput.setReadOnly(True)
        self.emergencyBrakeOutput.setText("Disengaged")
        layout.addWidget(self.emergencyBrakeOutput, 22, 3)

        # ADD FAILURE STATUS
        brakeStatusLabel = QLabel("Service Brake Status")
        layout.addWidget(brakeStatusLabel, 23, 2)
        self.brakeStatusOutput = QLineEdit()
        self.brakeStatusOutput.setReadOnly(True)
        self.brakeStatusOutput.setText("Functional")
        layout.addWidget(self.brakeStatusOutput, 23, 3)

        engineStatusLabel = QLabel("Engine Status")
        layout.addWidget(engineStatusLabel, 24, 2)
        self.engineStatusOutput = QLineEdit()
        self.engineStatusOutput.setReadOnly(True)
        self.engineStatusOutput.setText("Functional")
        layout.addWidget(self.engineStatusOutput, 24, 3)

        commStatusLabel = QLabel("Communications Status")
        layout.addWidget(commStatusLabel, 25, 2)
        self.commStatusOutput = QLineEdit()
        self.commStatusOutput.setReadOnly(True)
        self.commStatusOutput.setText("Functional")
        layout.addWidget(self.commStatusOutput, 25, 3)

        # UPDATE BUTTON FOR TESTING TO BE REMOVED
        updateButton = QPushButton("Update Values")
        updateButton.pressed.connect(self.updateOutputsBoth)
        layout.addWidget(updateButton, 26, 0, 1, 4)

    # Function to read the outputs from the Train Model to Train Controller
    def readTrainModelToTrackModel(self):
        with open(os.path.join(sys.path[0], "TrainModelToTrackModel.json"), "r") as filename:
            self.trainModelToTrackModel = json.loads(filename.read())
        self.testDataOutputs["currBlock"]     = self.trainModelToTrackModel["currBlock"]
        self.testDataOutputs["prevBlock"]     = self.trainModelToTrackModel["prevBlock"]
        self.testDataOutputs["passengersOff"] = self.trainModelToTrackModel["passengersOff"]

    # Function to read the outputs from the Train Model to the Train Controller
    def readTrainModelToTrainController(self):
        with open(os.path.join(sys.path[0], "TrainModelToTrainControllerSW.json"), "r") as filename:
            self.trainModelToTrainController = json.loads(filename.read())
        self.testDataOutputs["id"]                   = self.trainModelToTrainController["id"]
        self.testDataOutputs["commandedSpeed"]       = self.trainModelToTrainController["commandedSpeed"]
        self.testDataOutputs["currentSpeed"]         = self.trainModelToTrainController["currentSpeed"]
        self.testDataOutputs["authority"]            = self.trainModelToTrainController["authority"]
        self.testDataOutputs["inputTime"]            = self.trainModelToTrainController["inputTime"]
        self.testDataOutputs["undergroundState"]     = self.trainModelToTrainController["undergroundState"]
        self.testDataOutputs["speedLimit"]           = self.trainModelToTrainController["speedLimit"]
        self.testDataOutputs["temperature"]          = self.trainModelToTrainController["temperature"]
        self.testDataOutputs["engineState"]          = self.trainModelToTrainController["engineState"]
        self.testDataOutputs["stationState"]         = self.trainModelToTrainController["stationState"]
        self.testDataOutputs["stationName"]          = self.trainModelToTrainController["stationName"]
        self.testDataOutputs["platformSide"]         = self.trainModelToTrainController["platformSide"]
        self.testDataOutputs["externalLightsState"]  = self.trainModelToTrainController["externalLightsState"]
        self.testDataOutputs["internalLightsState"]  = self.trainModelToTrainController["internalLightsState"]
        self.testDataOutputs["leftDoorState"]        = self.trainModelToTrainController["leftDoorState"]
        self.testDataOutputs["rightDoorState"]       = self.trainModelToTrainController["rightDoorState"]
        self.testDataOutputs["serviceBrakeState"]    = self.trainModelToTrainController["serviceBrakeState"]
        self.testDataOutputs["emergencyBrakeState"]  = self.trainModelToTrainController["emergencyBrakeState"]
        self.testDataOutputs["serviceBrakeStatus"]   = self.trainModelToTrainController["serviceBrakeStatus"]
        self.testDataOutputs["engineStatus"]         = self.trainModelToTrainController["engineStatus"]
        self.testDataOutputs["communicationsStatus"] = self.trainModelToTrainController["communicationsStatus"]

    # Function to write inputs from the Track Model to the Train Model
    def writeTrackModelToTrainModel(self):
        self.trackModelToTrainModel["rtc"]                = self.testDataInputs["rtc"]
        self.trackModelToTrainModel["authority"]          = self.testDataInputs["authority"]
        self.trackModelToTrainModel["commandedSpeed"]     = self.testDataInputs["commandedSpeed"]
        self.trackModelToTrainModel["passengersEntering"] = self.testDataInputs["passengersEntering"]
        self.trackModelToTrainModel["speedLimit"]         = self.testDataInputs["speedLimit"]
        self.trackModelToTrainModel["undergroundState"]   = self.testDataInputs["undergroundState"]
        self.trackModelToTrainModel["beacon"]             = self.testDataInputs["beacon"]
        self.trackModelToTrainModel["switch"]             = self.testDataInputs["switch"]
        self.trackModelToTrainModel["switchState"]        = self.testDataInputs["switchState"]
        with open(os.path.join(sys.path[0], "TrackModelToTrainModel.json"), "w") as filename:
            (json.dump(self.trackModelToTrainModel, filename, indent=4))

    # Function to write inputs from the Train Controller to the Train Model
    def writeTrainControllerToTrainModel(self):
        self.trainControllerToTrainModel["id"]                    = self.testDataInputs["id"]
        self.trainControllerToTrainModel["power"]                 = self.testDataInputs["power"]
        self.trainControllerToTrainModel["leftDoorCommand"]       = self.testDataInputs["leftDoorCommand"]
        self.trainControllerToTrainModel["rightDoorCommand"]      = self.testDataInputs["rightDoorCommand"]
        self.trainControllerToTrainModel["serviceBrakeCommand"]   = self.testDataInputs["serviceBrakeCommand"]
        self.trainControllerToTrainModel["emergencyBrakeCommand"] = self.testDataInputs["emergencyBrakeCommand"]
        self.trainControllerToTrainModel["externalLightCommand"]  = self.testDataInputs["externalLightCommand"]
        self.trainControllerToTrainModel["internalLightCommand"]  = self.testDataInputs["internalLightCommand"]
        self.trainControllerToTrainModel["stationAnnouncement"]   = self.testDataInputs["stationAnnouncement"]
        with open(os.path.join(sys.path[0], "TrainControllerSWToTrainModel.json"), "w") as filename:
            (json.dump(self.trainControllerToTrainModel, filename, indent=4))

    def getSwitchInput(self, index):
        self.testDataInputs["switch"] = bool(index)
    
    def getSwitchStateInput(self, index):
        self.testDataInputs["switchState"] = index

    def getIDLabelInput(self):
        self.testDataInputs["id"] = int(self.idLabelInput.text())

    # Gets the Power input from the UI
    def getPowerInput(self):
        self.testDataInputs["power"] = float(self.powerInput.text())

    # Gets the Service Brake state from the UI
    def getServiceBrakeInput(self, index):
        self.testDataInputs["serviceBrakeCommand"] = bool(index)

    # Gets the Emergency Brake state from the UI
    def getEmergencyBrakeInput(self, index):
        self.testDataInputs["emergencyBrakeCommand"] = bool(index)

    # Gets the Left Door state from the UI
    def getLeftDoorInput(self, index):
        self.testDataInputs["leftDoorCommand"] = bool(index)

    # Gets the Right Door state from the UI
    def getRightDoorInput(self, index):
        self.testDataInputs["rightDoorCommand"] = bool(index)

    # Gets the External Light state from the UI
    def getExternalLightInput(self, index):
        self.testDataInputs["externalLightCommand"] = bool(index)

    # Gets the Internal Light state from the UI
    def getInternalLightInput(self, index):
        self.testDataInputs["internalLightCommand"] = bool(index)

    # Gets the Station Name input from the UI
    def getStationInput(self):
        self.testDataInputs["stationAnnouncement"] = self.stationInput.text()

    # Gets the Real Time Clock state from the UI
    def getRealTimeClockInput(self):
        self.testDataInputs["rtc"] = self.realTimeClockInput.text()

    # Gets the Authority input from the UI
    def getAuthorityInput(self):
        self.testDataInputs["authority"] = int(self.authorityInput.text())

    # Gets the commanded speed from the UI
    def getCommandedSpeedInput(self):
        self.testDataInputs["commandedSpeed"] = float(self.commandedSpeedInput.text())

    # Gets the number of passengers entering the train from the UI
    def getPassengersEnteringInput(self):
        self.testDataInputs["passengersEntering"] = int(self.passengersEnteringInput.text())
        
    # Gets the Speed Limit from the UI    
    def getSpeedLimitInput(self):
        self.testDataInputs["speedLimit"] = int(self.speedLimitInput.text())

    # Gets the Underground state from the UI
    def getUndergroundStateInput(self, index):
        self.testDataInputs["undergroundState"] = bool(index)

    # Gets the Station state from the UI
    def getStationStateInput(self, index):
        self.testDataInputs["beacon"][0] = bool(index)

    # Gets the Next Station input from the UI
    def getNextStationInput(self):
        self.testDataInputs["beacon"][1] = self.nextStationInput.text()
    
    # Gets the Platform Side input from the UI
    def getPlatformSideInput(self, index):
        self.testDataInputs["beacon"][2] = index

    # Updates all functions when the button is pressed
    def updateOutputsBoth(self):
        self.writeTrackModelToTrainModel()
        self.writeTrainControllerToTrainModel()
        trainSignals.updateOutputs.emit()
        self.readTrainModelToTrackModel()
        self.readTrainModelToTrainController()

        self.currBlockOutput.setText("Block " + str(self.testDataOutputs["currBlock"]))
        self.prevBlockOutput.setText("Block " + str(self.testDataOutputs["prevBlock"]))
        self.passengersExitingOutput.setText(str(self.testDataOutputs["passengersOff"]))
        self.idOutput.setText(str(self.testDataOutputs["id"]))
        self.commandedSpeedOutput.setText(str(self.testDataOutputs["commandedSpeed"]) + " m/s")
        self.velocityOutput.setText(str(round(self.testDataOutputs["currentSpeed"], 2)) + " m/s")
        self.authorityOutput.setText(str(self.testDataOutputs["authority"]) + " Blocks")
        self.realTimeClockOutput.setText(self.testDataOutputs["inputTime"])
        self.undergroundStateOutput.setText(str(bool(self.testDataOutputs["undergroundState"])))
        self.speedLimitOutput.setText(str(self.testDataOutputs["speedLimit"]) + " km/h")
        self.temperatureOutput.setText(str(self.testDataOutputs["temperature"]) + " F")
        self.engineStateOutput.setText(str(self.testDataOutputs["engineState"]))
        self.stationStateOutput.setText(str(self.testDataOutputs["stationState"]))
        self.nextStationOutput.setText(self.testDataOutputs["stationName"])
        self.platformSideOutput.setText(str(self.testDataOutputs["platformSide"]))


        outputText = "On" if (self.testDataOutputs["externalLightsState"] == 1) else "Off"
        self.externalLightOutput.setText(outputText)
        outputText = "On" if (self.testDataOutputs["internalLightsState"] == 1) else "Off"
        self.internalLightOutput.setText(outputText)

        outputText = "Open" if (self.testDataOutputs["leftDoorState"] == 1) else "Closed"
        self.leftDoorOutput.setText(outputText)
        outputText = "Open" if (self.testDataOutputs["rightDoorState"] == 1) else "Closed"
        self.rightDoorOutput.setText(outputText)

        if self.testDataOutputs["serviceBrakeStatus"]:
            outputText = "Engaged" if (self.testDataOutputs["serviceBrakeState"] == 1) else "Disengaged"
            self.serviceBrakeOutput.setText(outputText)
        else:
            self.serviceBrakeOutput.setText("Disengaged")
        outputText = "Engaged" if (self.testDataOutputs["emergencyBrakeState"] == 1) else "Disengaged"
        self.emergencyBrakeOutput.setText(outputText)

        self.brakeStatusOutput.setText(str(self.testDataOutputs["serviceBrakeStatus"]))
        self.engineStatusOutput.setText(str(self.testDataOutputs["engineStatus"]))
        self.commStatusOutput.setText(str(self.testDataOutputs["communicationsStatus"]))

def main():
    app = QApplication(argv)
    testUI = TrainModelTestUI()
    testUI.show()
    mainUI = TrainModelUI()
    mainUI.show()
    app.exec()

if __name__ == "__main__":
    main()
