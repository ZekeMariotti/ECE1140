# Train Model Test UI

# Importing all required modules
from sys import argv, exit
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QGridLayout, QComboBox, QLineEdit
from TrainModelMainUI import *
from TrainModelSignals import *
# Class for the Train Model Test UI
class TrainModelTestUI(QWidget):

    # Define an Array to store UI data
    data = {
        "pwr" : 0.0, 
        "sBrake" : 0,
        "eBrake" : 0,
        "lDoors" : 0,
        "rDoors" : 0,
        "eLights" : 0,
        "iLights" : 0,
        "station" : "",
        "rtc" : "",
        "authority" : 0,
        "cmdSpeed" : 0.0,
        "passEnter" : 0,
        "blockLength" : 0.0,
        "elevation" : 0.0,
        "speedLimit" : 0,
        "accelLimit" : 0.0,
        "underground" : 0,
        "beacon" : [0, "", 0], # [Station State, Next Station Name, Platform Side]
        "curr" : [0.0, 0.0], # Current Velocity and Acceleration
        "prev" : [0.0, 0.0], # Previous Velocity and Acceleration
        "mass" : 37103.8665}

    # Initialize the GUI
    def __init__(self):
        # Initializing the layout of the UI
        super(TrainModelTestUI, self).__init__()
        self.setWindowTitle("Train Model Test UI")
        layout = QGridLayout()
        self.setLayout(layout)

        # Setting up all the inputs
        # Add the Power Input
        powerLabel = QLabel("Power Input")
        layout.addWidget(powerLabel, 0, 0)
        self.powerInput = QLineEdit()
        self.powerInput.editingFinished.connect(self.getPowerInput)
        layout.addWidget(self.powerInput, 0, 1)

        #self.PowerSignal = pyqtSignal(boolean power)
        #self.PowerSignal.emit(self.power)

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
        self.realTimeClockOutput.setText("00:00:00")
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

    # Gets the Power input from the UI
    def getPowerInput(self):
        self.data["pwr"] = float(self.powerInput.text())
        self.data["prev"] = self.data["curr"]
    # Gets the Service Brake state from the UI
    def getServiceBrakeInput(self, index):
        self.data["sBrake"] = index
        outputText = "Engaged" if self.data["sBrake"] == 1 else "Disengaged"
        self.serviceBrakeOutput.setText(outputText)

    # Gets the Emergency Brake state from the UI
    def getEmergencyBrakeInput(self, index):
        self.data["eBrake"] = index
        outputText = "Engaged" if self.data["eBrake"] == 1 else "Disengaged"
        self.emergencyBrakeOutput.setText(outputText)

    # Gets the Left Door state from the UI
    def getLeftDoorInput(self, index):
        self.data["lDoors"] = index
        outputText = "Open" if self.data["lDoors"] == 1 else "Closed"
        self.leftDoorOutput.setText(outputText)

    # Gets the Right Door state from the UI
    def getRightDoorInput(self, index):
        self.data["rDoors"] = index
        outputText = "Open" if self.data["rDoors"] == 1 else "Closed"
        self.rightDoorOutput.setText(outputText)

    # Gets the External Light state from the UI
    def getExternalLightInput(self, index):
        self.data["eLights"] = index
        outputText = "On" if self.data["eLights"] == 1 else "Off"
        self.externalLightOutput.setText(outputText)

    # Gets the Internal Light state from the UI
    def getInternalLightInput(self, index):
        self.data["iLights"] = index
        outputText = "On" if self.data["iLights"] == 1 else "Off"
        self.internalLightOutput.setText(outputText)

    # Gets the Station Name input from the UI
    def getStationInput(self):
        self.data["station"] = self.stationInput.text()

    # Gets the Real Time Clock state from the UI
    def getRealTimeClockInput(self):
        self.data["rtc"] = self.realTimeClockInput.text()
        self.realTimeClockOutput.setText(self.data["rtc"])

    # Gets the Authority input from the UI
    def getAuthorityInput(self):
        self.data["authority"] = int(self.authorityInput.text())
        self.authorityOutput.setText(str(self.data["authority"]) + " Blocks")

    # Gets the commanded speed from the UI
    def getCommandedSpeedInput(self):
        self.data["cmdSpeed"] = float(self.commandedSpeedInput.text())
        self.commandedSpeedOutput.setText(str(self.data["cmdSpeed"]) + " m/s")

    # Gets the number of passengers entering the train from the UI
    def getPassengersEnteringInput(self):
        self.data["passEnter"] = int(self.passengersEnteringInput.text())

    # Gets the Block Length of the current Block from the UI
    def getBlockLengthInput(self):
        self.data["blockLength"] = float(self.blockLengthInput.text())

    # Gets the Elevation increase of the block from the UI
    def getElevationInput(self):
        self.data["elevation"] = float(self.elevationInput.text())
        
    # Gets the Speed Limit from the UI    
    def getSpeedLimitInput(self):
        self.data["speedLimit"] = int(self.speedLimitInput.text())
        self.speedLimitOutput.setText(str(self.data["speedLimit"]) + " km/h")

    # Gets the Acceleration Limit from the UI
    def getAccelerationLimitInput(self):
        self.data["accelLimit"] = float(self.accelerationLimitInput.text())

    # Gets the Underground state from the UI
    def getUndergroundStateInput(self, index):
        self.data["underground"] = index
        self.undergroundStateOutput.setText(str(self.data["underground"]))

    # Gets the Station state from the UI
    def getStationStateInput(self, index):
        self.data["beacon"][0] = index
        self.stationStateOutput.setText(str(self.data["beacon"][0]))

    # Gets the Next Station input from the UI
    def getNextStationInput(self):
        self.data["beacon"][1] = self.nextStationInput.text()
        self.nextStationOutput.setText(self.data["beacon"][1])
    
    # Gets the Platform Side input from the UI
    def getPlatformSideInput(self, index):
        self.data["beacon"][2] = index
        if self.data["beacon"][2] == 0:
            outputText = "Left"
        elif self.data["beacon"][2] == 1:
            outputText = "Right"
        else:
            outputText = "Both"
        self.platformSideOutput.setText(outputText)

    def main():
        app = QApplication(argv)
        form = TrainModelTestUI()
        form.show()
        app.exec()
        print(form.data)

if __name__ == "__main__":
    TrainModelTestUI.main()
