# Main UI for the Train Controller Software

from distutils.cmd import Command
import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from TrainControllerSW import TrainControllerSW

# Class for the main window
class TestWindow(QMainWindow):

        # Constructor 
        def __init__(self):
            super().__init__()    

            # TrainControllerSW Object for Test UI
            self.TrainControllerSW = TrainControllerSW(0, 0, 0, "2023-02-20T21:52:48.3940347-05:00", False, 0, 0, 0, 0, "setupStationName", 
                                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "setupStationAnnouncement")    

            # Update Inputs
            self.TrainControllerSW.readInputs()               

            # Set window defaults
            self.setWindowTitle("Train Controller Test UI")
            self.setFixedSize(QSize(480, 540))

            # Set element defaults
            self.windowWidth = self.frameGeometry().width()
            self.windowHeight = self.frameGeometry().height()
            self.buttonWidth = round(0.15*self.windowWidth)
            self.buttonHeight = round(0.07*self.windowHeight)
            self.labelWidth = self.buttonWidth*2
            self.labelHeight = round(self.buttonHeight*1.3)
            
            self.globalFont = "Times New Roman"     
            self.labelFont = QFont(self.globalFont, 15)
            self.buttonFont = QFont(self.globalFont, 9)
            self.stationFont = QFont(self.globalFont, 20)  
                
            # Create visual elements
            self.testLabel = self.testLabelSetup()
            self.setRealTimeLabel = self.setRealTimeLabelSetup()
            self.setRealTime = self.setRealTimeSetup()
            self.setEngineStatusLabel = self.setEngineStatusLabelSetup()
            self.setEngineStatus = self.setEngineStatusSetup()
            self.setEngineStateLabel = self.setEngineStateSetup()
            self.setEngineState = self.setEngineStateSetup()
            self.setCommunicationsStatusLabel = self.setCommunicationsStatusLabelSetup
            self.setCommunicationsStatus = self.setCommunicationsStatusSetup()
            self.setStationNameLabel = self.setStationNameLabelSetup()
            self.setStationName = self.setStationNameSetup()
            self.setStationStateLabel = self.setStationStateLabelSetup()
            self.setStationState = self.setStationStateSetup()
            self.setServiceBrakeStateLabel = self.setServiceBrakeStateLabelSetup()
            self.setServiceBrakeState = self.setServiceBrakeStateSetup()
            self.setServiceBrakeStatusLabel = self.setServiceBrakeStatusLabelSetup()
            self.setServiceBrakeStatus = self.setServiceBrakeStatusSetup()
            self.commandedSpeedSliderLabel = self.commandedSpeedSliderLabelSetup()
            self.setAuthorityLabel = self.setAuthorityLabelSetup()
            self.setAuthority = self.setAuthoritySetup()
            self.setSpeedLimitLabel = self.setSpeedLimitLabelSetup()
            self.setSpeedLimit = self.setSpeedLimitSetup()
            self.setTemperatureLabel = self.setTemperatureLabelSetup()
            self.setTemperature = self.setTemperatureSetup()
            self.setInternalLightStateLabel = self.setInternalLightStateLabelSetup()
            self.setInternalLightState = self.setInternalLightStateSetup()
            self.setExternalLightStateLabel = self.setExternalLightStateLabelSetup()
            self.setLeftDoorStateLabel = self.setLeftDoorStateLabelSetup()
            self.setLeftDoorState = self.setLeftDoorStateSetup()
            self.setRightDoorStateLabel = self.setRightDoorStateLabelSetup()
            self.setRightDoorState = self.setRightDoorStateSetup()
            self.setUndergroundStateLabel = self.setUndergroundStateLabelSetup()
            self.setUndergroundState = self.setUndergroundStateSetup()
            self.setPlatformSideLabel = self.setPlatformSideLabelSetup()
            self.setPlatformSide = self.setPlatformSideSetup()
            self.showAllOutputsLabel = self.showAllOutputsLabelSetup()
            self.showAllOutputs = self.showAllOutputsSetup()
            self.setEmergencyBrakeStateLabel = self.setEmergencyBrakeStateLabelSetup()
            self.setEmergencyBrakeState = self.setEmergencyBrakeStateSetup()
            self.currentSpeedSliderLabel = self.currentSpeedSliderLabelSetup()
            self.currentSpeedSlider = self.currentSpeedSliderSetup()

            # Grid Layout
            self.mainWidget = QWidget()
            self.gridLayout = QGridLayout()
            self.gridLayout.setColumnStretch(3, 100)

            self.gridLayout.addWidget(self.setEmergencyBrakeStateLabel, 0, 0)
            self.gridLayout.addWidget(self.setEmergencyBrakeState, 0, 1)
            self.gridLayout.addWidget(self.currentSpeedSliderLabel, 1, 0)
            self.gridLayout.addWidget(self.currentSpeedSlider, 1, 1)

            self.mainWidget.setLayout(self.gridLayout)
            self.setCentralWidget(self.mainWidget)
            

                
        # widget setups
        # TODO: add functionality to all test elements
        def testLabelSetup(self):
            testLabel = QLabel()         
            testLabel.setFont(self.stationFont)
            testLabel.setText("Test UI")
            testLabel.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*2)))
            testLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            testLabel.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-testLabel.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.07-testLabel.frameGeometry().height()*0.5)
            testLabel.move(x, y)
            testLabel.setParent(self)
            return testLabel

        def setRealTimeLabelSetup(self):
            setRealTimeLabel = QLabel()

        def setRealTimeSetup(self):
            setRealTime = QDateTimeEdit()

        def setEngineStatusLabelSetup(self):
            setEngineStatusSetup = QLabel()

        def setEngineStatusSetup(self):
            setEngineStatus = QComboBox()

        def setEngineStateLabelSetup(self):
            setEngineStateSetup = QLabel()
        
        def setEngineStateSetup(self):
            setEngineState = QComboBox()

        def setCommunicationsStatusLabelSetup(self):
            setCommunicationsStatusLabel = QLabel()
        
        def setCommunicationsStatusSetup(self):
            setCommunicationsStatus = QComboBox()

        def setStationNameLabelSetup(self):
            setStationNameLabel = QLabel()

        def setStationNameSetup(self):
            setStationName = QLineEdit()

        def setStationStateLabelSetup(self):
            setStationStateLabel = QLabel()

        def setStationStateSetup(self):
            setStation = QComboBox()
        
        def setEmergencyBrakeStateLabelSetup(self):
            setEmergencyBrakeStateLabel = QLabel()
            setEmergencyBrakeStateLabel.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setEmergencyBrakeStateLabel.setText("Emergency\nBrake:")
            setEmergencyBrakeStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
           # x = round(self.frameGeometry().width()*0.05)
           # y = round(self.frameGeometry().height()*0.1)
           # setEmergencyBrakeStateLabel.move(x, y)
            setEmergencyBrakeStateLabel.setParent(self)
            return setEmergencyBrakeStateLabel

        
        def setEmergencyBrakeStateSetup(self):
             setEmergencyBrakeState = QComboBox()
             setEmergencyBrakeState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
             setEmergencyBrakeState.addItems(["Disabled", "Enabled"])
             setEmergencyBrakeState.activated.connect(self.setEmergencyBrakeStateActivated)
           #  x = round(self.setEmergencyBrakeStateLabel.frameGeometry().x())
            # y = round(self.setEmergencyBrakeStateLabel.frameGeometry().height()+self.frameGeometry().width()*0.13)
            # setEmergencyBrakeState.move(x, y)
             setEmergencyBrakeState.setParent(self)
             return setEmergencyBrakeState

        def setServiceBrakeStateLabelSetup(self):
            setServiceBrakeStateLabel = QLabel()

        def setServiceBrakeStateSetup(self):
            setServiceBrakeState = QComboBox()

        def setServiceBrakeStatusLabelSetup(self):
            setServiceBrakeStatusLabel = QLabel()

        def setServiceBrakeStatusSetup(self):
            setServiceBrakeStatus = QComboBox()
        
        def currentSpeedSliderLabelSetup(self):
            currentSpeedSliderLabel = QLabel()
            currentSpeedSliderLabel.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            currentSpeedSliderLabel.setText("Current\nSpeed:")
            currentSpeedSliderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            currentSpeedSliderLabel.setParent(self)
            return currentSpeedSliderLabel

        def currentSpeedSliderSetup(self):
            currentSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            currentSpeedSlider.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonWidth*0.3)))
            currentSpeedSlider.valueChanged.connect(self.currentSpeedSliderRelease)
            currentSpeedSlider.setRange(0, self.TrainControllerSW.MAX_SPEED)
            currentSpeedSlider.setSingleStep(1)
            currentSpeedSlider.setParent(self)
            return currentSpeedSlider

        def commandedSpeedSliderLabelSetup(self):
            commandedSpeedSliderLabel = QLabel()

        def commandedSpeedSliderSetup(self):
            commandedSpeedSlider = QSlider(Qt.Orientation.Horizontal)

        def setAuthorityLabelSetup(self):
            setAuthorityLabel = QLabel()

        def setAuthoritySetup(self):
            setAuthority = QLineEdit()

        def setSpeedLimitLabelSetup(self):
            setSpeedLimitLabel = QLabel()

        def setSpeedLimitSetup(self):
            setSpeedLimit = QLineEdit()

        def setTemperatureLabelSetup(self):
            setTemperatureLabel = QLabel()

        def setTemperatureSetup(self):
            setTemperature = QLineEdit()

        def setInternalLightStateLabelSetup(self):
            setInternalLightStateLabel = QLabel()

        def setInternalLightStateSetup(self):
            setInternalLightState = QComboBox()

        def setExternalLightStateLabelSetup(self):
            setExternalLightStateLabel = QLabel()

        def setExternalLightStateSetup(self):
            setExternalLightState = QComboBox()

        def setLeftDoorStateLabelSetup(self):
            setLeftDoorStateLabel = QLabel()

        def setLeftDoorStateSetup(self):
            setLeftDoorState = QComboBox()

        def setRightDoorStateLabelSetup(self):
            setRightDoorStateLabel = QLabel()

        def setRightDoorStateSetup(self):
            setRightDoorState = QComboBox()

        def setUndergroundStateLabelSetup(self):
            setUndergroundStateLabel = QLabel()

        def setUndergroundStateSetup(self):
            setUndergroundState = QComboBox()

        def setPlatformSideLabelSetup(self):
            setPlatformSideLabel = QLabel()

        def setPlatformSideSetup(self):
            setPlatformSide = QComboBox()

        def showAllOutputsLabelSetup(self):
            showAllOutputsLabel = QLabel()

        def showAllOutputsSetup(self):
            showAllOutputs = QLabel()
            showAllOutputs.setText(
                f''
                f''
                f''
                f''
                f''
                f''
                f''
            )
        


        # event actions
        def currentSpeedSliderRelease(self):
             self.TrainControllerSW.inputs.currentSpeed = self.currentSpeedSlider.value()
             self.TrainControllerSW.writeInputs()

        def setEmergencyBrakeStateActivated(self):
             self.TrainControllerSW.inputs.emergencyBrakeState = (self.setEmergencyBrakeState.currentText() == "Enabled")
             self.TrainControllerSW.writeInputs()


# Class to create color widgets
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


# Run Test UI Alone
if (False):  
    app = QApplication(sys.argv)

    testWindow = TestWindow()
    testWindow.show()

    app.exec()