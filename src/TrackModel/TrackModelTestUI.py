# Track Model Test UI

# Import all reuired modules
from sys import argv, exit
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QGridLayout, QComboBox, QLineEdit
from TrackModelBackEnd import *
from TrackModelMainUI import TrackModelMainUI
from TrackModelSignals import *

# Class for the Track Model Test UI
class TrackModelTestUI(QWidget):

    backEnd = backEndCalculations()


    # Define an array to store block and station data
    data = {
        "line" : 0,
        "blockNo" : 0,
        "stationName" : 0,
    }

    # Define an array to store train data
    train = {
        "trainNo" : 0,
    }

    # Temp boolean
    toggle = 0

    toggleSwitch = 0
    toggleGate = 0
    toggleSignal = 0

    # Initialize the GUI
    def __init__(self):
        # Initializing the layout of the UI
        super(TrackModelTestUI, self).__init__()
        self.setWindowTitle("Track Model Test UI")
        layout = QGridLayout()
        self.setLayout(layout)

        # Setting up all the inputs

        # Add the Line
        lineLabel = QLabel("Line")
        layout.addWidget(lineLabel, 0, 0)
        self.lineInput = QComboBox()
        self.lineInput.addItems(["Red", "Green"])
        self.lineInput.currentIndexChanged.connect(self.getLineInput)
        self.lineInput.currentIndexChanged.connect(self.lineChange)
        layout.addWidget(self.lineInput, 0, 1)

        # Add the Block Number
        blockLabel = QLabel("Block Number")
        layout.addWidget(blockLabel, 1, 0)
        self.blockInput = QComboBox()
        i = 0
        while i < int(self.backEnd.csvConstants["redBlocks"].__len__()):
            self.blockInput.addItem(self.backEnd.csvConstants["redBlocks"].__getitem__(i))
            i += 1
        self.blockInput.currentIndexChanged.connect(self.getBlockInput)
        self.blockInput.currentIndexChanged.connect(self.blockChange)
        layout.addWidget(self.blockInput, 1, 1)

        # Add the Switch Position
        switchPositionLabel = QLabel("Switch Position") # Creates label
        layout.addWidget(switchPositionLabel, 2, 0) # Posts label to the UI
        self.switchPositionInput = QComboBox() # Creates combo box
        self.switchPositionInput.currentIndexChanged.connect(self.getSwitchPositionInput) # Calls function if combo box modified
        layout.addWidget(self.switchPositionInput, 2, 1) # Posts combo box to UI
        self.switchPositionInput.setEnabled(False)

        # Add the Gate Position
        gatePositionLabel = QLabel("Gate Position")

        layout.addWidget(gatePositionLabel, 3, 0)
        self.gatePositionInput = QComboBox()
        self.gatePositionInput.currentIndexChanged.connect(self.getGatePositionInput)
        layout.addWidget(self.gatePositionInput, 3, 1)
        self.gatePositionInput.setEnabled(False)

        # Add the Signal State
        signalStateLabel = QLabel("Signal State")

        layout.addWidget(signalStateLabel, 4, 0)
        self.signalStateInput = QComboBox()
        self.signalStateInput.addItems(["Green", "Yellow", "Red"])
        self.signalStateInput.currentIndexChanged.connect(self.getSignalStateInput)
        layout.addWidget(self.signalStateInput, 4, 1)

        # Add the Temperature
        tempLabel = QLabel("Temperature Input")
        layout.addWidget(tempLabel, 18, 0)
        self.tempInput = QLineEdit()
        self.tempInput.editingFinished.connect(self.getTempInput)
        layout.addWidget(self.tempInput, 18, 1)

        # Add the Track Heater
        trackHeaterLabel = QLabel("Track Heater")
        layout.addWidget(trackHeaterLabel, 19, 0)
        self.trackHeaterInput = QComboBox()
        self.trackHeaterInput.addItems(["Off", "On"])
        self.trackHeaterInput.currentIndexChanged.connect(self.getTrackHeaterInput)
        layout.addWidget(self.trackHeaterInput, 19, 1)

        # Add border
        layout.addWidget(QLabel(" "), 6, 0)
        layout.addWidget(QLabel(" "), 17, 0)

        # Add the Station Name
        stationNameLabel = QLabel("Station Name")
        layout.addWidget(stationNameLabel, 7, 0)
        self.stationNameInput = QComboBox()

        i = 0
        while i < int(self.backEnd.csvConstants["stationName"].__len__()):
            self.stationNameInput.addItem(self.backEnd.csvConstants["stationName"].__getitem__(i))
            i += 1
        self.stationNameInput.currentIndexChanged.connect(self.getStationNameInput)
        layout.addWidget(self.stationNameInput, 7, 1)

        # Add Station Occupancy
        stationOccLabel = QLabel("Station Occupancy")
        layout.addWidget(stationOccLabel, 8, 0)
        self.stationOccInput = QLineEdit()
        self.stationOccInput.editingFinished.connect(self.getStationOccInput)
        layout.addWidget(self.stationOccInput, 8, 1)

        # Add Passengers On
        onLabel = QLabel("Passengers On")
        layout.addWidget(onLabel, 9, 0)
        self.onInput = QLineEdit()
        self.onInput.editingFinished.connect(self.getOnInput)
        layout.addWidget(self.onInput, 9, 1)
        
        # Add border
        layout.addWidget(QLabel(" "), 10, 0)


        # Add the Train Line
        trainLnLabel = QLabel("Train Line")
        layout.addWidget(trainLnLabel, 12, 0)
        self.trainLnInput = QComboBox()
        self.trainLnInput.addItems(["Red", "Green"])
        self.trainLnInput.currentIndexChanged.connect(self.getTrainLnInput)
        layout.addWidget(self.trainLnInput, 12, 1)

        # Add the Train Number
        trainLabel = QLabel("Train Number")
        layout.addWidget(trainLabel, 11, 0)
        self.trainInput = QComboBox()

        self.trainInput.addItems(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
        "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"])
        self.trainInput.currentIndexChanged.connect(self.getTrainInput)
        self.trainInput.currentIndexChanged.connect(self.trainChange)
        layout.addWidget(self.trainInput, 11, 1)

        # Add the train block
        trainBlockLabel = QLabel("Train Block")

        layout.addWidget(trainBlockLabel, 13, 0)
        self.trainBlockInput = QComboBox()
        self.trainBlockInput.addItem("Yard")
        self.trainBlockInput.currentIndexChanged.connect(self.getTrainBlockInput)
        layout.addWidget(self.trainBlockInput, 13, 1)

        # Add Passengers Off
        offLabel = QLabel("Passengers Off")
        layout.addWidget(offLabel, 14, 0)
        self.offInput = QLineEdit()
        self.offInput.editingFinished.connect(self.getOffInput)
        layout.addWidget(self.offInput, 14, 1)

        # Add Authority
        authLabel = QLabel("Authority")
        layout.addWidget(authLabel, 15, 0)
        self.authInput = QLineEdit()
        self.authInput.editingFinished.connect(self.getAuthInput)
        layout.addWidget(self.authInput, 15, 1)

        # Add Commanded Speed
        cSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(cSpeedLabel, 16, 0)
        self.cSpeedInput = QLineEdit()
        self.cSpeedInput.editingFinished.connect(self.getCSpeedInput)
        layout.addWidget(self.cSpeedInput, 16, 1)

        # Add the Real Time Clock Input
        realTimeClockLabel = QLabel("Real Time Clock")
        layout.addWidget(realTimeClockLabel, 20, 0)
        self.realTimeClockInput = QLineEdit()
        self.realTimeClockInput.editingFinished.connect(self.getRealTimeClockInput)
        layout.addWidget(self.realTimeClockInput, 20, 1)

        # Setting up all the outputs

        # Adding the Line
        lineLabel = QLabel("Line")
        layout.addWidget(lineLabel, 0, 2)
        self.lineOutput = QLineEdit()
        self.lineOutput.setReadOnly(True)
        self.lineOutput.setText("Red")
        layout.addWidget(self.lineOutput, 0, 3)

        # Adding the Block Number
        blockLabel = QLabel("Block Number")
        layout.addWidget(blockLabel, 1, 2)
        self.blockNumberOutput = QLineEdit()
        self.blockNumberOutput.setReadOnly(True)
        self.blockNumberOutput.setText("1")
        layout.addWidget(self.blockNumberOutput, 1, 3)

        # Adding the Switch Position State
        switchPositionLabel = QLabel("Switch Position") # Creates label
        layout.addWidget(switchPositionLabel, 2, 2) # Posts label to UI
        self.switchPositionOutput = QLineEdit() # Creates value box
        self.switchPositionOutput.setReadOnly(True) # Prevent user from changing value in value box
        self.switchPositionOutput.setText("N/A") # Sets the initial value in output
        layout.addWidget(self.switchPositionOutput, 2, 3) # Posts value box to UI

        # Adding the Gate Position State
        gatePositionLabel = QLabel("Gate Position")
        layout.addWidget(gatePositionLabel, 3, 2)
        self.gatePositionOutput = QLineEdit()
        self.gatePositionOutput.setReadOnly(True)
        self.gatePositionOutput.setText("N/A")
        layout.addWidget(self.gatePositionOutput, 3, 3)

        # Adding the Signal State
        signalStateLabel = QLabel("Signal State")
        layout.addWidget(signalStateLabel, 4, 2)
        self.signalStateOutput = QLineEdit()
        self.signalStateOutput.setReadOnly(True)
        self.signalStateOutput.setText("Green")
        layout.addWidget(self.signalStateOutput, 4, 3)

        # Adding the block train number
        blockTrainLabel = QLabel("Block Train Number")
        layout.addWidget(blockTrainLabel, 5, 2)
        self.blockTrainOutput = QLineEdit()
        self.blockTrainOutput.setReadOnly(True)
        self.blockTrainOutput.setText("0")
        layout.addWidget(self.blockTrainOutput, 5, 3)

        # Adding the Temperature
        tempLabel = QLabel("Current Temperature")

        layout.addWidget(tempLabel, 18, 2)
        self.tempOutput = QLineEdit()
        self.tempOutput.setReadOnly(True)
        self.tempOutput.setText("70.0 degrees F")
        layout.addWidget(self.tempOutput, 18, 3)

        # Adding the Track Heater
        trackHeaterLabel = QLabel("Track Heater")
        layout.addWidget(trackHeaterLabel, 19, 2)
        self.trackHeaterOutput = QLineEdit()
        self.trackHeaterOutput.setReadOnly(True)
        self.trackHeaterOutput.setText("Off")
        layout.addWidget(self.trackHeaterOutput, 19, 3)

        # Adding the Station Name
        stationNameLabel = QLabel("Station Name")
        layout.addWidget(stationNameLabel, 7, 2)
        self.stationNameOutput = QLineEdit()
        self.stationNameOutput.setReadOnly(True)

        self.stationNameOutput.setText(self.backEnd.csvConstants["stationName"].__getitem__(0))
        layout.addWidget(self.stationNameOutput, 7, 3)

        # Adding the Station Occupancy
        occLabel = QLabel("Station Occupancy")
        layout.addWidget(occLabel, 8, 2)
        self.occOutput = QLineEdit()
        self.occOutput.setReadOnly(True)
        self.occOutput.setText("0 people")
        layout.addWidget(self.occOutput, 8, 3)
        
        # Adding the train line
        trainLnLabel = QLabel("Train Line")
        layout.addWidget(trainLnLabel, 12, 2)
        self.trainLnOutput = QLineEdit()
        self.trainLnOutput.setReadOnly(True)
        self.trainLnOutput.setText("Red")
        layout.addWidget(self.trainLnOutput, 12, 3)
        
        # Adding the train number
        trainLabel = QLabel("Train Number")
        layout.addWidget(trainLabel, 11, 2)
        self.trainNumberOutput = QLineEdit()
        self.trainNumberOutput.setReadOnly(True)
        self.trainNumberOutput.setText("1")
        layout.addWidget(self.trainNumberOutput, 11, 3)

        # Adding the train block
        trainBlockLabel = QLabel("Train Block")
        layout.addWidget(trainBlockLabel, 13, 2)
        self.trainBlockOutput = QLineEdit()
        self.trainBlockOutput.setReadOnly(True)
        self.trainBlockOutput.setText("Yard")
        layout.addWidget(self.trainBlockOutput, 13, 3)

        # Adding the passenger count
        numPassengersLabel = QLabel("Number of Passengers")
        layout.addWidget(numPassengersLabel, 14, 2)
        self.numPassengersOutput = QLineEdit()
        self.numPassengersOutput.setReadOnly(True)
        self.numPassengersOutput.setText("0 people")
        layout.addWidget(self.numPassengersOutput, 14, 3)

        # Adding the Authority
        authLabel = QLabel("Authority")
        layout.addWidget(authLabel, 15, 2)
        self.authOutput = QLineEdit()
        self.authOutput.setReadOnly(True)
        self.authOutput.setText("0 blocks")
        layout.addWidget(self.authOutput, 15, 3)

        # Adding the Commanded Speed
        cSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(cSpeedLabel, 16, 2)
        self.cSpeedOutput = QLineEdit()
        self.cSpeedOutput.setReadOnly(True)
        self.cSpeedOutput.setText("0 MPH")
        layout.addWidget(self.cSpeedOutput, 16, 3)

        # Adding the Real Time Clock
        realTimeClockLabel = QLabel("Real Time Clock")
        layout.addWidget(realTimeClockLabel, 20, 2)
        self.realTimeClockOutput = QLineEdit()
        self.realTimeClockOutput.setReadOnly(True)
        self.realTimeClockOutput.setText("00:00:00")
        layout.addWidget(self.realTimeClockOutput, 20, 3)

    # Gets the Line from the UI
    def getLineInput(self, index):
        self.data["line"] = index
        outputText = "Green" if self.data["line"] == 1 else "Red"
        self.lineOutput.setText(outputText)

    # Gets the Block Number from the UI
    def getBlockInput(self, index):
        self.data["blockNo"] = index
        outputText = str(self.data["blockNo"] + 1)
        self.blockNumberOutput.setText(outputText)
    
    # Gets the Switch Position from the UI
    def getSwitchPositionInput(self, index):
        if self.toggleSwitch != 1:
            trackSignals.getSwitchPositionInput.emit(index, self.data["line"], self.data["blockNo"])

        if self.data["line"] == 0:
            if int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) > 0 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)) == 0 and self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1) == 1:
                outputText = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)) + "-Yard"
            else:
                outputText = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)) if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1) == 1 else str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1))
        elif self.data["line"] == 1:
            if int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) > 0 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)) == 0 and self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1) == 1:
                outputText = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)) + "-Yard"
            else:
                outputText = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)) if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1) == 1 else str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1))
        self.switchPositionOutput.setText(outputText) # Put output text in value box

        self.updateCombo()

    # Gets the Gate Position state from the UI
    def getGatePositionInput(self, index):
        if self.toggleGate != 1:
            trackSignals.getGatePositionInput.emit(index, self.data["line"], self.data["blockNo"])
        
        if self.data["line"] == 0:
            outputText = "Down" if self.backEnd.data["gatePos"].__getitem__(int(self.backEnd.csvConstants["crossingRed"].__getitem__(self.data["blockNo"])) - 1) == 1 else "Up"
        elif self.data["line"] == 1:
            outputText = "Down" if self.backEnd.data["gatePos"].__getitem__(int(self.backEnd.csvConstants["crossingGreen"].__getitem__(self.data["blockNo"])) - 1) == 1 else "Up"
        self.gatePositionOutput.setText(outputText)

    # Gets the Signal State from the UI
    def getSignalStateInput(self, index):
        if self.toggleSignal != -1:
            trackSignals.getSignalStateInput.emit(index, self.data["line"], self.data["blockNo"])

        if self.data["line"] == 0 and self.data["blockNo"] != -1:
            if self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.data["blockNo"])) - 1) == 2:
                outputText = "Red"
            elif self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.data["blockNo"])) - 1) == 1:
                outputText = "Yellow"
            else:
                outputText = "Green"
            self.signalStateOutput.setText(outputText)
        elif self.data["line"] == 1 and self.data["blockNo"] != -1:
            if self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.data["blockNo"])) - 1) == 2:
                outputText = "Red"
            elif self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.data["blockNo"])) - 1) == 1:
                outputText = "Yellow"
            else:
                outputText = "Green"
            self.signalStateOutput.setText(outputText)

    # Gets Signal State if block changes
    def blockChange(self, index):
        # Set new switch states
        self.toggleSwitch = 1
        if self.data["line"] == 0 and index != -1 and int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) > 0 and index + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)):
            if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) != 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1))
            elif self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) == 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-Yard"
            else:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1))
            self.switchPositionInput.setEnabled(True)
            self.switchPositionOutput.setText(outputText1)

            i = self.switchPositionInput.count() - 1
            while i >= 0:
                self.switchPositionInput.removeItem(i)
                i -= 1

            self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)))
            if int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) != 0:
                self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)))
            elif int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) == 0:
                self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-Yard")
            self.switchPositionInput.setCurrentText(outputText1)

        elif self.data["line"] == 1 and index != -1 and int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) > 0 and index + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)):
            if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) != 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1))
            elif self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) == 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-Yard"
            else:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1))
            self.switchPositionInput.setEnabled(True)
            self.switchPositionOutput.setText(outputText1)

            i = self.switchPositionInput.count() - 1
            while i >= 0:
                self.switchPositionInput.removeItem(i)
                i -= 1

            self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)))
            if int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) != 0:
                self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)))
            elif int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) == 0:
                self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-Yard")
            self.switchPositionInput.setCurrentText(outputText1)
        else:
            i = self.switchPositionInput.count() - 1
            while i >= 0:
                self.switchPositionInput.removeItem(i)
                i -= 1
            self.switchPositionInput.setEnabled(False)
            self.switchPositionOutput.setText("N/A")
        self.toggleSwitch = 0

        # Set new gates
        self.toggleGate = 1
        if self.data["line"] == 0 and index != -1 and int(self.backEnd.csvConstants["crossingRed"].__getitem__(index)) > 0:
            outputText1 = "Down" if self.backEnd.data["gatePos"].__getitem__(int(self.backEnd.csvConstants["crossingRed"].__getitem__(index)) - 1) == 1 else "Up"
            self.gatePositionInput.setEnabled(True)
            self.gatePositionOutput.setText(outputText1)

            i = self.gatePositionInput.count() - 1
            while i >= 0:
                self.gatePositionInput.removeItem(i)
                i -= 1

            self.gatePositionInput.addItems(["Up", "Down"])
            self.gatePositionInput.setCurrentText(outputText1)
        elif self.data["line"] == 1 and index != -1 and int(self.backEnd.csvConstants["crossingGreen"].__getitem__(index)) > 0:
            outputText1 = "Down" if self.backEnd.data["gatePos"].__getitem__(int(self.backEnd.csvConstants["crossingGreen"].__getitem__(index)) - 1) == 1 else "Up"
            self.gatePositionInput.setEnabled(True)
            self.gatePositionOutput.setText(outputText1)

            i = self.gatePositionInput.count() - 1
            while i >= 0:
                self.gatePositionInput.removeItem(i)
                i -= 1

            self.gatePositionInput.addItems(["Up", "Down"])
            self.gatePositionInput.setCurrentText(outputText1)
        else:
            i = self.gatePositionInput.count() - 1
            while i >= 0:
                self.gatePositionInput.removeItem(i) 
                i -= 1
            self.gatePositionInput.setEnabled(False)
            self.gatePositionOutput.setText("N/A")
        self.toggleGate = 0

        # Set new signals
        self.toggleSignal = 1
        if self.data["line"] == 0 and index != -1 and int(self.backEnd.csvConstants["signalRed"].__getitem__(index)) > 0:
            if self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.data["blockNo"])) - 1) == 2:
                outputText1 = "Red"
            elif self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.data["blockNo"])) - 1) == 1:
                outputText1 = "Yellow"
            else:
                outputText1 = "Green"
            self.signalStateInput.setEnabled(True)
            self.signalStateOutput.setText(outputText1)

            i = self.signalStateInput.count() - 1
            while i >= 0:
                self.signalStateInput.removeItem(i)
                i -= 1

            self.signalStateInput.addItems(["Green", "Yellow", "Red"])
            self.signalStateInput.setCurrentText(outputText1)
        elif self.data["line"] == 1 and index != -1 and int(self.backEnd.csvConstants["signalGreen"].__getitem__(index)) > 0:
            if self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.data["blockNo"])) - 1) == 2:
                outputText1 = "Red"
            elif self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.data["blockNo"])) - 1) == 1:
                outputText1 = "Yellow"
            else:
                outputText1 = "Green"
            self.signalStateInput.setEnabled(True)
            self.signalStateOutput.setText(outputText1)

            i = self.signalStateInput.count() - 1
            while i >= 0:
                self.signalStateInput.removeItem(i)
                i -= 1

            self.signalStateInput.addItems(["Green", "Yellow", "Red"])
            self.signalStateInput.setCurrentText(outputText1)
        else:
            i = self.signalStateInput.count() - 1
            while i >= 0:
                self.signalStateInput.removeItem(i)
                i -= 1
            self.signalStateInput.setEnabled(False)
            self.signalStateOutput.setText("N/A")
        self.toggleSignal = 0

        # Set new block train number
        if self.data["line"] == 0:
            self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNoRed"].__getitem__(self.data["blockNo"])))
        elif self.data["line"] == 1:
            self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNoGreen"].__getitem__(self.data["blockNo"])))

    # Gets Signal State if line changes
    def lineChange(self, index):
        # Set new combo box values
        self.data["blockNo"] = 0
        i = self.blockInput.count() - 1
        while i >= 0:
                self.blockInput.removeItem(i)
                i -= 1
        i = 0
        if index == 0:
            while i < int(self.backEnd.csvConstants["redBlocks"].__len__()):
                self.blockInput.addItem(self.backEnd.csvConstants["redBlocks"].__getitem__(i))
                i += 1
        elif index == 1:
            while i < int(self.backEnd.csvConstants["greenBlocks"].__len__()):
                self.blockInput.addItem(self.backEnd.csvConstants["greenBlocks"].__getitem__(i))
                i += 1

        # Set Block number equal to one
        self.blockNumberOutput.setText("1")
        self.blockInput.setCurrentText("1")
        self.blockChange(0)
        

    # Gets the Temperature from the UI
    def getTempInput(self):
        trackSignals.getTempInput.emit(float(self.tempInput.text()))
        self.tempOutput.setText(str(self.backEnd.data["temp"]) + " degrees F")

        # Configure Track Heaters
        if self.backEnd.data["temp"] > 32:
            self.trackHeaterOutput.setText("Off")
            self.trackHeaterInput.setCurrentText("Off")
        elif self.backEnd.data["temp"] < 32:
            self.trackHeaterOutput.setText("On")
            self.trackHeaterInput.setCurrentText("On")
    
    # Gets the Track Heater state from the UI
    def getTrackHeaterInput(self, index):
        trackSignals.getTrackHeaterInput.emit(index)
        outputText = "On" if self.backEnd.data["trackHeater"] == 1 else "Off"
        self.trackHeaterOutput.setText(outputText)

    # Gets the Station Name from the UI
    def getStationNameInput(self, index):
        self.data["stationName"] = index
        outputText = self.backEnd.csvConstants["stationName"].__getitem__(self.data["stationName"])
        self.stationNameOutput.setText(outputText)

        # Set new station occupancy
        if self.backEnd.data["stationOccupancy"].__getitem__(index) == 1:
            outputText1  = "1 person"
        else:
            outputText1 = str(self.backEnd.data["stationOccupancy"].__getitem__(index)) + " people"
        self.occOutput.setText(outputText1)

    # Gets the Station Occupancy from the UI
    def getStationOccInput(self):
        trackSignals.getStationOccInput.emit(int(self.stationOccInput.text()))
        if self.backEnd.data["stationOccupancy"].__getitem__(self.data["stationName"]) == 1:
            self.occOutput.setText("1 person")
        else:
            self.occOutput.setText(str(self.backEnd.data["stationOccupancy"].__getitem__(self.data["stationName"])) + " people")

    # Gets the Train Number from the UI
    def getTrainInput(self, index):
        self.train["trainNo"] = index
        outputText = str(self.train["trainNo"] + 1)
        self.trainNumberOutput.setText(outputText)

    # Gets the Train Block from the UI
    def getTrainBlockInput(self, index):
        # Update block train number
        if self.toggle != 1:
            trackSignals.getTrainBlockInputSignal.emit(index, self.train["trainNo"])

            # Display new train block
            if self.backEnd.data["moves"][self.train["trainNo"]][index] != 0:
                if self.backEnd.data["trainLine"][self.train["trainNo"]] == 0:
                    self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNoRed"].__getitem__(self.train["trainNo"])))
                elif self.backEnd.data["trainLine"][self.train["trainNo"]] == 1:
                    self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNoGreen"].__getitem__(self.train["trainNo"])))
            else:
                self.blockTrainOutput.setText("Yard")
   
            # Update Authority
            if self.backEnd.data["authority"][self.train["trainNo"]] == 1:
                self.authOutput.setText("1 block")
            else:
                self.authOutput.setText(str(self.backEnd.data["authority"][self.train["trainNo"]]) + " blocks")

            # Update train block output
            if self.backEnd.data["trainBlock"][self.train["trainNo"]] == 0:
                outputText  = "Yard"
            else:
                outputText = str(self.backEnd.data["trainBlock"][self.train["trainNo"]])
            self.trainBlockOutput.setText(outputText)

            # Update train block combo box
            self.updateCombo()

            # Disable line change if not at yard
            if self.backEnd.data["moves"][self.train["trainNo"]][0] > 0:
                self.trainLnInput.setEnabled(False)
            elif self.backEnd.data["moves"][self.train["trainNo"]][0] == 0:
                self.trainLnInput.setEnabled(True)

            # Update the block train number
            if self.data["line"] == 0:
                self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNoRed"].__getitem__(self.data["blockNo"])))
            elif self.data["line"] == 1:
                self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNoGreen"].__getitem__(self.data["blockNo"])))

    # Gets new data if train line changes
    def getTrainLnInput(self, index):
        trackSignals.getTrainLnInput.emit(index, self.train["trainNo"])
        outputText = "Green" if self.backEnd.data["trainLine"][self.train["trainNo"]] == 1 else "Red"
        self.trainLnOutput.setText(outputText)
        self.updateCombo()

    # Gets new data if train changes
    def trainChange(self, index):
        self.toggle = 1
        # Set new train block
        if self.backEnd.data["trainBlock"][index] == 0:
            outputText  = "Yard"
        else:
            outputText = str(self.backEnd.data["trainBlock"][index])
        self.trainBlockOutput.setText(outputText)
        self.backEnd.data["moves"][self.train["trainNo"]][0] = self.backEnd.data["trainBlock"][index]
        self.backEnd.updateVector(self.train["trainNo"])
        self.updateCombo()
        self.toggle = 0

        # Disable line change if not at yard
        if self.backEnd.data["moves"][self.train["trainNo"]][0] > 0:
            self.trainLnInput.setEnabled(False)
        elif self.backEnd.data["moves"][self.train["trainNo"]][0] == 0:
            self.trainLnInput.setEnabled(True)

        # Update Passenger Count
        if self.backEnd.data["numPassengers"][self.train["trainNo"]] == 1:
            self.numPassengersOutput.setText("1 person")
        else:
            self.numPassengersOutput.setText(str(self.backEnd.data["numPassengers"][self.train["trainNo"]]) + " people")

        # Update Authority
        if self.backEnd.data["authority"][self.train["trainNo"]] == 1:
            self.authOutput.setText("1 block")
        else:
            self.authOutput.setText(str(self.backEnd.data["authority"][self.train["trainNo"]]) + " blocks")

        # Update Commanded Speed
        self.cSpeedOutput.setText(str(self.backEnd.data["commandedSpeed"][self.train["trainNo"]]) + " MPH")

    # Gets the number of passengers off from the UI
    def getOffInput(self):
        trackSignals.getOffInput.emit(self.train["trainNo"], self.data["stationName"], int(self.offInput.text()))

        if self.backEnd.data["numPassengers"][self.train["trainNo"]] == 1:
            self.numPassengersOutput.setText("1 person")
        else:
            self.numPassengersOutput.setText(str(self.backEnd.data["numPassengers"][self.train["trainNo"]]) + " people")

    # Gets the number of passengers on from the UI
    def getOnInput(self):
        trackSignals.getOnInput.emit(self.data["stationName"], int(self.onInput.text()))

        if int(self.backEnd.data["stationOccupancy"].__getitem__(self.data["stationName"])) == 1:
            self.occOutput.setText("1 person")
        else:
            self.occOutput.setText(str(self.backEnd.data["stationOccupancy"].__getitem__(self.data["stationName"])) + " people")

        if self.backEnd.data["numPassengers"][self.train["trainNo"]] == 1:
            self.numPassengersOutput.setText("1 person")
        else:
            self.numPassengersOutput.setText(str(self.backEnd.data["numPassengers"][self.train["trainNo"]]) + " people")

    # Gets the authority input from the UI
    def getAuthInput(self):
        trackSignals.getAuthInput.emit(int(self.authInput.text()), self.train["trainNo"])

        if self.backEnd.data["authority"][self.train["trainNo"]] == 1:
            self.authOutput.setText("1 block")
        else:
            self.authOutput.setText(str(self.backEnd.data["authority"][self.train["trainNo"]]) + " blocks")

    # Gets the commanded speed input from the UI
    def getCSpeedInput(self):
        trackSignals.getCSpeedInput.emit(int(self.cSpeedInput.text()), self.train["trainNo"])
        self.cSpeedOutput.setText(str(self.backEnd.data["commandedSpeed"][self.train["trainNo"]]) + " MPH")

    # Gets the Real Time Clock state from the UI
    def getRealTimeClockInput(self):
        trackSignals.getRealTimeClockInput.emit(self.realTimeClockInput.text())
        self.realTimeClockOutput.setText(self.backEnd.data["rtc"])

    def updateCombo(self):
        self.toggle = 1
        i = self.trainBlockInput.count() - 1
        while i >= 0:
            self.trainBlockInput.removeItem(i)
            i -= 1

        if self.backEnd.data["moves"][self.train["trainNo"]][0] == 0:
            self.trainBlockInput.addItem("Yard")
        else:
            self.trainBlockInput.addItem(str(self.backEnd.data["moves"][self.train["trainNo"]][0]))
        if self.backEnd.data["moves"][self.train["trainNo"]][1] != None:
            if self.backEnd.data["moves"][self.train["trainNo"]][1] == 0:
                self.trainBlockInput.addItem("Yard")
            else:
                self.trainBlockInput.addItem(str(self.backEnd.data["moves"][self.train["trainNo"]][1]))
        if self.backEnd.data["moves"][self.train["trainNo"]][2] != None:
            if self.backEnd.data["moves"][self.train["trainNo"]][2] == 0:
                self.trainBlockInput.addItem("Yard")
            else:
                self.trainBlockInput.addItem(str(self.backEnd.data["moves"][self.train["trainNo"]][2]))
        self.toggle = 0

    # Returns all the data in the inputData Array
    def getData(self):
        return self.data

def main():
    app = QApplication(argv)
    testUI = TrackModelTestUI()
    testUI.show()
    mainUI = TrackModelMainUI()
    mainUI.show()
    app.exit(app.exec())

if __name__ == "__main__":
    main()
