# Train Model Test UI

# Importing all required modules
import sys
from datetime import *
from sys import argv
import os
import json
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from TrainModelMainUI import TrainModelUI
from TrainModelSignals import *
from TMTCSignals import *
from TMTkMSignals import *


# Class for the Train Model Test UI
class TrainModelTestUI(QWidget):

    testDataInputs = {
        "rtc"                   : "2023-02-22T11:00:00.0000000-05:00",
        "authority"             : 0,
        "commandedSpeed"        : 0.0,
        "passengersEntering"    : 0,
        "undergroundState"      : False,
        "beacon"                : ["", 0, "", False],
        "id"                    : 0,
        "power"                 : 0.0,
        "leftDoorCommand"       : False,
        "rightDoorCommand"      : False,
        "serviceBrakeCommand"   : False,
        "emergencyBrakeCommand" : False,
        "externalLightCommand"  : False,
        "internalLightCommand"  : False,
        "stationAnnouncement"   : "The Yard",
        "switch"                : False,
        "switchState"           : 0,
        "blockLength"           : 100.0,
        "elevation"             : 0
    }

    testDataOutputs = {
        #"id"                   : 0,
        "commandedSpeed"       : 0.0,
        "currentSpeed"         : 0.0,
        "authority"            : 0,
        "inputTime"            : "",
        "undergroundState"     : False,
        "temperature"          : 0.0,
        "stationName"          : "",
        "platformSide"         : 0,
        "nextStationName"      : "",
        "isBeacon"             : False,
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

    # Dictionary for inputs from the Train Controller JSON File (WAS USING JSON, SCRAPPED)
    #trainControllerToTrainModel = {
    #    "power"                 : 0.0,       # Power input from the Train Controller
    #    "leftDoorCommand"       : False,     # Left Door Command from the Train Controller, False if closed, True if open
    #    "rightDoorCommand"      : False,     # Right Door Command from the Train Controller, False if closed, True if open
    #    "serviceBrakeCommand"   : False,     # Service Brake Command from the Train Controller, True if engaged, False is disengaged
    #    "emergencyBrakeCommand" : False,     # Emergency Brake Command from the Train Controller, True if engaged, False is isengaged
    #    "externalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
    #    "InternalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
    #    "stationAnnouncement"   : "The Yard" # Station Announcement from the Train Controller
    #}

    # Dictionary for outputs to the Train Controller (WAS USING JSON, SCRAPPED)
    #trainModelToTrainController = {
    #    "commandedSpeed"        : 0.0,                                 # Commanded Speed in m/s
    #    "currentSpeed"          : 0.0,                                 # Current Speed in m/s
    #    "authority"             : 0,                                   # Authority in Blocks
    #    "inputTime"             : "2023-02-22T11:00:00.0000000-05:00", # RTC Clock in ISO 8601
    #    "undergroundState"      : False,                               # Underground State
    #    "temperature"           : 0.0,                                 # Temperature inside the Train in degrees Fahrenheit
    #    "stationName"           : "The Yard",                          # Station Name, from the beacon
    #    "platformSide"          : 0,                                   # Platform Side, 0 if left, 1 if right, 2 if both, from the beacon
    #    "nextStationName"       : "",                                  # Name of the next station, from the beacon
    #    "isBeacon"              : False,                               # Whether or not a beacon is active
    #    "externalLightsState"   : False,                               # State of the External Lights, True if on, False if off
    #    "internalLightsState"   : False,                               # State of the Internal Lights, True if on, False if off
    #    "leftDoorState"         : False,                               # State of the Left Doors, True if open, False if closed
    #    "rightDoorState"        : False,                               # State of the Right Doors, True if open, False if closed
    #    "serviceBrakeState"     : False,                               # State of the Service Brake, True if engaged, False if disengaged
    #    "emergencyBrakeState"   : False,                               # State of the Emergency Brake, True if engaged, Flase if disengaged
    #    "serviceBrakeStatus"    : True,                                # Status of the Service Brake, True if operational, False if offline
    #    "engineStatus"          : True,                                # Status of the Engine, True if operational, False if offline
    #    "communicationsStatus"  : True                                 # Status of the Communications with the Track, True if operational, False if offline
    #}

    # Dictionary for inputs from the Track Model (WAS USING JSON, SCRAPPED)
    #trackModelToTrainModel = {
    #    "rtc"                : "2023-02-22T11:00:00.0000000-05:00",    # Real Time Clock in ISO 8601 Format
    #    "authority"          : 0,                                      # Authority of the train to be passed to the train controller in blocks
    #    "commandedSpeed"     : 0.0,                                    # Commanded speed of the train in m/s
    #    "passengersEntering" : 0,                                      # Number of passengers entering the train
    #    "undergroundState"   : False,                                  # State of whether the train is underground or not
    #    "beacon"             : ["", 0, "", False],                     # Array to store the beacon inputs [stationName, platformSide, nextStationName, isBeacon]
    #    "switch"             : False,                                  # True if the block the train is currently on is a switch, false otherwise                      
    #    "switchState"        : 0,                                      # 0 if the switch is in a default position, 1 otherwise
    #    "blockLength"        : 100.0,                                  # Length of the current block that the train is on
    #    "elevation"          : 0.0                                     # elevation different of the current block that the train is on
    #}

    # Dictionary for outputs to the Track Model (WAS USING JSON, SCRAPPED)
    #trainModelToTrackModel = {
    #    "currBlock"     : 0, # Current Block of the train
    #    "prevBlock"     : 0, # Block the train is exiting
    #    "passengersOff" : 0  # Passengers getting off of the train
    #}


    def mainThreadSetup(self):
        self.timerThread = QThread()
        self.timerThread.started.connect(self.mainTimerSetup)

    def mainTimerSetup(self):     
        mainTimer = QTimer()
        mainTimer.setInterval(100)
        mainTimer.timeout.connect(self.updateOutputsBoth)
        mainTimer.setParent(self)
        mainTimer.start()
        return mainTimer

    # Initialize the GUI
    def __init__(self):

        # Connecting Signals from the Train Model
        TMTkMSignals.passengersExitingSignal.connect(self.catchPassengersOff)
        TMTkMSignals.currBlockSignal.connect(self.catchCurrBlock)

        TMTCSignals.commandedSpeedSignal.connect(self.catchCommandedSpeed)
        TMTCSignals.currentSpeedSignal.connect(self.catchCurrentSpeed)
        TMTCSignals.authoritySignal.connect(self.catchAuthority)
        TMTCSignals.undergroundSignal.connect(self.catchUndergroundState)
        TMTCSignals.temperatureSignal.connect(self.catchTemperature)
        TMTCSignals.stationNameSignal.connect(self.catchStationName)
        TMTCSignals.platformSideSignal.connect(self.catchPlatformSide)
        TMTCSignals.nextStationNameSignal.connect(self.catchNextStationName)
        TMTCSignals.isBeaconSignal.connect(self.catchIsBeacon)
        TMTCSignals.externalLightsStateSignal.connect(self.catchExternalLights)
        TMTCSignals.internalLightsStateSignal.connect(self.catchInternalLights)
        TMTCSignals.leftDoorStateSignal.connect(self.catchLeftDoors)
        TMTCSignals.rightDoorStateSignal.connect(self.catchRightDoors)
        TMTCSignals.serviceBrakeStateSignal.connect(self.catchServiceBrakeState)
        TMTCSignals.emergencyBrakeStateSignal.connect(self.catchEmergencyBrakeState)
        TMTCSignals.serviceBrakeStatusSignal.connect(self.catchServiceBrakeStatus)
        TMTCSignals.engineStatusSignal.connect(self.catchEngineStatus)
        TMTCSignals.communicationsStatusSignal.connect(self.catchCommStatus)

        # Initializing the layout of the UI
        super().__init__()
        #self.mainTimer = self.mainTimerSetup()
        self.setWindowTitle("Train Model Test UI")
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFixedSize(700, 785)
        orientation = self.frameGeometry()
        self.move(orientation.topLeft())

        # Setting up all the inputs

        # Adding the Track Model Label
        trackModelLabel = QLabel("Track Model Inputs")
        layout.addWidget(trackModelLabel, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Add the Real Time Clock Input
        #realTimeClockLabel = QLabel("Real Time Clock")
        #layout.addWidget(realTimeClockLabel, 1, 0)
        #self.realTimeClockInput = QLineEdit()
        #self.realTimeClockInput.editingFinished.connect(self.getRealTimeClockInput)
        #layout.addWidget(self.realTimeClockInput, 1, 1)

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

        # Add the Underground State Input
        undergroundStateLabel = QLabel("Underground State")
        layout.addWidget(undergroundStateLabel, 5, 0)
        self.undergroundStateInput = QComboBox()
        self.undergroundStateInput.addItems(["False", "True"])
        self.undergroundStateInput.currentIndexChanged.connect(self.getUndergroundStateInput)
        layout.addWidget(self.undergroundStateInput, 5, 1)

        # Add the Beacon Inputs [stationName, platformSide, nextStationName, isBeacon]
        beaconLabel = QLabel("Beacon Inputs")
        layout.addWidget(beaconLabel, 6, 0)
        beaconLabel2 = QLabel("[stationName, platformSide, nextStationName, isBeacon]")
        beaconLabel2.setWordWrap(True)
        layout.addWidget(beaconLabel2, 6, 1)

        # Add the Station Name Beacon Input
        stationNameLabel = QLabel("Station Name")
        layout.addWidget(stationNameLabel, 7, 0)
        self.stationNameInput = QLineEdit()
        self.stationNameInput.editingFinished.connect(self.getStationNameInput)
        layout.addWidget(self.stationNameInput, 7, 1)

        # Platform Side Beacon Selector
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 8, 0)
        self.platformSideInput = QComboBox()
        self.platformSideInput.addItems(["Left", "Right", "Both"])
        self.platformSideInput.currentIndexChanged.connect(self.getPlatformSideInput)
        layout.addWidget(self.platformSideInput, 8, 1)

        # Next Station Name Beacon Input
        nextStationLabel = QLabel("Next Station Name")
        layout.addWidget(nextStationLabel, 9, 0)
        self.nextStationInput = QLineEdit()
        self.nextStationInput.editingFinished.connect(self.getNextStationInput)
        layout.addWidget(self.nextStationInput, 9, 1)

        # is Beacon Input
        isBeaconLabel = QLabel("isBeacon")
        layout.addWidget(isBeaconLabel, 10, 0)
        self.isBeaconInput = QComboBox()
        self.isBeaconInput.addItems(["False", "True"])
        self.isBeaconInput.currentIndexChanged.connect(self.getIsBeaconInput)
        layout.addWidget(self.isBeaconInput, 10, 1)

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

        # Add the Block Length Input
        blockLengthLabel = QLabel("Block Length")
        layout.addWidget(blockLengthLabel, 13, 0)
        self.blockLengthInput = QLineEdit()
        self.blockLengthInput.editingFinished.connect(self.getBlockLengthInput)
        layout.addWidget(self.blockLengthInput, 13, 1)

        # Add the Elevation Length Input
        elevationLabel = QLabel("Elevation")
        layout.addWidget(elevationLabel, 14, 0)
        self.elevationInput = QLineEdit()
        self.elevationInput.editingFinished.connect(self.getElevationInput)
        layout.addWidget(self.elevationInput, 14, 1)


        # Adding the Train Controller Label
        trainControllerLabel = QLabel("Train Controller Inputs")
        layout.addWidget(trainControllerLabel, 15, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Train ID Input
        idLabel = QLabel("Train ID")
        layout.addWidget(idLabel, 16, 0)
        self.idLabelInput = QLineEdit()
        self.idLabelInput.editingFinished.connect(self.getIDLabelInput)
        layout.addWidget(self.idLabelInput, 16, 1)

        # Add the Power Input
        powerLabel = QLabel("Commanded Power Input")
        layout.addWidget(powerLabel, 17, 0)
        self.powerInput = QLineEdit()
        self.powerInput.editingFinished.connect(self.getPowerInput)
        layout.addWidget(self.powerInput, 17, 1)

        # Add the Left Door Switch
        leftDoorLabel = QLabel("Left Doors")
        layout.addWidget(leftDoorLabel, 18, 0)
        self.leftDoorInput = QComboBox()
        self.leftDoorInput.addItems(["Closed", "Open"])
        self.leftDoorInput.currentIndexChanged.connect(self.getLeftDoorInput)
        layout.addWidget(self.leftDoorInput, 18, 1)

        # Add the Right Door Switch
        rightDoorLabel = QLabel("Right Doors")
        layout.addWidget(rightDoorLabel, 19, 0)
        self.rightDoorInput = QComboBox()
        self.rightDoorInput.addItems(["Closed", "Open"])
        self.rightDoorInput.currentIndexChanged.connect(self.getRightDoorInput)
        layout.addWidget(self.rightDoorInput, 19, 1)

        # Add the Service Brake Switch
        serviceBrakeLabel = QLabel("Service Brake")
        layout.addWidget(serviceBrakeLabel, 20, 0)
        self.serviceBrakeInput = QComboBox()
        self.serviceBrakeInput.addItems(["Disengaged", "Engaged"])
        self.serviceBrakeInput.currentIndexChanged.connect(self.getServiceBrakeInput)
        layout.addWidget(self.serviceBrakeInput, 20, 1)

        # Add the Emergency Brake Switch
        emergencyBrakeLabel = QLabel("Emergency Brake")
        layout.addWidget(emergencyBrakeLabel, 21, 0)
        self.emergencyBrakeInput = QComboBox()
        self.emergencyBrakeInput.addItems(["Disengaged", "Engaged"])
        self.emergencyBrakeInput.currentIndexChanged.connect(self.getEmergencyBrakeInput)
        layout.addWidget(self.emergencyBrakeInput, 21, 1)

        # Add the External Lights Switch
        externalLightLabel = QLabel("External Lights")
        layout.addWidget(externalLightLabel, 22, 0)
        self.externalLightInput = QComboBox()
        self.externalLightInput.addItems(["Off", "On"])
        self.externalLightInput.currentIndexChanged.connect(self.getExternalLightInput)
        layout.addWidget(self.externalLightInput, 22, 1)

        # Add the Internal Lights Switch
        internalLightLabel = QLabel("Internal Lights")
        layout.addWidget(internalLightLabel, 23, 0)
        self.internalLightInput = QComboBox()
        self.internalLightInput.addItems(["Off", "On"])
        self.internalLightInput.currentIndexChanged.connect(self.getInternalLightInput)
        layout.addWidget(self.internalLightInput, 23, 1)

        # Add the Station Announcement Input
        stationLabel = QLabel("Station Announcement")
        layout.addWidget(stationLabel, 24, 0)
        self.stationInput = QLineEdit()
        self.stationInput.editingFinished.connect(self.getStationInput)
        layout.addWidget(self.stationInput, 24, 1)

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
        #prevBlockLabel = QLabel("Previous Block")
        #layout.addWidget(prevBlockLabel, 2, 2)
        #self.prevBlockOutput = QLineEdit()
        #self.prevBlockOutput.setReadOnly(True)
        #self.prevBlockOutput.setText("0")
        #layout.addWidget(self.prevBlockOutput, 2, 3)

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
        #realTimeClockLabel = QLabel("Real Time Clock")
        #layout.addWidget(realTimeClockLabel, 9, 2)
        #self.realTimeClockOutput = QLineEdit()
        #self.realTimeClockOutput.setReadOnly(True)
        #self.realTimeClockOutput.setText("12:00:00 am")
        #self.realTimeClockOutput.setFixedWidth(200)
        #layout.addWidget(self.realTimeClockOutput, 9, 3)

        # Adding the Underground State
        undergroundStateLabel = QLabel("Underground State")
        layout.addWidget(undergroundStateLabel, 10, 2)
        self.undergroundStateOutput = QLineEdit()
        self.undergroundStateOutput.setReadOnly(True)
        self.undergroundStateOutput.setText("0")
        layout.addWidget(self.undergroundStateOutput, 10, 3)

        # ADD THE TEMPERATURE OUTPUT
        temperatureLabel = QLabel("Temperature")
        layout.addWidget(temperatureLabel, 12, 2)
        self.temperatureOutput = QLineEdit()
        self.temperatureOutput.setReadOnly(True)
        self.temperatureOutput.setText("68 F")
        layout.addWidget(self.temperatureOutput, 12, 3)

        # Adding the Station Name Output
        beaconStationLabel = QLabel("Station Name")
        layout.addWidget(beaconStationLabel, 14, 2)
        self.beaconStationOutput = QLineEdit()
        self.beaconStationOutput.setReadOnly(True)
        self.beaconStationOutput.setText("")
        layout.addWidget(self.beaconStationOutput, 14, 3)

        # Adding the Platform Side Output
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 15, 2)
        self.platformSideOutput = QLineEdit()
        self.platformSideOutput.setReadOnly(True)
        self.platformSideOutput.setText("Left")
        layout.addWidget(self.platformSideOutput, 15, 3)

        # Adding the Next Station Name Output
        nextStationLabel = QLabel("nextStationName")
        layout.addWidget(nextStationLabel, 16, 2)
        self.nextStationOutput = QLineEdit()
        self.nextStationOutput.setReadOnly(True)
        self.nextStationOutput.setText("")
        layout.addWidget(self.nextStationOutput, 16, 3)

        # Adding the isBeacon Output
        isBeaconLabel = QLabel("isBeacon")
        layout.addWidget(isBeaconLabel, 17, 2)
        self.isBeaconOutput = QLineEdit()
        self.isBeaconOutput.setReadOnly(True)
        self.nextStationOutput.setText("False")
        layout.addWidget(self.isBeaconOutput, 17, 3)

        # Adding the External Light State
        externalLightLabel = QLabel("External Lights")
        layout.addWidget(externalLightLabel, 18, 2)
        self.externalLightOutput = QLineEdit()
        self.externalLightOutput.setReadOnly(True)
        self.externalLightOutput.setText("Off")
        layout.addWidget(self.externalLightOutput, 18, 3)

        # Adding the Internal Light State
        internalLightLabel = QLabel("Internal Lights")
        layout.addWidget(internalLightLabel, 19, 2)
        self.internalLightOutput = QLineEdit()
        self.internalLightOutput.setReadOnly(True)
        self.internalLightOutput.setText("Off")
        layout.addWidget(self.internalLightOutput, 19, 3)

        # Adding the Left Door State
        leftDoorLabel = QLabel("Left Doors")
        layout.addWidget(leftDoorLabel, 20, 2)
        self.leftDoorOutput = QLineEdit()
        self.leftDoorOutput.setReadOnly(True)
        self.leftDoorOutput.setText("Closed")
        layout.addWidget(self.leftDoorOutput, 20, 3)

        # Adding the Right Door State
        rightDoorLabel = QLabel("Right Doors")
        layout.addWidget(rightDoorLabel, 21, 2)
        self.rightDoorOutput = QLineEdit()
        self.rightDoorOutput.setReadOnly(True)
        self.rightDoorOutput.setText("Closed")
        layout.addWidget(self.rightDoorOutput, 21, 3)

        # Adding the Service Brake State
        serviceBrakeLabel = QLabel("Service Brake")
        layout.addWidget(serviceBrakeLabel, 22, 2)
        self.serviceBrakeOutput = QLineEdit()
        self.serviceBrakeOutput.setReadOnly(True)
        self.serviceBrakeOutput.setText("Disengaged")
        layout.addWidget(self.serviceBrakeOutput, 22, 3)

        # Adding the Emergency Brake State
        emergencyBrakeLabel = QLabel("Emergency Brake")
        layout.addWidget(emergencyBrakeLabel, 23, 2)
        self.emergencyBrakeOutput = QLineEdit()
        self.emergencyBrakeOutput.setReadOnly(True)
        self.emergencyBrakeOutput.setText("Disengaged")
        layout.addWidget(self.emergencyBrakeOutput, 23, 3)

        # ADD FAILURE STATUS
        brakeStatusLabel = QLabel("Service Brake Status")
        layout.addWidget(brakeStatusLabel, 24, 2)
        self.brakeStatusOutput = QLineEdit()
        self.brakeStatusOutput.setReadOnly(True)
        self.brakeStatusOutput.setText("Functional")
        layout.addWidget(self.brakeStatusOutput, 24, 3)

        engineStatusLabel = QLabel("Engine Status")
        layout.addWidget(engineStatusLabel, 25, 2)
        self.engineStatusOutput = QLineEdit()
        self.engineStatusOutput.setReadOnly(True)
        self.engineStatusOutput.setText("Functional")
        layout.addWidget(self.engineStatusOutput, 25, 3)

        commStatusLabel = QLabel("Communications Status")
        layout.addWidget(commStatusLabel, 26, 2)
        self.commStatusOutput = QLineEdit()
        self.commStatusOutput.setReadOnly(True)
        self.commStatusOutput.setText("Functional")
        layout.addWidget(self.commStatusOutput, 26, 3)

        updateButton = QPushButton("Update Values")
        updateButton.pressed.connect(self.updateOutputsBoth)
        layout.addWidget(updateButton, 27, 0, 1, 4)

        # Update Outputs to
        self.updateOutputsBoth()

    # Function to read the outputs from the Train Model to Train Controller (WAS USING JSON, SCRAPPED)
    #def readTrainModelToTrackModel(self):
    #    with open(os.path.join(sys.path[0], "TrainModelToTrackModel.json"), "r") as filename:
    #        self.trainModelToTrackModel = json.loads(filename.read())
    #    self.testDataOutputs["currBlock"]     = self.trainModelToTrackModel["currBlock"]
    #    self.testDataOutputs["prevBlock"]     = self.trainModelToTrackModel["prevBlock"]
    #    self.testDataOutputs["passengersOff"] = self.trainModelToTrackModel["passengersOff"]

    # Function to read the outputs from the Train Model to the Train Controller (WAS USING JSON, SCRAPPED)
    #def readTrainModelToTrainController(self):
    #    with open(os.path.join(sys.path[0], "TrainModelToTrainControllerSW.json"), "r") as filename:
    #        self.trainModelToTrainController = json.loads(filename.read())
    #    self.testDataOutputs["commandedSpeed"]       = self.trainModelToTrainController["commandedSpeed"]
    #    self.testDataOutputs["currentSpeed"]         = self.trainModelToTrainController["currentSpeed"]
    #    self.testDataOutputs["authority"]            = self.trainModelToTrainController["authority"]
    #    self.testDataOutputs["inputTime"]            = self.trainModelToTrainController["inputTime"]
    #    self.testDataOutputs["undergroundState"]     = self.trainModelToTrainController["undergroundState"]
    #    self.testDataOutputs["temperature"]          = self.trainModelToTrainController["temperature"]
    #    self.testDataOutputs["stationName"]          = self.trainModelToTrainController["stationName"]
    #    self.testDataOutputs["platformSide"]         = self.trainModelToTrainController["platformSide"]
    #    self.testDataOutputs["nextStationName"]      = self.trainModelToTrainController["nextStationName"]
    #    self.testDataOutputs["isBeacon"]             = self.trainModelToTrainController["isBeacon"]
    #    self.testDataOutputs["externalLightsState"]  = self.trainModelToTrainController["externalLightsState"]
    #    self.testDataOutputs["internalLightsState"]  = self.trainModelToTrainController["internalLightsState"]
    #    self.testDataOutputs["leftDoorState"]        = self.trainModelToTrainController["leftDoorState"]
    #    self.testDataOutputs["rightDoorState"]       = self.trainModelToTrainController["rightDoorState"]
    #    self.testDataOutputs["serviceBrakeState"]    = self.trainModelToTrainController["serviceBrakeState"]
    #    self.testDataOutputs["emergencyBrakeState"]  = self.trainModelToTrainController["emergencyBrakeState"]
    #    self.testDataOutputs["serviceBrakeStatus"]   = self.trainModelToTrainController["serviceBrakeStatus"]
    #    self.testDataOutputs["engineStatus"]         = self.trainModelToTrainController["engineStatus"]
    #    self.testDataOutputs["communicationsStatus"] = self.trainModelToTrainController["communicationsStatus"]

    # Function to write inputs from the Track Model to the Train Model (WAS USING JSON, SCRAPPED)
    #def writeTrackModelToTrainModel(self):
    #    self.trackModelToTrainModel["rtc"]                = self.testDataInputs["rtc"]
    #    self.trackModelToTrainModel["authority"]          = self.testDataInputs["authority"]
    #    self.trackModelToTrainModel["commandedSpeed"]     = self.testDataInputs["commandedSpeed"]
    #    self.trackModelToTrainModel["passengersEntering"] = self.testDataInputs["passengersEntering"]
    #    self.trackModelToTrainModel["undergroundState"]   = self.testDataInputs["undergroundState"]
    #    self.trackModelToTrainModel["beacon"]             = self.testDataInputs["beacon"]
    #    self.trackModelToTrainModel["switch"]             = self.testDataInputs["switch"]
    #    self.trackModelToTrainModel["switchState"]        = self.testDataInputs["switchState"]
    #    self.trackModelToTrainModel["blockLength"]        = self.testDataInputs["blockLength"]
    #    self.trackModelToTrainModel["elevation"]          = self.testDataInputs["elevation"]
    #    with open(os.path.join(sys.path[0], "TrackModelToTrainModel.json"), "w") as filename:
    #        (json.dump(self.trackModelToTrainModel, filename, indent=4))

    # Function to write inputs from the Train Controller to the Train Model (WAS USING JSON, SCRAPPED)
    #def writeTrainControllerToTrainModel(self):
    #    self.trainControllerToTrainModel["power"]                 = self.testDataInputs["power"]
    #    self.trainControllerToTrainModel["leftDoorCommand"]       = self.testDataInputs["leftDoorCommand"]
    #    self.trainControllerToTrainModel["rightDoorCommand"]      = self.testDataInputs["rightDoorCommand"]
    #    self.trainControllerToTrainModel["serviceBrakeCommand"]   = self.testDataInputs["serviceBrakeCommand"]
    #    self.trainControllerToTrainModel["emergencyBrakeCommand"] = self.testDataInputs["emergencyBrakeCommand"]
    #    self.trainControllerToTrainModel["externalLightCommand"]  = self.testDataInputs["externalLightCommand"]
    #    self.trainControllerToTrainModel["internalLightCommand"]  = self.testDataInputs["internalLightCommand"]
    #    self.trainControllerToTrainModel["stationAnnouncement"]   = self.testDataInputs["stationAnnouncement"]
    #    with open(os.path.join(sys.path[0], "TCtoTM1.json"), "w") as filename:
    #        (json.dump(self.trainControllerToTrainModel, filename, indent=4))
    
    # Emit Train Controller to Train Model Singals
    def emitTrainControllerSignals(self):
        TMTCSignals.commandedPowerSignal.emit(self.testDataInputs["id"], self.testDataInputs["power"])
        TMTCSignals.leftDoorCommandSignal.emit(self.testDataInputs["id"], self.testDataInputs["leftDoorCommand"])
        TMTCSignals.rightDoorCommandSignal.emit(self.testDataInputs["id"], self.testDataInputs["rightDoorCommand"])
        TMTCSignals.serviceBrakeCommandSignal.emit(self.testDataInputs["id"], self.testDataInputs["serviceBrakeCommand"])
        TMTCSignals.emergencyBrakeCommandSignal.emit(self.testDataInputs["id"], self.testDataInputs["emergencyBrakeCommand"])
        TMTCSignals.externalLightCommandSignal.emit(self.testDataInputs["id"], self.testDataInputs["externalLightCommand"])
        TMTCSignals.internalLightCommandSignal.emit(self.testDataInputs["id"], self.testDataInputs["internalLightCommand"])
        TMTCSignals.stationAnnouncementSignal.emit(self.testDataInputs["id"], self.testDataInputs["stationAnnouncement"])

    # Handle Train Model to Train Controller Signals
    def catchCommandedSpeed(self, id, cmdSpeed):
        self.testDataOutputs["commandedSpeed"] = cmdSpeed 

    def catchCurrentSpeed(self, id, speed):
        self.testDataOutputs["currentSpeed"] = speed

    def catchAuthority(self, id, authority):
        self.testDataOutputs["authority"] = authority

    def catchUndergroundState(self, id, underground):
        self.testDataOutputs["undergroundState"] = underground

    def catchTemperature(self, id, temp):
        self.testDataOutputs["temperature"] = temp

    def catchStationName(self, id, station):
        self.testDataOutputs["stationName"] = station

    def catchPlatformSide(self, id, platformSide):
        self.testDataOutputs["platformSide"] = platformSide

    def catchNextStationName(self, id, nextStation):
        self.testDataOutputs["nextStationName"] = nextStation
    
    def catchIsBeacon(self, id, isBeacon):
        self.testDataOutputs["isBeacon"] = isBeacon

    def catchExternalLights(self, id, offOn):
        self.testDataOutputs["externalLightsState"] = offOn
    
    def catchInternalLights(self, id, offOn):
        self.testDataOutputs["internalLightsState"] = offOn
    
    def catchLeftDoors(self, id, openClosed):
        self.testDataOutputs["leftDoorState"] = openClosed

    def catchRightDoors(self, id, openClosed):
        self.testDataOutputs["rightDoorState"] = openClosed

    def catchServiceBrakeState(self, id, serviceBrake):
        self.testDataOutputs["serviceBrakeState"] = serviceBrake
    
    def catchEmergencyBrakeState(self, id, emergencyBrake):
        self.testDataOutputs["emergencyBrakeState"] = emergencyBrake

    def catchServiceBrakeStatus(self, id, status):
        self.testDataOutputs["serviceBrakeStatus"] = status
    
    def catchEngineStatus(self, id, status):
        self.testDataOutputs["engineStatus"] = status
    
    def catchCommStatus(self, id, status):
        self.testDataOutputs["communicationsStatus"] = status

    # Emit Track Model to Train Model Signals
    def emitTrackModelSignals(self):
        TMTkMSignals.authoritySignal.emit(self.testDataInputs["id"], self.testDataInputs["authority"])
        TMTkMSignals.commandedSpeedSignal.emit(self.testDataInputs["id"], self.testDataInputs["commandedSpeed"])
        TMTkMSignals.passengersEnteringSignal.emit(self.testDataInputs["id"], self.testDataInputs["passengersEntering"])
        TMTkMSignals.undergroundStateSignal.emit(self.testDataInputs["id"], self.testDataInputs["undergroundState"])
        TMTkMSignals.beaconSignal.emit(self.testDataInputs["id"], self.testDataInputs["beacon"][0], self.testDataInputs["beacon"][1], self.testDataInputs["beacon"][2], self.testDataInputs["beacon"][3], -1, False)
        TMTkMSignals.switchSignal.emit(self.testDataInputs["id"], self.testDataInputs["switch"])
        TMTkMSignals.switchStateSignal.emit(self.testDataInputs["id"], self.testDataInputs["switchState"])
        TMTkMSignals.blockLengthSignal.emit(self.testDataInputs["id"], self.testDataInputs["blockLength"])
        TMTkMSignals.elevationSignal.emit(self.testDataInputs["id"], self.testDataInputs["elevation"])

    # Handle Train Model to Track Model Signals
    def catchPassengersOff(self, id, passOff):
        self.testDataOutputs["passengersOff"] = passOff
    
    def catchCurrBlock(self, id, block):
        self.testDataOutputs["currBlock"] = block

    def getSwitchInput(self, index):
        self.testDataInputs["switch"] = bool(index)
    
    def getSwitchStateInput(self, index):
        self.testDataInputs["switchState"] = index

    def getBlockLengthInput(self):
        self.testDataInputs["blockLength"] = float(self.blockLengthInput.text())

    def getElevationInput(self):
        self.testDataInputs["elevation"] = float(self.elevationInput.text())

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
    #def getRealTimeClockInput(self):
    #    self.testDataInputs["rtc"] = self.realTimeClockInput.text()

    # Gets the Authority input from the UI
    def getAuthorityInput(self):
        self.testDataInputs["authority"] = int(self.authorityInput.text())

    # Gets the commanded speed from the UI
    def getCommandedSpeedInput(self):
        self.testDataInputs["commandedSpeed"] = float(self.commandedSpeedInput.text())

    # Gets the number of passengers entering the train from the UI
    def getPassengersEnteringInput(self):
        self.testDataInputs["passengersEntering"] = int(self.passengersEnteringInput.text())

    # Gets the Underground state from the UI
    def getUndergroundStateInput(self, index):
        self.testDataInputs["undergroundState"] = bool(index)

    # Get station name input
    def getStationNameInput(self):
        self.testDataInputs["beacon"][0] = self.stationNameInput.text()

    # Gets the Platform Side input from the UI
    def getPlatformSideInput(self, index):
        self.testDataInputs["beacon"][1] = index

    # Gets the Next Station input from the UI
    def getNextStationInput(self):
        self.testDataInputs["beacon"][2] = self.nextStationInput.text()
    
    # Gets the beacon state input
    def getIsBeaconInput(self, index):
        self.testDataInputs["beacon"][3] = bool(index)

    # Updates all functions when the button is pressed
    def updateOutputsBoth(self):
        # Wipe Output files so they are clean (WAS USING JSON, SCRAPPED)
        #with open(os.path.join(sys.path[0], "TrainControllerSWToTrainModel.json"), "w") as filename:
        #    (json.dump({}, filename, indent=4))
        #with open(os.path.join(sys.path[0], "TrackModelToTrainModel.json"), "w") as filename:
        #    (json.dump({}, filename, indent=4))

        #time = datetime.now()
        #iso_time = time.isoformat()
        #self.testDataInputs["rtc"] = str(iso_time) + "-5:00"
        #print(self.testDataInputs["rtc"])

        # Write Data To Output Module
        #self.writeTrackModelToTrainModel() (WAS USING JSON, SCRAPPED)
        #self.writeTrainControllerToTrainModel() (WAS USING JSON, SCRAPPED)
        self.emitTrainControllerSignals()
        self.emitTrackModelSignals()
        trainSignals.updateOutputs.emit()
        #self.readTrainModelToTrackModel() (WAS USING JSON, SCRAPPED)
        #self.readTrainModelToTrainController() (WAS USING JSON, SCRAPPED)

        self.currBlockOutput.setText("Block " + str(self.testDataOutputs["currBlock"]))
        #self.prevBlockOutput.setText("Block " + str(self.testDataOutputs["prevBlock"]))
        self.passengersExitingOutput.setText(str(self.testDataOutputs["passengersOff"]))
        #self.idOutput.setText(str(self.testDataOutputs["id"]))
        self.commandedSpeedOutput.setText(str(self.testDataOutputs["commandedSpeed"]) + " m/s")
        self.velocityOutput.setText(str(round(self.testDataOutputs["currentSpeed"], 2)) + " m/s")
        self.authorityOutput.setText(str(self.testDataOutputs["authority"]) + " Blocks")
        #self.realTimeClockOutput.setText(self.testDataOutputs["inputTime"])
        self.undergroundStateOutput.setText(str(bool(self.testDataOutputs["undergroundState"])))
        self.temperatureOutput.setText(str(self.testDataOutputs["temperature"]) + " F")
        self.beaconStationOutput.setText(self.testDataOutputs["stationName"])
        self.platformSideOutput.setText(str(self.testDataOutputs["platformSide"]))
        self.nextStationOutput.setText(self.testDataOutputs["nextStationName"])
        self.isBeaconOutput.setText(str(self.testDataOutputs["isBeacon"]))


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
    mainUI = TrainModelUI(2, "Green")
    mainUI.show()
    app.exec()

if __name__ == "__main__":
    main()
