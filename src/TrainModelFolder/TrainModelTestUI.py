# Train Model Test UI

# Importing all required modules
import sys
sys.path.append(__file__.replace("\TrainModelFolder\TrainModelTestUI.py", ""))

from datetime import *
from sys import argv
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from TrainModelFolder.TrainModelMainUI import TrainModelUI
from TrainModelFolder.TrainModelSignals import *
from Integration.TMTCSignals import *
from Integration.TMTkMSignals import *
from Integration.TimeSignals import *


# Class for the Train Model Test UI
class TrainModelTestUI(QWidget):

    testDataInputs = {
        "rtc"                   : "2023-02-22T11:00:00.0000000-05:00",
        "authority"             : 0,
        "commandedSpeed"        : 0.0,
        "passengersEntering"    : 0,
        "beacon"                : ["", 0, "", False, -1, 0, 0],
        "switch"                : False,
        "switchState"           : 0,
        "id"                    : 0,
        "power"                 : 0.0,
        "leftDoorCommand"       : False,
        "rightDoorCommand"      : False,
        "serviceBrakeCommand"   : False,
        "emergencyBrakeCommand" : False,
        "externalLightCommand"  : False,
        "internalLightCommand"  : False,
        "stationAnnouncement"   : "The Yard",
        "isAtStation"           : False
    }

    testDataOutputs = {
        "currBlock"            : 0,
        "passengersOff"        : 0,
        "commandedSpeed"       : 0.0,
        "currentSpeed"         : 0.0,
        "authority"            : 0,
        "undergroundState"     : False,
        "temperature"          : 0.0,
        "stationName"          : "",
        "platformSide"         : 0,
        "nextStationName"      : "",
        "isBeacon"             : False,
        "polarityCount"        : -1,
        "positiveNegative"     : 0,
        "switchBlock"          : 0,
        "externalLightsState"  : False,
        "internalLightsState"  : False,
        "leftDoorState"        : False,
        "rightDoorState"       : False,
        "serviceBrakeState"    : False,
        "emergencyBrakeState"  : False,
        "serviceBrakeStatus"   : True,
        "engineStatus"         : True,
        "communicationsStatus" : True,
        "polarity"             : 0
    }


    def mainThreadSetup(self):
        self.timerThread = QThread()
        self.timerThread.started.connect(self.mainTimerSetup)

    def mainTimerSetup(self):     
        mainTimer = QTimer()
        mainTimer.setInterval(self.timerInterval)
        mainTimer.timeout.connect(self.mainEventLoop)
        mainTimer.setParent(self)
        mainTimer.start()
        return mainTimer
    
    def mainEventLoop(self):
        self.rtc = self.rtc + timedelta(0, 0, 0, self.timerInterval * self.simulationSpeed)
        rtcSignals.rtcSignal.emit(self.rtc.isoformat() + "0-04:00")
        self.updateOutputsBoth()


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
        TMTCSignals.blockCountSignal.connect(self.catchBlockCount)
        TMTCSignals.fromSwitchSignal.connect(self.catchFromSwitch)
        TMTCSignals.externalLightsStateSignal.connect(self.catchExternalLights)
        TMTCSignals.internalLightsStateSignal.connect(self.catchInternalLights)
        TMTCSignals.leftDoorStateSignal.connect(self.catchLeftDoors)
        TMTCSignals.rightDoorStateSignal.connect(self.catchRightDoors)
        TMTCSignals.serviceBrakeStateSignal.connect(self.catchServiceBrakeState)
        TMTCSignals.emergencyBrakeStateSignal.connect(self.catchEmergencyBrakeState)
        TMTCSignals.serviceBrakeStatusSignal.connect(self.catchServiceBrakeStatus)
        TMTCSignals.engineStatusSignal.connect(self.catchEngineStatus)
        TMTCSignals.communicationsStatusSignal.connect(self.catchCommStatus)
        TMTCSignals.polaritySignal.connect(self.catchPolarity)

        self.simulationSpeed = 1
        self.timerInterval = 100
        self.rtc = datetime.now()
        
        # Initializing the layout of the UI
        super().__init__()
        self.mainTimer = self.mainTimerSetup()
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

        # Add the Authority Input
        authorityLabel = QLabel("Authority")
        layout.addWidget(authorityLabel, 1, 0)
        self.authorityInput = QLineEdit()
        self.authorityInput.editingFinished.connect(self.getAuthorityInput)
        layout.addWidget(self.authorityInput, 1, 1)

        # Add the Commanded Speed Input
        commandedSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(commandedSpeedLabel, 2, 0)
        self.commandedSpeedInput = QLineEdit()
        self.commandedSpeedInput.editingFinished.connect(self.getCommandedSpeedInput)
        layout.addWidget(self.commandedSpeedInput, 2, 1)

        # Add the Passengers Entering Input
        passengersEnteringLabel = QLabel("Passengers Entering")
        layout.addWidget(passengersEnteringLabel, 3, 0)
        self.passengersEnteringInput = QLineEdit()
        self.passengersEnteringInput.editingFinished.connect(self.getPassengersEnteringInput)
        layout.addWidget(self.passengersEnteringInput, 3, 1)

        # Add the Switch Input
        switchLabel = QLabel("Switch")
        layout.addWidget(switchLabel, 4, 0)
        self.switchInput = QComboBox()
        self.switchInput.addItems(["False", "True"])
        self.switchInput.currentIndexChanged.connect(self.getSwitchInput)
        layout.addWidget(self.switchInput, 4, 1)

        # Add the Switch State Input
        switchStateLabel = QLabel("Switch State")
        layout.addWidget(switchStateLabel, 5, 0)
        self.switchStateInput = QComboBox()
        self.switchStateInput.addItems(["0", "1"])
        self.switchStateInput.currentIndexChanged.connect(self.getSwitchStateInput)
        layout.addWidget(self.switchStateInput, 5, 1)

        # Add the Beacon Inputs [stationName, platformSide, nextStationName, isBeacon, polarityCount, positiveNegative]
        beaconLabel = QLabel("Beacon Inputs")
        layout.addWidget(beaconLabel, 6, 0, 2, 1)
        beaconLabel2 = QLabel("[stationName, platformSide, nextStationName, isBeacon, polarityCount, positiveNegative]")
        beaconLabel2.setWordWrap(True)
        layout.addWidget(beaconLabel2, 6, 1, 2, 1)

        # Add the Station Name Beacon Input
        stationNameLabel = QLabel("Station Name")
        layout.addWidget(stationNameLabel, 8, 0)
        self.stationNameInput = QLineEdit()
        self.stationNameInput.editingFinished.connect(self.getStationNameInput)
        layout.addWidget(self.stationNameInput, 8, 1)

        # Platform Side Beacon Selector
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 9, 0)
        self.platformSideInput = QComboBox()
        self.platformSideInput.addItems(["Left", "Right", "Both"])
        self.platformSideInput.currentIndexChanged.connect(self.getPlatformSideInput)
        layout.addWidget(self.platformSideInput, 9, 1)

        # Next Station Name Beacon Input
        nextStationLabel = QLabel("Next Station Name")
        layout.addWidget(nextStationLabel, 10, 0)
        self.nextStationInput = QLineEdit()
        self.nextStationInput.editingFinished.connect(self.getNextStationInput)
        layout.addWidget(self.nextStationInput, 10, 1)

        # is Beacon Input
        isBeaconLabel = QLabel("isBeacon")
        layout.addWidget(isBeaconLabel, 11, 0)
        self.isBeaconInput = QComboBox()
        self.isBeaconInput.addItems(["False", "True"])
        self.isBeaconInput.currentIndexChanged.connect(self.getIsBeaconInput)
        layout.addWidget(self.isBeaconInput, 11, 1)

        # polarityCounterInput
        polarityCountLabel = QLabel("PolarityCount")
        layout.addWidget(polarityCountLabel, 12, 0)
        self.polarityCountInput = QLineEdit()
        self.polarityCountInput.editingFinished.connect(self.getPolarityCountInput)
        layout.addWidget(self.polarityCountInput, 12, 1)

        # positiveNegative Input
        positiveNegativeLabel = QLabel("PositiveNegative")
        layout.addWidget(positiveNegativeLabel, 13, 0)
        self.positiveNegativeInput = QComboBox()
        self.positiveNegativeInput.addItems(["Positive", "Negative"])
        self.positiveNegativeInput.currentIndexChanged.connect(self.getPositiveNegativeInput)
        layout.addWidget(self.positiveNegativeInput, 13, 1)

        # switchBlock Input
        switchBlockLabel = QLabel("switchBlock")
        layout.addWidget(switchBlockLabel, 14, 0)
        self.switchBlockInput = QLineEdit()
        self.switchBlockInput.editingFinished.connect(self.getSwitchBlock)
        layout.addWidget(self.switchBlockInput, 14, 1)

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

        # Add the isAtStation Input
        atStationLabel = QLabel("isAtStation")
        layout.addWidget(atStationLabel, 25, 0)
        self.atStationInput = QComboBox()
        self.atStationInput.addItems(["False", "True"])
        self.atStationInput.currentIndexChanged.connect(self.getAtStationInput)
        layout.addWidget(self.atStationInput, 25, 1)

        # Simluation Speed Selector
        simSpeedLabel = QLabel("Simulation Speed")
        layout.addWidget(simSpeedLabel, 26, 0)
        self.simSpeedInput = QLineEdit()
        self.simSpeedInput.editingFinished.connect(self.simSpeedUpdate)
        layout.addWidget(self.simSpeedInput, 26, 1)

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

        # Adding the Passengers Exiting
        passengersExitingLabel = QLabel("Passengers Exiting")
        layout.addWidget(passengersExitingLabel, 2, 2)
        self.passengersExitingOutput = QLineEdit()
        self.passengersExitingOutput.setReadOnly(True)
        self.passengersExitingOutput.setText("0")
        layout.addWidget(self.passengersExitingOutput, 2, 3)

        # Adding the Train Controller Label
        trainControllerOutputLabel = QLabel("Train Controller Outputs")
        layout.addWidget(trainControllerOutputLabel, 3, 2, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Adding the Train ID Output
        idOutputLabel = QLabel("Train ID")
        layout.addWidget(idOutputLabel, 4, 2)
        self.idOutput = QLineEdit()
        self.idOutput.setReadOnly(True)
        self.idOutput.setText("0")
        layout.addWidget(self.idOutput, 4, 3)

        # Adding the Commanded Speed
        commandedSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(commandedSpeedLabel, 5, 2)
        self.commandedSpeedOutput = QLineEdit()
        self.commandedSpeedOutput.setReadOnly(True)
        self.commandedSpeedOutput.setText("0 m/s")
        layout.addWidget(self.commandedSpeedOutput, 5, 3)

        # Adding the Velocity
        velocityLabel = QLabel("Current Speed")
        layout.addWidget(velocityLabel, 6, 2)
        self.velocityOutput = QLineEdit()
        self.velocityOutput.setReadOnly(True)
        self.velocityOutput.setText("0 m/s")
        layout.addWidget(self.velocityOutput, 6, 3)

        # Adding the Authority
        authorityLabel = QLabel("Authority")
        layout.addWidget(authorityLabel, 7, 2)
        self.authorityOutput = QLineEdit()
        self.authorityOutput.setReadOnly(True)
        self.authorityOutput.setText("0 Blocks")
        layout.addWidget(self.authorityOutput, 7, 3)

        # Adding the Underground State
        undergroundStateLabel = QLabel("Underground State")
        layout.addWidget(undergroundStateLabel, 8, 2)
        self.undergroundStateOutput = QLineEdit()
        self.undergroundStateOutput.setReadOnly(True)
        self.undergroundStateOutput.setText("0")
        layout.addWidget(self.undergroundStateOutput, 8, 3)

        # ADD THE TEMPERATURE OUTPUT
        temperatureLabel = QLabel("Temperature")
        layout.addWidget(temperatureLabel, 9, 2)
        self.temperatureOutput = QLineEdit()
        self.temperatureOutput.setReadOnly(True)
        self.temperatureOutput.setText("68 F")
        layout.addWidget(self.temperatureOutput, 9, 3)

        # Adding the Station Name Output
        beaconStationLabel = QLabel("Station Name")
        layout.addWidget(beaconStationLabel, 10, 2)
        self.beaconStationOutput = QLineEdit()
        self.beaconStationOutput.setReadOnly(True)
        self.beaconStationOutput.setText("")
        layout.addWidget(self.beaconStationOutput, 10, 3)

        # Adding the Platform Side Output
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 11, 2)
        self.platformSideOutput = QLineEdit()
        self.platformSideOutput.setReadOnly(True)
        self.platformSideOutput.setText("Left")
        layout.addWidget(self.platformSideOutput, 11, 3)

        # Adding the Next Station Name Output
        nextStationLabel = QLabel("nextStationName")
        layout.addWidget(nextStationLabel, 12, 2)
        self.nextStationOutput = QLineEdit()
        self.nextStationOutput.setReadOnly(True)
        self.nextStationOutput.setText("")
        layout.addWidget(self.nextStationOutput, 12, 3)

        # Adding the isBeacon Output
        isBeaconLabel = QLabel("isBeacon")
        layout.addWidget(isBeaconLabel, 13, 2)
        self.isBeaconOutput = QLineEdit()
        self.isBeaconOutput.setReadOnly(True)
        self.isBeaconOutput.setText("False")
        layout.addWidget(self.isBeaconOutput, 13, 3)

        # Adding the polarityCounter Output
        polarityCountOutputLabel = QLabel("polarityCount")
        layout.addWidget(polarityCountOutputLabel, 14, 2)
        self.polarityCountOutput = QLineEdit()
        self.polarityCountOutput.setReadOnly(True)
        self.polarityCountOutput.setText("-1")
        layout.addWidget(self.polarityCountOutput, 14, 3)

        # Adding the positiveNegative Output
        positiveNegativeOutputLabel = QLabel("positiveNegative")
        layout.addWidget(positiveNegativeOutputLabel, 15, 2)
        self.positiveNegativeOutput = QLineEdit()
        self.positiveNegativeOutput.setReadOnly(True)
        self.positiveNegativeOutput.setText("False")
        layout.addWidget(self.positiveNegativeOutput, 15, 3)

        # Adding the switchBlock Output
        switchBlockOutputLabel = QLabel("switchBlock")
        layout.addWidget(switchBlockOutputLabel, 16, 2)
        self.switchBlockOutput = QLineEdit()
        self.switchBlockOutput.setReadOnly(True)
        self.switchBlockOutput.setText("0")
        layout.addWidget(self.switchBlockOutput, 16, 3)

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

        # Adding the Polarity Output
        polarityOutputLabel = QLabel("Polarity")
        layout.addWidget(polarityOutputLabel, 26, 2)
        self.polarityOutput = QLineEdit()
        self.polarityOutput.setReadOnly(True)
        self.polarityOutput.setText("")
        layout.addWidget(self.polarityOutput, 26, 3)
    
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
        TMTCSignals.stationStateSignal.emit(self.testDataInputs["id"], self.testDataInputs["isAtStation"])

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
    
    def catchBlockCount(self, id, blockCount):
        self.testDataOutputs["polarityCount"] = blockCount

    def catchFromSwitch(self, id, fromSwitch):
        self.testDataOutputs["positiveNegative"] = fromSwitch
    
    def catchSwitchBlock(self, id, switchBlock):
        self.testDataOutputs["switchBlock"] = switchBlock

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

    def catchPolarity(self, id, polarity):
        self.testDataOutputs["polarity"] = polarity

    # Emit Track Model to Train Model Signals
    def emitTrackModelSignals(self):
        TMTkMSignals.authoritySignal.emit(self.testDataInputs["id"], self.testDataInputs["authority"])
        TMTkMSignals.commandedSpeedSignal.emit(self.testDataInputs["id"], self.testDataInputs["commandedSpeed"])
        TMTkMSignals.passengersEnteringSignal.emit(self.testDataInputs["id"], self.testDataInputs["passengersEntering"])
        TMTkMSignals.beaconSignal.emit(self.testDataInputs["id"], self.testDataInputs["beacon"][0], self.testDataInputs["beacon"][1], self.testDataInputs["beacon"][2], self.testDataInputs["beacon"][3], self.testDataInputs["beacon"][4], self.testDataInputs["beacon"][5], self.testDataInputs["beacon"][6])
        TMTkMSignals.switchSignal.emit(self.testDataInputs["id"], self.testDataInputs["switch"])
        TMTkMSignals.switchStateSignal.emit(self.testDataInputs["id"], self.testDataInputs["switchState"])

    # Handle Train Model to Track Model Signals
    def catchPassengersOff(self, id, passOff):
        self.testDataOutputs["passengersOff"] = passOff
    
    def catchCurrBlock(self, id, block):
        self.testDataOutputs["currBlock"] = block

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

    # Gets the Simulation Speed Updated from the UI
    def simSpeedUpdate(self):
        self.simulationSpeed = int(self.simSpeedInput.text())

    # Gets the At Station Input from the UI
    def getAtStationInput(self, index):
        self.testDataInputs["isAtStation"] = bool(index)

    # Gets the Polarity Count Beacon input from the UI
    def getPolarityCountInput(self):
        self.testDataInputs["beacon"][4] = int(self.polarityCountInput.text())

    # Gets the positive negative beacon input from the UI
    def getPositiveNegativeInput(self, index):
        self.testDataInputs["beacon"][5] = bool(index)

    # Gets the switch block input from the UI
    def getSwitchBlock(self):
        self.testDataInputs["beacon"][6] = int(self.switchBlockInput.text())

    # Updates all functions when the button is pressed
    def updateOutputsBoth(self):
        if (__name__ == "__main__"):
            self.emitTrainControllerSignals()

        self.emitTrackModelSignals()

        self.currBlockOutput.setText("Block " + str(self.testDataOutputs["currBlock"]))
        self.passengersExitingOutput.setText(str(self.testDataOutputs["passengersOff"]))
        self.commandedSpeedOutput.setText(str(self.testDataOutputs["commandedSpeed"]) + " m/s")
        self.velocityOutput.setText(str(round(self.testDataOutputs["currentSpeed"], 2)) + " m/s")
        self.authorityOutput.setText(str(self.testDataOutputs["authority"]) + " Blocks")
        self.undergroundStateOutput.setText(str(bool(self.testDataOutputs["undergroundState"])))
        self.temperatureOutput.setText(str(self.testDataOutputs["temperature"]) + " F")
        self.beaconStationOutput.setText(self.testDataOutputs["stationName"])
        self.platformSideOutput.setText(str(self.testDataOutputs["platformSide"]))
        self.nextStationOutput.setText(self.testDataOutputs["nextStationName"])
        self.isBeaconOutput.setText(str(self.testDataOutputs["isBeacon"]))
        self.polarityCountOutput.setText(str(self.testDataOutputs["polarityCount"]))
        self.positiveNegativeOutput.setText(str(self.testDataOutputs["positiveNegative"]))
        self.switchBlockOutput.setText(str(self.testDataOutputs["switchBlock"]))

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
        self.polarityOutput.setText(str(self.testDataOutputs["polarity"]))

def main():
    app = QApplication(argv)
    testUI = TrainModelTestUI()
    testUI.show()
    mainUI = TrainModelUI(2, "Green")
    mainUI.show()
    app.exec()

if __name__ == "__main__":
    main()