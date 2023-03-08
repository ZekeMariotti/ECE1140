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
        "trainBlock" : [0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0],
    }

    # Temp boolean
    toggle = 0
    toggleSwitch = 0
    toggleGate = 0

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
        self.gatePositionInput.addItems(["Up", "Down"])
        self.gatePositionInput.currentIndexChanged.connect(self.getGatePositionInput)
        layout.addWidget(self.gatePositionInput, 3, 1)
        self.gatePositionInput.setEnabled(False)

        # Add the Signal State
        signalStateLabel = QLabel("Signal State")
        layout.addWidget(signalStateLabel, 4, 0)
        self.signalStateInput = QComboBox()
        self.signalStateInput.addItems(["Red", "Yellow", "Green"])
        self.signalStateInput.currentIndexChanged.connect(self.getSignalStateInput)
        layout.addWidget(self.signalStateInput, 4, 1)

        # Add the Track Direction
        directionLabel = QLabel("Track Direction")
        layout.addWidget(directionLabel, 5, 0)
        self.directionInput = QComboBox()
        self.directionInput.addItems(["Eastbound", "Westbound"])
        self.directionInput.currentIndexChanged.connect(self.getDirectionInput)
        layout.addWidget(self.directionInput, 5, 1)

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
        layout.addWidget(QLabel(" "), 7, 0)
        layout.addWidget(QLabel(" "), 17, 0)

        # Add the Station Name
        stationNameLabel = QLabel("Station Name")
        layout.addWidget(stationNameLabel, 8, 0)
        self.stationNameInput = QComboBox()
        self.stationNameInput.addItems(["Station B", "Station C"])
        self.stationNameInput.currentIndexChanged.connect(self.getStationNameInput)
        layout.addWidget(self.stationNameInput, 8, 1)

        # Add Station Occupancy
        stationOccLabel = QLabel("Station Occupancy")
        layout.addWidget(stationOccLabel, 9, 0)
        self.stationOccInput = QLineEdit()
        self.stationOccInput.editingFinished.connect(self.getStationOccInput)
        layout.addWidget(self.stationOccInput, 9, 1)

        # Add Passengers On
        onLabel = QLabel("Passengers On")
        layout.addWidget(onLabel, 10, 0)
        self.onInput = QLineEdit()
        self.onInput.editingFinished.connect(self.getOnInput)
        layout.addWidget(self.onInput, 10, 1)
        
        # Add border
        layout.addWidget(QLabel(" "), 11, 0)

        # Add the Train Number
        trainLabel = QLabel("Train Number")
        layout.addWidget(trainLabel, 12, 0)
        self.trainInput = QComboBox()
        self.trainInput.addItems(["1", "2", "3", "4", "5"])
        self.trainInput.currentIndexChanged.connect(self.getTrainInput)
        self.trainInput.currentIndexChanged.connect(self.trainChange)
        layout.addWidget(self.trainInput, 12, 1)

        # Add the train block
        trainBlockLabel = QLabel("Train Block")
        layout.addWidget(trainBlockLabel, 13, 0)
        self.trainBlockInput = QComboBox()
        self.trainBlockInput.addItems(["Yard", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"])
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
        self.signalStateOutput.setText("Red")
        layout.addWidget(self.signalStateOutput, 4, 3)

        # Adding the Track Direction
        directionLabel = QLabel("Track Direction")
        layout.addWidget(directionLabel, 5, 2)
        self.directionOutput = QLineEdit()
        self.directionOutput.setReadOnly(True)
        self.directionOutput.setText("Eastbound")
        layout.addWidget(self.directionOutput, 5, 3)

        # Adding the block train number
        blockTrainLabel = QLabel("Block Train Number")
        layout.addWidget(blockTrainLabel, 6, 2)
        self.blockTrainOutput = QLineEdit()
        self.blockTrainOutput.setReadOnly(True)
        self.blockTrainOutput.setText("0")
        layout.addWidget(self.blockTrainOutput, 6, 3)

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
        layout.addWidget(stationNameLabel, 8, 2)
        self.stationNameOutput = QLineEdit()
        self.stationNameOutput.setReadOnly(True)
        self.stationNameOutput.setText("Station B")
        layout.addWidget(self.stationNameOutput, 8, 3)

        # Adding the Station Occupancy
        occLabel = QLabel("Station Occupancy")
        layout.addWidget(occLabel, 9, 2)
        self.occOutput = QLineEdit()
        self.occOutput.setReadOnly(True)
        self.occOutput.setText("0 people")
        layout.addWidget(self.occOutput, 9, 3)

        # Adding the train number
        trainLabel = QLabel("Train Number")
        layout.addWidget(trainLabel, 12, 2)
        self.trainNumberOutput = QLineEdit()
        self.trainNumberOutput.setReadOnly(True)
        self.trainNumberOutput.setText("1")
        layout.addWidget(self.trainNumberOutput, 12, 3)

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

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Block Number from the UI
    def getBlockInput(self, index):
        self.data["blockNo"] = index
        outputText = str(self.data["blockNo"] + 1)
        self.blockNumberOutput.setText(outputText)

        # Refresh Main UI
        trackSignals.updateSignal.emit()
    
    # Gets the Switch Position from the UI
    def getSwitchPositionInput(self, index):
        if self.toggleSwitch != 1:
            if self.data["line"] == 0:
                self.backEnd.data["switchPos"].removeAt(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)
                self.backEnd.data["switchPos"].insertAt(index, int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)
            elif self.data["line"] == 1:
                self.backEnd.data["switchPos"].removeAt(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)
                self.backEnd.data["switchPos"].insertAt(index, int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)

        if self.data["line"] == 0:
            outputText = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)) if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1) == 1 else str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.data["blockNo"])) - 1))
        elif self.data["line"] == 1:
            outputText = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)) if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1) == 1 else str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.data["blockNo"])) - 1))
        self.switchPositionOutput.setText(outputText) # Put output text in value box

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Gate Position state from the UI
    def getGatePositionInput(self, index):
        self.backEnd.data["gatePos"] = index
        outputText = "Down" if self.backEnd.data["gatePos"] == 1 else "Up"
        self.gatePositionOutput.setText(outputText)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Signal State from the UI
    def getSignalStateInput(self, index):
        self.backEnd.data["sigState"][self.data["blockNo"]] = index
        if self.backEnd.data["sigState"][self.data["blockNo"]] == 2:
            outputText  = "Green"
        elif (self.backEnd.data["sigState"][self.data["blockNo"]]) == 1:
            outputText = "Yellow"
        else:
            outputText = "Red"
        self.signalStateOutput.setText(outputText)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Track direction from the UI
    def getDirectionInput(self, index):
        self.backEnd.data["direction"][self.data["blockNo"]] = index
        outputText = "Westbound" if self.backEnd.data["direction"][self.data["blockNo"]] == 1 else "Eastbound"
        self.directionOutput.setText(outputText)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets Signal State if block changes
    def blockChange(self, index):
        # Set new signal states
        if self.backEnd.data["sigState"][index] == 2:
            outputText  = "Green"
        elif (self.backEnd.data["sigState"][index]) == 1:
            outputText = "Yellow"
        else:
            outputText = "Red"
        self.signalStateOutput.setText(outputText)
        self.signalStateInput.setCurrentText(outputText)

        # Set new switch states
        self.toggleSwitch = 1
        if self.data["line"] == 0 and index != -1 and int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) > 0 and index + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)):
            outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1) == 1 else str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1))
            self.switchPositionInput.setEnabled(True)
            self.switchPositionOutput.setText(outputText1)

            i = self.switchPositionInput.count() - 1
            while i >= 0:
                self.switchPositionInput.removeItem(i)
                i -= 1

            self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)))
            self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(index)) - 1)))
            self.switchPositionInput.setCurrentText(outputText1)
        elif self.data["line"] == 1 and index != -1 and int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) > 0 and index + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)):
            outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1) == 1 else str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1))
            self.switchPositionInput.setEnabled(True)
            self.switchPositionOutput.setText(outputText1)

            i = self.switchPositionInput.count() - 1
            while i >= 0:
                self.switchPositionInput.removeItem(i)
                i -= 1

            self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)))
            self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)))
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
            self.gatePositionInput.addItems(["Up", "Down"])
            self.gatePositionInput.setCurrentText(outputText1)
        elif self.data["line"] == 1 and index != -1 and int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) > 0 and index + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)):
            outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1) == 1 else str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1))
            self.switchPositionInput.setEnabled(True)
            self.switchPositionOutput.setText(outputText1)

            i = self.switchPositionInput.count() - 1
            while i >= 0:
                self.switchPositionInput.removeItem(i)
                i -= 1

            self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)))
            self.switchPositionInput.addItem(str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(index)) - 1)))
            self.switchPositionInput.setCurrentText(outputText1)
        else:
            i = self.switchPositionInput.count() - 1
            while i >= 0:
                self.switchPositionInput.removeItem(i)
                i -= 1
            self.switchPositionInput.setEnabled(False)
            self.switchPositionOutput.setText("N/A")
        self.toggleGate = 0

        # Set new block train number
        if self.data["line"] == 0:
            self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNoRed"].__getitem__(self.data["blockNo"])))
        elif self.data["line"] == 1:
            self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNoGreen"].__getitem__(self.data["blockNo"])))


        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets Signal State if block changes
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
        self.backEnd.data["temp"] = float(self.tempInput.text())
        self.tempOutput.setText(str(self.backEnd.data["temp"]) + " degrees F")

        # Configure Track Heaters
        if self.backEnd.data["temp"] > 32:
            self.backEnd.data["trackHeater"] = 0
            self.trackHeaterOutput.setText("Off")
            self.trackHeaterInput.setCurrentText("Off")
        elif self.backEnd.data["temp"] < 32:
            self.backEnd.data["trackHeater"] = 1
            self.trackHeaterOutput.setText("On")
            self.trackHeaterInput.setCurrentText("On")

        # Refresh Main UI
        trackSignals.updateSignal.emit()
    
    # Gets the Track Heater state from the UI
    def getTrackHeaterInput(self, index):
        self.backEnd.data["trackHeater"] = index
        outputText = "On" if self.backEnd.data["trackHeater"] == 1 else "Off"
        self.trackHeaterOutput.setText(outputText)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Station Name from the UI
    def getStationNameInput(self, index):
        self.data["stationName"] = index
        outputText = "Station C" if self.data["stationName"] == 1 else "Station B"
        self.stationNameOutput.setText(outputText)

        # Set new station occupancy
        if self.backEnd.data["stationOccupancy"][index] == 1:
            outputText1  = "1 person"
        else:
            outputText1 = str(self.backEnd.data["stationOccupancy"][index]) + " people"
        self.occOutput.setText(outputText1)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Station Occupancy from the UI
    def getStationOccInput(self):
        self.backEnd.data["stationOccupancy"][self.data["stationName"]] = int(self.stationOccInput.text())
        if self.backEnd.data["stationOccupancy"][self.data["stationName"]] == 1:
            self.occOutput.setText("1 person")
        else:
            self.occOutput.setText(str(self.backEnd.data["stationOccupancy"][self.data["stationName"]]) + " people")

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Train Number from the UI
    def getTrainInput(self, index):
        self.train["trainNo"] = index
        outputText = str(self.train["trainNo"] + 1)
        self.trainNumberOutput.setText(outputText)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Train Block from the UI
    def getTrainBlockInput(self, index):
        # Update block train number
        if self.toggle != 1:
            if self.backEnd.data["direction"][index] == 0:
                if index == 11 and self.backEnd.data["switchPos"] == 1:
                        self.backEnd.data["blockTrainNo"][4] = 0
                else:
                    self.backEnd.data["blockTrainNo"][index - 2] = 0
            elif self.backEnd.data["direction"][index] == 1:
                if index == 5 and self.backEnd.data["switchPos"] == 1:
                    self.backEnd.data["blockTrainNo"][10] = 0
                else:
                    self.backEnd.data["blockTrainNo"][index] = 0
            if index != 0:
                self.backEnd.data["blockTrainNo"][index - 1] = self.train["trainNo"] + 1
                self.blockTrainOutput.setText(str(self.backEnd.data["blockTrainNo"][self.data["blockNo"]]))
            else:
                self.blockTrainOutput.setText("Yard")

            # Update Authority
            self.backEnd.data["authority"][self.train["trainNo"]] -= 1
            if self.backEnd.data["authority"][self.train["trainNo"]] == 1:
                self.authOutput.setText("1 block")
            else:
                self.authOutput.setText(str(self.backEnd.data["authority"][self.train["trainNo"]]) + " blocks")

        # Update train block output
        self.train["trainBlock"][self.train["trainNo"]] = index
        if self.train["trainBlock"][self.train["trainNo"]] == 0:
            outputText  = "Yard"
        else:
            outputText = str(self.train["trainBlock"][self.train["trainNo"]])
        self.trainBlockOutput.setText(outputText)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets new data if train changes
    def trainChange(self, index):
        self.toggle = 1

        # Set new train block
        if self.train["trainBlock"][index] == 0:
            outputText  = "Yard"
        else:
            outputText = str(self.train["trainBlock"][index])
        self.trainBlockOutput.setText(outputText)
        self.trainBlockInput.setCurrentText(outputText)
        self.toggle = 0

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

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the number of passengers off from the UI
    def getOffInput(self):
        if (self.train["trainBlock"][self.train["trainNo"]] == 10 or self.train["trainBlock"][self.train["trainNo"]] == 15) and self.backEnd.data["numPassengers"][self.train["trainNo"]] - int(self.offInput.text()) >= 0:
            self.backEnd.data["numPassengers"][self.train["trainNo"]] -= int(self.offInput.text())
        elif self.backEnd.data["numPassengers"][self.train["trainNo"]] - int(self.offInput.text()) < 0:
            self.backEnd.data["numPassengers"][self.train["trainNo"]] = 0
        if self.backEnd.data["numPassengers"][self.train["trainNo"]] == 1:
            self.numPassengersOutput.setText("1 person")
        else:
            self.numPassengersOutput.setText(str(self.backEnd.data["numPassengers"][self.train["trainNo"]]) + " people")

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the number of passengers on from the UI
    def getOnInput(self):
        if self.backEnd.data["blockTrainNo"][9] > 0 and self.data["stationName"] == 0 and self.backEnd.data["stationOccupancy"][self.data["stationName"]] - int(self.onInput.text()) >= 0:
            self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][9] - 1] += int(self.onInput.text())
            self.backEnd.data["stationOccupancy"][self.data["stationName"]] -= int(self.onInput.text())
        elif self.backEnd.data["blockTrainNo"][14] > 0 and self.data["stationName"] == 1 and self.backEnd.data["stationOccupancy"][self.data["stationName"]] - int(self.onInput.text()) >= 0:
            self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][14] - 1] += int(self.onInput.text())
            self.backEnd.data["stationOccupancy"][self.data["stationName"]] -= int(self.onInput.text())
        elif self.backEnd.data["blockTrainNo"][9] > 0 and self.data["stationName"] == 0 and self.backEnd.data["stationOccupancy"][self.data["stationName"]] - int(self.onInput.text()) < 0:
            self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][9] - 1] += self.backEnd.data["stationOccupancy"][self.data["stationName"]]
            self.backEnd.data["stationOccupancy"][self.data["stationName"]] = 0
        elif self.backEnd.data["blockTrainNo"][14] > 0 and self.data["stationName"] == 1 and self.backEnd.data["stationOccupancy"][self.data["stationName"]] - int(self.onInput.text()) < 0:
            self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][14] - 1] += self.backEnd.data["stationOccupancy"][self.data["stationName"]]
            self.backEnd.data["stationOccupancy"][self.data["stationName"]] = 0

        if self.backEnd.data["stationOccupancy"][self.data["stationName"]] == 1:
            self.occOutput.setText("1 person")
        else:
            self.occOutput.setText(str(self.backEnd.data["stationOccupancy"][self.data["stationName"]]) + " people")

        if self.backEnd.data["numPassengers"][self.train["trainNo"]] == 1:
            self.numPassengersOutput.setText("1 person")
        else:
            self.numPassengersOutput.setText(str(self.backEnd.data["numPassengers"][self.train["trainNo"]]) + " people")

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the authority input from the UI
    def getAuthInput(self):
        self.backEnd.data["authority"][self.train["trainNo"]] = int(self.authInput.text())
        if self.backEnd.data["authority"][self.train["trainNo"]] == 1:
            self.authOutput.setText("1 block")
        else:
            self.authOutput.setText(str(self.backEnd.data["authority"][self.train["trainNo"]]) + " blocks")

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the commanded speed input from the UI
    def getCSpeedInput(self):
        self.backEnd.data["commandedSpeed"][self.train["trainNo"]] = int(self.cSpeedInput.text())
        self.cSpeedOutput.setText(str(self.backEnd.data["commandedSpeed"][self.train["trainNo"]]) + " MPH")

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Real Time Clock state from the UI
    def getRealTimeClockInput(self):
        self.backEnd.data["rtc"] = self.realTimeClockInput.text()
        self.realTimeClockOutput.setText(self.backEnd.data["rtc"])

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Returns all the data in the inputData Array
    def getData(self):
        return self.data

def main():
    app = QApplication(argv)
    testUI = TrackModelTestUI()
    testUI.show()
    #mainUI = TrackModelMainUI()
    #mainUI.show()
    app.exit(app.exec())

if __name__ == "__main__":
    main()