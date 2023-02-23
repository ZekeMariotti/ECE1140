# Train Model Test UI

# Importing all required modules
from sys import argv
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from TrainModelMainUI import TrainModelMainUI
from TrainModelSignals import *


# Class for the Train Model Test UI
class TrainModelTestUI(QWidget):

    testData = {
        "rtc"            : "12:00:00 am",
        "sBrake"         : False,
        "eBrake"         : False,
        "eBrakeUser"     : False,
        "eBrakeTest"     : False,
        "lDoors"         : False,
        "rDoors"         : False,
        "eLights"        : False,
        "iLights"        : False,
        "authority"      : 0,
        "cmdSpeed"       : 0.0,
        "velocity"       : 0.0,
        "underground"    : False,
        "speedLimit"     : 0.0,
        "beacon"         : [False, "", 0],
        "passengersOff"  : 0,
        "commStatus"     : True,
        "sBrakeStatus"   : True
    }

    # Initialize the GUI
    def __init__(self):
        
        # Back End Signal Handlers
        trainSignals.velocityToTestUI.connect(self.setCurrentVelocity)
        trainSignals.eBrakeToTestUI.connect(self.eBrakeHandler)
        trainSignals.passengersOff.connect(self.passengersOffHandler)
        trainSignals.communicationsFailure.connect(self.commFailureHandler)
        trainSignals.sBrakeFailure.connect(self.sBrakeFailureHandler)

        # Initializing the layout of the UI
        super().__init__()
        self.setWindowTitle("Train Model Test UI")
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFixedSize(500, 700)
        orientation = self.frameGeometry()
        self.move(orientation.topLeft())

        # Setting up all the inputs
        # Add the Power Input
        powerLabel = QLabel("Power Input")
        layout.addWidget(powerLabel, 0, 0)
        self.powerInput = QLineEdit()
        self.powerInput.editingFinished.connect(self.getPowerInput)
        layout.addWidget(self.powerInput, 0, 1)

        # Add the Service Brake Switch
        serviceBrakeLabel = QLabel("Service Brake")
        layout.addWidget(serviceBrakeLabel, 1, 0)
        self.serviceBrakeInput = QComboBox()
        self.serviceBrakeInput.addItems(["Disengaged", "Engaged"])
        self.serviceBrakeInput.currentIndexChanged.connect(self.getServiceBrakeInput)
        layout.addWidget(self.serviceBrakeInput, 1, 1)

        # Add the Emergency Brake Switch
        emergencyBrakeLabel = QLabel("Emergency Brake")
        layout.addWidget(emergencyBrakeLabel, 2, 0)
        self.emergencyBrakeInput = QComboBox()
        self.emergencyBrakeInput.addItems(["Disengaged", "Engaged"])
        self.emergencyBrakeInput.currentIndexChanged.connect(self.getEmergencyBrakeInput)
        layout.addWidget(self.emergencyBrakeInput, 2, 1)

        # Add the Left Door Switch
        leftDoorLabel = QLabel("Left Doors")
        layout.addWidget(leftDoorLabel, 3, 0)
        self.leftDoorInput = QComboBox()
        self.leftDoorInput.addItems(["Closed", "Open"])
        self.leftDoorInput.currentIndexChanged.connect(self.getLeftDoorInput)
        layout.addWidget(self.leftDoorInput, 3, 1)

        # Add the Right Door Switch
        rightDoorLabel = QLabel("Right Doors")
        layout.addWidget(rightDoorLabel, 4, 0)
        self.rightDoorInput = QComboBox()
        self.rightDoorInput.addItems(["Closed", "Open"])
        self.rightDoorInput.currentIndexChanged.connect(self.getRightDoorInput)
        layout.addWidget(self.rightDoorInput, 4, 1)

        # Add the External Lights Switch
        externalLightLabel = QLabel("External Lights")
        layout.addWidget(externalLightLabel, 5, 0)
        self.externalLightInput = QComboBox()
        self.externalLightInput.addItems(["Off", "On"])
        self.externalLightInput.currentIndexChanged.connect(self.getExternalLightInput)
        layout.addWidget(self.externalLightInput, 5, 1)

        # Add the Internal Lights Switch
        internalLightLabel = QLabel("Internal Lights")
        layout.addWidget(internalLightLabel, 6, 0)
        self.internalLightInput = QComboBox()
        self.internalLightInput.addItems(["Off", "On"])
        self.internalLightInput.currentIndexChanged.connect(self.getInternalLightInput)
        layout.addWidget(self.internalLightInput, 6, 1)

        # Add the Station Announcement Input
        stationLabel = QLabel("Station Announcement")
        layout.addWidget(stationLabel, 7, 0)
        self.stationInput = QLineEdit()
        self.stationInput.editingFinished.connect(self.getStationInput)
        layout.addWidget(self.stationInput, 7, 1)

        # Add the Real Time Clock Input
        realTimeClockLabel = QLabel("Real Time Clock")
        layout.addWidget(realTimeClockLabel, 8, 0)
        self.realTimeClockInput = QLineEdit()
        self.realTimeClockInput.editingFinished.connect(self.getRealTimeClockInput)
        layout.addWidget(self.realTimeClockInput, 8, 1)

        # Add the Authority Input
        authorityLabel = QLabel("Authority")
        layout.addWidget(authorityLabel, 9, 0)
        self.authorityInput = QLineEdit()
        self.authorityInput.editingFinished.connect(self.getAuthorityInput)
        layout.addWidget(self.authorityInput, 9, 1)

        # Add the Commanded Speed Input
        commandedSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(commandedSpeedLabel, 10, 0)
        self.commandedSpeedInput = QLineEdit()
        self.commandedSpeedInput.editingFinished.connect(self.getCommandedSpeedInput)
        layout.addWidget(self.commandedSpeedInput, 10, 1)

        # Add the Passengers Entering Input
        passengersEnteringLabel = QLabel("Passengers Entering")
        layout.addWidget(passengersEnteringLabel, 11, 0)
        self.passengersEnteringInput = QLineEdit()
        self.passengersEnteringInput.editingFinished.connect(self.getPassengersEnteringInput)
        layout.addWidget(self.passengersEnteringInput, 11, 1)

        # Add the Block Length Input
        blockLengthLabel = QLabel("Block Length")
        layout.addWidget(blockLengthLabel, 12, 0)
        self.blockLengthInput = QLineEdit()
        self.blockLengthInput.editingFinished.connect(self.getBlockLengthInput)
        layout.addWidget(self.blockLengthInput, 12, 1)

        # Add the Elevation Input
        elevationLabel = QLabel ("Elevation")
        layout.addWidget(elevationLabel, 13, 0)
        self.elevationInput = QLineEdit()
        self.elevationInput.editingFinished.connect(self.getElevationInput)
        layout.addWidget(self.elevationInput, 13, 1)

        # Add the Speed Limit Input
        speedLimitLabel = QLabel("Speed Limit")
        layout.addWidget(speedLimitLabel, 14, 0)
        self.speedLimitInput = QLineEdit()
        self.speedLimitInput.editingFinished.connect(self.getSpeedLimitInput)
        layout.addWidget(self.speedLimitInput, 14, 1)

        # Add the Acceleration Limit Input
        accelerationLimitLabel = QLabel("Acceleration Limit")
        layout.addWidget(accelerationLimitLabel, 15, 0)
        self.accelerationLimitInput = QLineEdit()
        self.accelerationLimitInput.editingFinished.connect(self.getAccelerationLimitInput)
        layout.addWidget(self.accelerationLimitInput, 15, 1)

        # Add the Underground State Switch
        undergroundStateLabel = QLabel("Underground State")
        layout.addWidget(undergroundStateLabel, 16, 0)
        self.undergroundStateInput = QComboBox()
        self.undergroundStateInput.addItems(["False", "True"])
        self.undergroundStateInput.currentIndexChanged.connect(self.getUndergroundStateInput)
        layout.addWidget(self.undergroundStateInput, 16, 1)

        # Add the Beacon Inputs [Station State, Next Station Name, Platform Side]
        beaconLabel = QLabel("Beacon Inputs")
        layout.addWidget(beaconLabel, 17, 0)
        beaconLabel2 = QLabel("[Station State, Next Station Name, Platform Side]")
        beaconLabel2.setWordWrap(True)
        layout.addWidget(beaconLabel2, 17, 1)

        # Station State Beacon Switch
        stationStateLabel = QLabel("Station State")
        layout.addWidget(stationStateLabel, 18, 0)
        self.stationStateInput = QComboBox()
        self.stationStateInput.addItems(["False", "True"])
        self.stationStateInput.currentIndexChanged.connect(self.getStationStateInput)
        layout.addWidget(self.stationStateInput, 18, 1)

        # Next Station Name Beacon Input
        nextStationLabel = QLabel("Next Station Name")
        layout.addWidget(nextStationLabel, 19, 0)
        self.nextStationInput = QLineEdit()
        self.nextStationInput.editingFinished.connect(self.getNextStationInput)
        layout.addWidget(self.nextStationInput, 19, 1)

        # Platform Side Beacon Selector
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 20, 0)
        self.platformSideInput = QComboBox()
        self.platformSideInput.addItems(["Left", "Right", "Both"])
        self.platformSideInput.currentIndexChanged.connect(self.getPlatformSideInput)
        layout.addWidget(self.platformSideInput, 20, 1)

        # Setting up all the outputs

        # Adding the Real Time Clock
        realTimeClockLabel = QLabel("Real Time Clock")
        layout.addWidget(realTimeClockLabel, 0, 2)
        self.realTimeClockOutput = QLineEdit()
        self.realTimeClockOutput.setReadOnly(True)
        self.realTimeClockOutput.setText("12:00:00 am")
        layout.addWidget(self.realTimeClockOutput, 0, 3)

        # Adding the Service Brake State
        serviceBrakeLabel = QLabel("Service Brake")
        layout.addWidget(serviceBrakeLabel, 1, 2)
        self.serviceBrakeOutput = QLineEdit()
        self.serviceBrakeOutput.setReadOnly(True)
        self.serviceBrakeOutput.setText("Disengaged")
        layout.addWidget(self.serviceBrakeOutput, 1, 3)

        # Adding the Emergency Brake State
        emergencyBrakeLabel = QLabel("Emergency Brake")
        layout.addWidget(emergencyBrakeLabel, 2, 2)
        self.emergencyBrakeOutput = QLineEdit()
        self.emergencyBrakeOutput.setReadOnly(True)
        self.emergencyBrakeOutput.setText("Disengaged")
        layout.addWidget(self.emergencyBrakeOutput, 2, 3)

        # Adding the Left Door State
        leftDoorLabel = QLabel("Left Doors")
        layout.addWidget(leftDoorLabel, 3, 2)
        self.leftDoorOutput = QLineEdit()
        self.leftDoorOutput.setReadOnly(True)
        self.leftDoorOutput.setText("Closed")
        layout.addWidget(self.leftDoorOutput, 3, 3)

        # Adding the Right Door State
        rightDoorLabel = QLabel("Right Doors")
        layout.addWidget(rightDoorLabel, 4, 2)
        self.rightDoorOutput = QLineEdit()
        self.rightDoorOutput.setReadOnly(True)
        self.rightDoorOutput.setText("Closed")
        layout.addWidget(self.rightDoorOutput, 4, 3)

        # Adding the External Light State
        externalLightLabel = QLabel("External Lights")
        layout.addWidget(externalLightLabel, 5, 2)
        self.externalLightOutput = QLineEdit()
        self.externalLightOutput.setReadOnly(True)
        self.externalLightOutput.setText("Off")
        layout.addWidget(self.externalLightOutput, 5, 3)

        # Adding the Internal Light State
        internalLightLabel = QLabel("Internal Lights")
        layout.addWidget(internalLightLabel, 6, 2)
        self.internalLightOutput = QLineEdit()
        self.internalLightOutput.setReadOnly(True)
        self.internalLightOutput.setText("Off")
        layout.addWidget(self.internalLightOutput, 6, 3)

        # Adding the Authority
        authorityLabel = QLabel("Authority")
        layout.addWidget(authorityLabel, 7, 2)
        self.authorityOutput = QLineEdit()
        self.authorityOutput.setReadOnly(True)
        self.authorityOutput.setText("0 Blocks")
        layout.addWidget(self.authorityOutput, 7, 3)

        # Adding the Commanded Speed
        commandedSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(commandedSpeedLabel, 8, 2)
        self.commandedSpeedOutput = QLineEdit()
        self.commandedSpeedOutput.setReadOnly(True)
        self.commandedSpeedOutput.setText("0 m/s")
        layout.addWidget(self.commandedSpeedOutput, 8, 3)

        # Adding the Velocity
        velocityLabel = QLabel("Current Velocity")
        layout.addWidget(velocityLabel, 9, 2)
        self.velocityOutput = QLineEdit()
        self.velocityOutput.setReadOnly(True)
        self.velocityOutput.setText("0 m/s")
        layout.addWidget(self.velocityOutput, 9, 3)

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

        # Adding the Beacon Outputs
        beaconLabel = QLabel("Beacon Outputs")
        beaconLabel2 = QLabel("[Station State, Next Station Name, Platform Side]")
        beaconLabel2.setWordWrap(True)
        layout.addWidget(beaconLabel, 12, 2)
        layout.addWidget(beaconLabel2, 12, 3)

        # Adding the Station State
        stationStateLabel = QLabel("Station State")
        layout.addWidget(stationStateLabel, 13, 2)
        self.stationStateOutput = QLineEdit()
        self.stationStateOutput.setReadOnly(True)
        self.stationStateOutput.setText("0")
        layout.addWidget(self.stationStateOutput, 13, 3)

        # Adding the Next Station Name
        nextStationLabel = QLabel("Next Station")
        layout.addWidget(nextStationLabel, 14, 2)
        self.nextStationOutput = QLineEdit()
        self.nextStationOutput.setReadOnly(True)
        self.nextStationOutput.setText("")
        layout.addWidget(self.nextStationOutput, 14, 3)

        # Adding the Platform Side
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 15, 2)
        self.platformSideOutput = QLineEdit()
        self.platformSideOutput.setReadOnly(True)
        self.platformSideOutput.setText("Left")
        layout.addWidget(self.platformSideOutput, 15, 3)

        # Adding the Passengers Exiting
        passengersExitingLabel = QLabel("Passengers Exiting")
        layout.addWidget(passengersExitingLabel, 16, 2)
        self.passengersExitingOutput = QLineEdit()
        self.passengersExitingOutput.setReadOnly(True)
        self.passengersExitingOutput.setText("0")
        layout.addWidget(self.passengersExitingOutput, 16, 3)

        # UPDATE BUTTON FOR TESTING TO BE REMOVED
        updateButton = QPushButton("Update Values")
        updateButton.pressed.connect(self.updateOutputsBoth)
        layout.addWidget(updateButton, 21, 0, 1, 4)

    # Gets the Power input from the UI
    def getPowerInput(self):
        trainSignals.power.emit(float(self.powerInput.text()))

    # Gets the Service Brake state from the UI
    def getServiceBrakeInput(self, index):
        trainSignals.serviceBrake.emit(bool(index))
        self.testData["sBrake"] = bool(index)

    # Gets the Emergency Brake state from the UI
    def getEmergencyBrakeInput(self, index):
        trainSignals.emergencyBrake.emit(bool(index))
        self.testData["eBrakeTest"] = bool(index)
        self.testData["eBrake"] = self.testData["eBrakeUser"] | self.testData["eBrakeTest"]

    # Gets the Left Door state from the UI
    def getLeftDoorInput(self, index):
        trainSignals.leftDoors.emit()
        self.testData["lDoors"] = bool(index)

    # Gets the Right Door state from the UI
    def getRightDoorInput(self, index):
        trainSignals.rightDoors.emit()
        self.testData["rDoors"] = bool(index)

    # Gets the External Light state from the UI
    def getExternalLightInput(self, index):
        trainSignals.externalLights.emit()
        self.testData["eLights"] = bool(index)

    # Gets the Internal Light state from the UI
    def getInternalLightInput(self, index):
        trainSignals.internalLights.emit()
        self.testData["iLights"] = bool(index)

    # Gets the Station Name input from the UI
    def getStationInput(self):
        trainSignals.stationLabel.emit(self.stationInput.text())

    # Gets the Real Time Clock state from the UI
    def getRealTimeClockInput(self):
        trainSignals.realTimeClock.emit(self.realTimeClockInput.text())
        self.testData["rtc"] = self.realTimeClockInput.text()

    # Gets the Authority input from the UI
    def getAuthorityInput(self):
        self.testData["authority"] = int(self.authorityInput.text())

    # Gets the commanded speed from the UI
    def getCommandedSpeedInput(self):
        self.testData["cmdSpeed"] = float(self.commandedSpeedInput.text())

    # Gets the number of passengers entering the train from the UI
    def getPassengersEnteringInput(self):
        trainSignals.passengersEntering.emit(int(self.passengersEnteringInput.text()))

    # Gets the Block Length of the current Block from the UI
    def getBlockLengthInput(self):
        trainSignals.blockLength.emit(float(self.blockLengthInput.text()))

    # Gets the Elevation increase of the block from the UI
    def getElevationInput(self):
        trainSignals.elevation.emit(float(self.elevationInput.text()))
        
    # Gets the Speed Limit from the UI    
    def getSpeedLimitInput(self):
        self.testData["speedLimit"] = int(self.speedLimitInput.text())

    # Gets the Acceleration Limit from the UI
    def getAccelerationLimitInput(self):
        self.testData["accelLimit"] = float(self.accelerationLimitInput.text())

    # Gets the Underground state from the UI
    def getUndergroundStateInput(self, index):
        trainSignals.underground.emit()
        self.testData["underground"] = bool(index)

    # Gets the Station state from the UI
    def getStationStateInput(self, index):
        trainSignals.stationState.emit()
        self.testData["beacon"][0] = bool(index)

    # Gets the Next Station input from the UI
    def getNextStationInput(self):
        self.testData["beacon"][1] = self.nextStationInput.text()
    
    # Gets the Platform Side input from the UI
    def getPlatformSideInput(self, index):
        self.testData["beacon"][2] = index

    # Connects the velocity from the back end to the test UI
    def setCurrentVelocity(self, velocity):
        self.testData["velocity"] = velocity

    # Defines what to do when the eBrake is pulled
    def eBrakeHandler(self, index):
        self.testData["eBrakeUser"] = bool(index)
        self.testData["eBrake"] = self.testData["eBrakeTest"] | self.testData["eBrakeUser"]

    # Defines what happens when passengers off is set
    def passengersOffHandler(self, num):
        self.testData["passengersOff"] = num

    def commFailureHandler(self):
        if (self.testData["commStatus"] == True):
            self.testData["commStatus"] = False
        else:
            self.testData["commStatus"] = True

    def sBrakeFailureHandler(self):
        if (self.testData["sBrakeStatus"] == True):
            self.testData["sBrakeStatus"] = False
        else:
            self.testData["sBrakeStatus"] = True

    # Updates all functions when the button is pressed
    def updateOutputsBoth(self):
        trainSignals.updateOutputs.emit()

        self.realTimeClockOutput.setText(self.testData["rtc"])
        if self.testData["sBrakeStatus"]:
            outputText = "Engaged" if (self.testData["sBrake"] == 1) else "Disengaged"
            self.serviceBrakeOutput.setText(outputText)
        else:
            self.serviceBrakeOutput.setText("Disengaged")
        outputText = "Engaged" if (self.testData["eBrake"] == 1) else "Disengaged"
        self.emergencyBrakeOutput.setText(outputText)
        outputText = "Open" if (self.testData["lDoors"] == 1) else "Closed"
        self.leftDoorOutput.setText(outputText)
        outputText = "Open" if (self.testData["rDoors"] == 1) else "Closed"
        self.rightDoorOutput.setText(outputText)
        outputText = "On" if (self.testData["eLights"] == 1) else "Off"
        self.externalLightOutput.setText(outputText)
        outputText = "On" if (self.testData["iLights"] == 1) else "Off"
        self.internalLightOutput.setText(outputText)
        self.velocityOutput.setText(str(round(self.testData["velocity"], 2)) + " m/s")
        if self.testData["commStatus"]:
            self.authorityOutput.setText(str(self.testData["authority"]) + " Blocks")
            self.commandedSpeedOutput.setText(str(self.testData["cmdSpeed"]) + " m/s")
            self.undergroundStateOutput.setText(str(bool(self.testData["underground"])))
            self.speedLimitOutput.setText(str(self.testData["speedLimit"]) + " km/h")
            self.stationStateOutput.setText(str(self.testData["beacon"][0]))
            self.nextStationOutput.setText(self.testData["beacon"][1])
            self.platformSideOutput.setText(str(self.testData["beacon"][2]))
            self.passengersExitingOutput.setText(str(self.testData["passengersOff"]))

def main():
    app = QApplication(argv)
    testUI = TrainModelTestUI()
    testUI.show()
    mainUI = TrainModelMainUI()
    mainUI.show()
    app.exec()

if __name__ == "__main__":
    main()
