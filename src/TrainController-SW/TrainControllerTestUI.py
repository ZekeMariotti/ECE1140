# Main UI for the Train Controller Software

from distutils.cmd import Command
import sys
import Conversions

from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from TrainControllerSW import TrainControllerSW, Inputs, Outputs
from datetime import *
from animated_toggle import AnimatedToggle
import os
import json

# Class for the main window
class TestWindow(QMainWindow):

        # Constructor 
        def __init__(self):
            super().__init__()    

            # TrainControllerSW Object for Test UI
            self.TrainControllerSW = TrainControllerSW(0, 0, 0, 0, "2023-02-20T21:52:48.3940347-05:00", False, 0, 0, 0, 0, "setupStationName", 
                                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "setupStationAnnouncement")    

            # Update Inputs
            self.TrainControllerSW.readInputs()      
            self.connectIO = False         

            # Set window defaults
            self.setWindowTitle("Train Controller Test UI")
            self.setFixedSize(QSize(700, 700))

            # Set element defaults
            self.windowWidth = self.frameGeometry().width()
            self.windowHeight = self.frameGeometry().height()
            self.buttonWidth = round(0.15*self.windowWidth)
            self.buttonHeight = round(0.05*self.windowHeight)
            self.labelWidth = round(0.17*self.windowWidth)
            self.labelHeight = round(0.05*self.windowHeight)
            
            self.globalFont = "Times New Roman"     
            self.labelFont = QFont(self.globalFont, 15)
            self.buttonFont = QFont(self.globalFont, 9)
            self.stationFont = QFont(self.globalFont, 20)  
                
            # Create visual elements
            self.mainTimer = self.mainTimerSetup()
            
            self.emptyWidget = self.emptyWidgetSetup()
            self.testLabel = self.testLabelSetup()

            self.setRealTimeLabel = self.setRealTimeLabelSetup()
            self.setRealTime = self.setRealTimeSetup()

            self.setEngineStatusLabel = self.setEngineStatusLabelSetup()
            self.setEngineStatus = self.setEngineStatusSetup()

            self.setEngineStateLabel = self.setEngineStateLabelSetup()
            self.setEngineState = self.setEngineStateSetup()

            self.setCommunicationsStatusLabel = self.setCommunicationsStatusLabelSetup()
            self.setCommunicationsStatus = self.setCommunicationsStatusSetup()

            self.setStationNameLabel = self.setStationNameLabelSetup()
            self.setStationName = self.setStationNameSetup()

            self.setStationStateLabel = self.setStationStateLabelSetup()
            self.setStationState = self.setStationStateSetup()

            self.setEmergencyBrakeStateLabel = self.setEmergencyBrakeStateLabelSetup()
            self.setEmergencyBrakeState = self.setEmergencyBrakeStateSetup()

            self.setServiceBrakeStateLabel = self.setServiceBrakeStateLabelSetup()
            self.setServiceBrakeState = self.setServiceBrakeStateSetup()

            self.setServiceBrakeStatusLabel = self.setServiceBrakeStatusLabelSetup()
            self.setServiceBrakeStatus = self.setServiceBrakeStatusSetup()

            self.currentSpeedSliderLabel = self.currentSpeedSliderLabelSetup()
            self.currentSpeedSlider = self.currentSpeedSliderSetup()

            self.commandedSpeedSliderLabel = self.commandedSpeedSliderLabelSetup()
            self.commandedSpeedSlider = self.commandedSpeedSliderSetup()

            self.setAuthorityLabel = self.setAuthorityLabelSetup()
            self.setAuthority = self.setAuthoritySetup()

            self.setSpeedLimitLabel = self.setSpeedLimitLabelSetup()
            self.setSpeedLimit = self.setSpeedLimitSetup()

            self.setTemperatureLabel = self.setTemperatureLabelSetup()
            self.setTemperature = self.setTemperatureSetup()

            self.setInternalLightStateLabel = self.setInternalLightStateLabelSetup()
            self.setInternalLightState = self.setInternalLightStateSetup()
            
            self.setExternalLightStateLabel = self.setExternalLightStateLabelSetup()
            self.setExternalLightState = self.setExternalLightStateSetup()

            self.setLeftDoorStateLabel = self.setLeftDoorStateLabelSetup()
            self.setLeftDoorState = self.setLeftDoorStateSetup()

            self.setRightDoorStateLabel = self.setRightDoorStateLabelSetup()
            self.setRightDoorState = self.setRightDoorStateSetup()

            self.setUndergroundStateLabel = self.setUndergroundStateLabelSetup()
            self.setUndergroundState = self.setUndergroundStateSetup()

            self.setPlatformSideLabel = self.setPlatformSideLabelSetup()
            self.setPlatformSide = self.setPlatformSideSetup()

            self.connectOutputsToInputs = self.connectOutputsToInputsSetup()
            self.toggleOutputToInputConnection = self.toggleOutputToInputConnectionSetup()

            self.showAllOutputsLabel = self.showAllOutputsLabelSetup()
            self.showAllOutputs = self.showAllOutputsSetup()

            # Grid Layout
            self.mainWidget = QWidget()
            self.gridLayout = QGridLayout()

            self.gridLayout.addWidget(self.emptyWidget, 0, 0)

            self.gridLayout.addWidget(self.setRealTimeLabel, 1, 0)
            self.gridLayout.addWidget(self.setRealTime, 1, 1)

            self.gridLayout.addWidget(self.setEngineStatusLabel, 2, 0)
            self.gridLayout.addWidget(self.setEngineStatus, 2, 1)

            self.gridLayout.addWidget(self.setEngineStateLabel, 3, 0)
            self.gridLayout.addWidget(self.setEngineState, 3, 1)

            self.gridLayout.addWidget(self.setCommunicationsStatusLabel, 4, 0)
            self.gridLayout.addWidget(self.setCommunicationsStatus, 4, 1)

            self.gridLayout.addWidget(self.setStationNameLabel, 5, 0)
            self.gridLayout.addWidget(self.setStationName, 5, 1)

            self.gridLayout.addWidget(self.setStationStateLabel, 6, 0)
            self.gridLayout.addWidget(self.setStationState, 6, 1)

            self.gridLayout.addWidget(self.setEmergencyBrakeStateLabel, 7, 0)
            self.gridLayout.addWidget(self.setEmergencyBrakeState, 7, 1)

            self.gridLayout.addWidget(self.setServiceBrakeStateLabel, 8, 0)
            self.gridLayout.addWidget(self.setServiceBrakeState, 8, 1)

            self.gridLayout.addWidget(self.setServiceBrakeStatusLabel, 9, 0)
            self.gridLayout.addWidget(self.setServiceBrakeStatus, 9, 1)

            self.gridLayout.addWidget(self.setUndergroundStateLabel, 10, 0)
            self.gridLayout.addWidget(self.setUndergroundState, 10, 1)

            self.gridLayout.addWidget(self.currentSpeedSliderLabel, 1, 2)
            self.gridLayout.addWidget(self.currentSpeedSlider, 1, 3)

            self.gridLayout.addWidget(self.commandedSpeedSliderLabel, 2, 2)
            self.gridLayout.addWidget(self.commandedSpeedSlider, 2, 3)

            self.gridLayout.addWidget(self.setAuthorityLabel, 3, 2)
            self.gridLayout.addWidget(self.setAuthority, 3, 3)

            self.gridLayout.addWidget(self.setSpeedLimitLabel, 4, 2)
            self.gridLayout.addWidget(self.setSpeedLimit, 4, 3)

            self.gridLayout.addWidget(self.setTemperatureLabel, 5, 2)
            self.gridLayout.addWidget(self.setTemperature, 5, 3)

            self.gridLayout.addWidget(self.setInternalLightStateLabel, 6, 2)
            self.gridLayout.addWidget(self.setInternalLightState, 6, 3)

            self.gridLayout.addWidget(self.setExternalLightStateLabel, 7, 2)
            self.gridLayout.addWidget(self.setExternalLightState, 7, 3)

            self.gridLayout.addWidget(self.setLeftDoorStateLabel, 8, 2)
            self.gridLayout.addWidget(self.setLeftDoorState, 8, 3)

            self.gridLayout.addWidget(self.setRightDoorStateLabel, 9, 2)
            self.gridLayout.addWidget(self.setRightDoorState, 9, 3)

            self.gridLayout.addWidget(self.setPlatformSideLabel, 10, 2)
            self.gridLayout.addWidget(self.setPlatformSide, 10, 3)

            #self.gridLayout.addWidget(self.connectOutputsToInputs, 9, 5)
            self.gridLayout.addWidget(self.toggleOutputToInputConnection, 9, 6)

            self.gridLayout.addWidget(self.showAllOutputsLabel, 1, 5)

            self.mainWidget.setLayout(self.gridLayout)
            self.setCentralWidget(self.mainWidget)
            

                
        # widget setups
        def emptyWidgetSetup(self):
            emptyWidget = QLabel()
            emptyWidget.setFixedSize(QSize(round(self.labelWidth), round(self.buttonHeight)))
            emptyWidget.setParent(self)
            return emptyWidget

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
            setRealTimeLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setRealTimeLabel.setText("Clock:")
            setRealTimeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setRealTimeLabel.setParent(self)
            return setRealTimeLabel

        def setRealTimeSetup(self):
            setRealTime = QTimeEdit()
            setRealTime.setDisplayFormat("HH:mm:ss.zzz")
            setRealTime.timeChanged.connect(self.realTimeChanged)
            setRealTime.setParent(self)
            return setRealTime

        def setEngineStatusLabelSetup(self):
            setEngineStatusLabel = QLabel()
            setEngineStatusLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setEngineStatusLabel.setText("Engine Status:")
            setEngineStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setEngineStatusLabel.setParent(self)
            return setEngineStatusLabel

        def setEngineStatusSetup(self):
            setEngineStatus = QComboBox()
            setEngineStatus.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setEngineStatus.addItems(["Disabled", "Enabled"])
            setEngineStatus.activated.connect(self.engineStatusActivated)
            setEngineStatus.setParent(self)
            return setEngineStatus

        def setEngineStateLabelSetup(self):
            setEngineStateLabel = QLabel()
            setEngineStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setEngineStateLabel.setText("Engine State:")
            setEngineStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setEngineStateLabel.setParent(self)
            return setEngineStateLabel
        
        def setEngineStateSetup(self):
            setEngineState = QComboBox()
            setEngineState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setEngineState.addItems(["Disabled", "Enabled"])
            setEngineState.activated.connect(self.engineStateActivated)
            setEngineState.setParent(self)
            return setEngineState

        def setCommunicationsStatusLabelSetup(self):
            setCommunicationsStatusLabel = QLabel()
            setCommunicationsStatusLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setCommunicationsStatusLabel.setText("Communciations\nState:")
            setCommunicationsStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setCommunicationsStatusLabel.setParent(self)
            return setCommunicationsStatusLabel
        
        def setCommunicationsStatusSetup(self):
            setCommunicationsStatus = QComboBox()
            setCommunicationsStatus.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setCommunicationsStatus.addItems(["Disabled", "Enabled"])
            setCommunicationsStatus.activated.connect(self.setCommunicationsStatusActivated)
            setCommunicationsStatus.setParent(self)
            return setCommunicationsStatus

        def setStationNameLabelSetup(self):
            setStationNameLabel = QLabel()
            setStationNameLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setStationNameLabel.setText("Station Name:")
            setStationNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setStationNameLabel.setParent(self)
            return setStationNameLabel

        def setStationNameSetup(self):
            setStationName = QLineEdit()
            setStationName.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setStationName.textChanged.connect(self.setStationNameTextChanged)
            setStationName.setParent(self)
            return setStationName

        def setStationStateLabelSetup(self):
            setStationStateLabel = QLabel()
            setStationStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setStationStateLabel.setText("Station State:")
            setStationStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setStationStateLabel.setParent(self)
            return setStationStateLabel

        def setStationStateSetup(self):
            setStationState = QComboBox()
            setStationState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setStationState.addItems(["Disabled", "Enabled"])
            setStationState.activated.connect(self.setStationStateActivated)
            setStationState.setParent(self)
            return setStationState
        
        def setEmergencyBrakeStateLabelSetup(self):
            setEmergencyBrakeStateLabel = QLabel()
            setEmergencyBrakeStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setEmergencyBrakeStateLabel.setText("Emergency\nBrake:")
            setEmergencyBrakeStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setEmergencyBrakeStateLabel.setParent(self)
            return setEmergencyBrakeStateLabel

        
        def setEmergencyBrakeStateSetup(self):
            setEmergencyBrakeState = QComboBox()
            setEmergencyBrakeState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setEmergencyBrakeState.addItems(["Disabled", "Enabled"])
            setEmergencyBrakeState.activated.connect(self.setEmergencyBrakeStateActivated)
            setEmergencyBrakeState.setParent(self)
            return setEmergencyBrakeState

        def setServiceBrakeStateLabelSetup(self):
            setServiceBrakeStateLabel = QLabel()
            setServiceBrakeStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setServiceBrakeStateLabel.setText("Service\nBrake State:")
            setServiceBrakeStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setServiceBrakeStateLabel.setParent(self)
            return setServiceBrakeStateLabel

        def setServiceBrakeStateSetup(self):
            setServiceBrakeState = QComboBox()
            setServiceBrakeState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setServiceBrakeState.addItems(["Disabled", "Enabled"])
            setServiceBrakeState.activated.connect(self.setServiceBrakeStateActivated)
            setServiceBrakeState.setParent(self)
            return setServiceBrakeState

        def setServiceBrakeStatusLabelSetup(self):
            setServiceBrakeStatusLabel = QLabel()
            setServiceBrakeStatusLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setServiceBrakeStatusLabel.setText("Service\nBrake Status:")
            setServiceBrakeStatusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setServiceBrakeStatusLabel.setParent(self)
            return setServiceBrakeStatusLabel


        def setServiceBrakeStatusSetup(self):
            setServiceBrakeStatus = QComboBox()
            setServiceBrakeStatus.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setServiceBrakeStatus.addItems(["Disabled", "Enabled"])
            setServiceBrakeStatus.activated.connect(self.setServiceBrakeStatusActivated)
            setServiceBrakeStatus.setParent(self)
            return setServiceBrakeStatus
        
        def currentSpeedSliderLabelSetup(self):
            currentSpeedSliderLabel = QLabel()
            currentSpeedSliderLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
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
            commandedSpeedSliderLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            commandedSpeedSliderLabel.setText("Commanded \nSpeed:")
            commandedSpeedSliderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            commandedSpeedSliderLabel.setParent(self)
            return commandedSpeedSliderLabel

        def commandedSpeedSliderSetup(self):
            commandedSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            commandedSpeedSlider.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonWidth*0.3)))
            commandedSpeedSlider.valueChanged.connect(self.commandedSpeedSliderRelease)
            commandedSpeedSlider.setRange(0, self.TrainControllerSW.MAX_SPEED*2)
            commandedSpeedSlider.setSingleStep(1)
            commandedSpeedSlider.setParent(self)
            return commandedSpeedSlider

        def setAuthorityLabelSetup(self):
            setAuthorityLabel = QLabel()
            setAuthorityLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setAuthorityLabel.setText("Authority:")
            setAuthorityLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setAuthorityLabel.setParent(self)
            return setAuthorityLabel

        def setAuthoritySetup(self):
            setAuthority = QLineEdit()
            setAuthority.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setAuthority.textChanged.connect(self.setAuthorityTextChanged)
            setAuthority.setParent(self)
            return setAuthority

        def setSpeedLimitLabelSetup(self):
            setSpeedLimitLabel = QLabel()
            setSpeedLimitLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setSpeedLimitLabel.setText("Speed Limit:")
            setSpeedLimitLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setSpeedLimitLabel.setParent(self)
            return setSpeedLimitLabel

        def setSpeedLimitSetup(self):
            setSpeedLimit = QSlider(Qt.Orientation.Horizontal)
            setSpeedLimit.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setSpeedLimit.valueChanged.connect(self.setSpeedLimitValueChanged)
            setSpeedLimit.setRange(0, self.TrainControllerSW.MAX_SPEED)
            setSpeedLimit.setSingleStep(1)
            setSpeedLimit.setParent(self)
            return setSpeedLimit

        def setTemperatureLabelSetup(self):
            setTemperatureLabel = QLabel()
            setTemperatureLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setTemperatureLabel.setText("Temperature:")
            setTemperatureLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setTemperatureLabel.setParent(self)
            return setTemperatureLabel

        def setTemperatureSetup(self):
            setTemperature = QSlider(Qt.Orientation.Horizontal)
            setTemperature.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setTemperature.valueChanged.connect(self.setTemperatureValueChanged)
            setTemperature.setRange(-50, 50)
            setTemperature.setSingleStep(1)
            setTemperature.setParent(self)
            return setTemperature

        def setInternalLightStateLabelSetup(self):
            setInternalLightStateLabel = QLabel()
            setInternalLightStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setInternalLightStateLabel.setText("Internal\nLights:")
            setInternalLightStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setInternalLightStateLabel.setParent(self)
            return setInternalLightStateLabel

        def setInternalLightStateSetup(self):
            setInternalLightState = QComboBox()
            setInternalLightState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setInternalLightState.addItems(["Disabled", "Enabled"])
            setInternalLightState.activated.connect(self.setInternalLightStateActivated)
            setInternalLightState.setParent(self)
            return setInternalLightState

        def setExternalLightStateLabelSetup(self):
            setExternalLightStateLabel = QLabel()
            setExternalLightStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setExternalLightStateLabel.setText("External\nLights:")
            setExternalLightStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setExternalLightStateLabel.setParent(self)
            return setExternalLightStateLabel

        def setExternalLightStateSetup(self):
            setExternalLightState = QComboBox()
            setExternalLightState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setExternalLightState.addItems(["Disabled", "Enabled"])
            setExternalLightState.activated.connect(self.setExternalLightStateActivated)
            setExternalLightState.setParent(self)
            return setExternalLightState

        def setLeftDoorStateLabelSetup(self):
            setLeftDoorStateLabel = QLabel()
            setLeftDoorStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setLeftDoorStateLabel.setText("Left Door:")
            setLeftDoorStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setLeftDoorStateLabel.setParent(self)
            return setLeftDoorStateLabel

        def setLeftDoorStateSetup(self):
            setLeftDoorState = QComboBox()
            setLeftDoorState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setLeftDoorState.addItems(["Closed", "Opened"])
            setLeftDoorState.activated.connect(self.setLeftDoorStateActivated)
            setLeftDoorState.setParent(self)
            return setLeftDoorState

        def setRightDoorStateLabelSetup(self):
            setRightDoorStateLabel = QLabel()
            setRightDoorStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setRightDoorStateLabel.setText("Right Door:")
            setRightDoorStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setRightDoorStateLabel.setParent(self)
            return setRightDoorStateLabel

        def setRightDoorStateSetup(self):
            setRightDoorState = QComboBox()
            setRightDoorState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setRightDoorState.addItems(["Closed", "Opened"])
            setRightDoorState.activated.connect(self.setRightDoorStateActivated)
            setRightDoorState.setParent(self)
            return setRightDoorState

        def setUndergroundStateLabelSetup(self):
            setUndergroundStateLabel = QLabel()
            setUndergroundStateLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setUndergroundStateLabel.setText("Underground\nState:")
            setUndergroundStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setUndergroundStateLabel.setParent(self)
            return setUndergroundStateLabel

        def setUndergroundStateSetup(self):
            setUndergroundState = QComboBox()
            setUndergroundState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setUndergroundState.addItems(["False", "True"])
            setUndergroundState.activated.connect(self.setUndergroundStateActivated)
            setUndergroundState.setParent(self)
            return setUndergroundState

        def setPlatformSideLabelSetup(self):
            setPlatformSideLabel = QLabel()
            setPlatformSideLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setPlatformSideLabel.setText("Platform Side:")
            setPlatformSideLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setPlatformSideLabel.setParent(self)
            return setPlatformSideLabel

        def setPlatformSideSetup(self):
            setPlatformSide = QComboBox()
            setPlatformSide.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setPlatformSide.addItems(["Left", "Right", "Both"])
            setPlatformSide.activated.connect(self.setPlatformSideActivated)
            setPlatformSide.setParent(self)
            return setPlatformSide
        
        def connectOutputsToInputsSetup(self):
            connectOutputsToInputs = QLabel()
            connectOutputsToInputs.setFixedSize(QSize(round(self.labelWidth*0.75), round(self.labelHeight)))
            connectOutputsToInputs.setText("Connect Inputs\nand Outputs:")
            connectOutputsToInputs.setFont(QFont("Times", 10))
            connectOutputsToInputs.setAlignment(Qt.AlignmentFlag.AlignLeft)
            connectOutputsToInputs.move(525, 565)
            connectOutputsToInputs.setParent(self)
            return connectOutputsToInputs
        
        def toggleOutputToInputConnectionSetup(self):
            toggleOutputToInputConnection = AnimatedToggle()
            toggleOutputToInputConnection.setFixedSize(toggleOutputToInputConnection.sizeHint())
            toggleOutputToInputConnection.stateChanged.connect(self.ioConnectionToggled)
            toggleOutputToInputConnection.setParent(self)
            return toggleOutputToInputConnection

        def showAllOutputsLabelSetup(self):
            showAllOutputsLabel = QLabel()
            showAllOutputsLabel.setFixedSize(QSize(round(self.labelWidth*1.5), round(self.labelHeight)))
            showAllOutputsLabel.setText("Outputs Column:")
            showAllOutputsLabel.setFont(QFont("Times", 14))
            showAllOutputsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            showAllOutputsLabel.setParent(self)
            return showAllOutputsLabel

        def showAllOutputsSetup(self):
            showAllOutputs = QLabel()
            showAllOutputs.setFixedSize(QSize(round(self.labelWidth*1.5), round(self.labelHeight)*12))
            showAllOutputs.setAlignment(Qt.AlignmentFlag.AlignLeft)
            showAllOutputs.move(525, 135)
            showAllOutputs.setWordWrap(True)

            with open(os.path.join(sys.path[0], "TrainControllerSWOutputs.json"), "r") as filename:
                outputs = Outputs(**json.loads(filename.read()))

            showAllOutputs.setText(
                f'Power: {round(outputs.power, 1)}\n\n'
                f'Left Door\nCommand: {outputs.leftDoorCommand}\n\n'
                f'Right Door\nCommand: {outputs.rightDoorCommand}\n\n'
                f'Service Brake\nCommand: {outputs.serviceBrakeCommand}\n\n'
                f'Emergency Brake\nCommand: {outputs.emergencyBrakeCommand}\n\n'
                f'External\nLight Command: {outputs.externalLightCommand}\n\n'
                f'Internal\nLight Command: {outputs.internalLightCommand}\n\n'
                f'Station\nAnnouncement: {outputs.stationAnnouncement}\n\n'
            )

            showAllOutputs.setParent(self)
            return showAllOutputs
        
        def mainThreadSetup(self):
            self.timerThread = QThread()
            self.timerThread.started.connect(self.mainTimerSetup)

        def mainTimerSetup(self):     
            mainTimer = QTimer()
            mainTimer.setInterval(100)
            mainTimer.timeout.connect(self.mainEventLoop)
            mainTimer.setParent(self)
            mainTimer.start()
            return mainTimer
            
        def mainEventLoop(self):
            with open(os.path.join(sys.path[0], "TrainControllerSWOutputs.json"), "r") as filename:
                outputs = Outputs(**json.loads(filename.read()))

            self.showAllOutputs.setText(
                f'Power: {outputs.power}\n\n'
                f'Left Door\nCommand: {outputs.leftDoorCommand}\n\n'
                f'Right Door\nCommand: {outputs.rightDoorCommand}\n\n'
                f'Service Brake\nCommand: {outputs.serviceBrakeCommand}\n\n'
                f'Emergency Brake\nCommand: {outputs.emergencyBrakeCommand}\n\n'
                f'External\nLight Command: {outputs.externalLightCommand}\n\n'
                f'Internal\nLight Command: {outputs.internalLightCommand}\n\n'
                f'Station\nAnnouncement:\n{outputs.stationAnnouncement}\n\n'
            )

            if(self.connectIO == True):
                self.TrainControllerSW.inputs.emergencyBrakeState = outputs.emergencyBrakeCommand
                self.TrainControllerSW.inputs.serviceBrakeState = outputs.serviceBrakeCommand
                self.TrainControllerSW.inputs.internalLightsState = outputs.internalLightCommand
                self.TrainControllerSW.inputs.externalLightsState = outputs.externalLightCommand
                self.TrainControllerSW.inputs.leftDoorState = outputs.leftDoorCommand
                self.TrainControllerSW.inputs.rightDoorState = outputs.rightDoorCommand
                self.TrainControllerSW.writeInputs()
        


        # event actions
        def realTimeChanged(self):
            hour = (f'0{self.setRealTime.time().hour()}' if (self.setRealTime.time().hour() < 10) else self.setRealTime.time().hour())
            minute = (f'0{self.setRealTime.time().minute()}' if (self.setRealTime.time().minute() < 10) else self.setRealTime.time().minute())
            second = (f'0{self.setRealTime.time().second()}' if (self.setRealTime.time().second() < 10) else self.setRealTime.time().second())
            millisecond = (f'00{self.setRealTime.time().msec()}' if (self.setRealTime.time().msec() < 10) else self.setRealTime.time().msec())
            if (int(millisecond) < 100 and int(millisecond) >= 10): 
                millisecond = f'0{millisecond}'

            self.TrainControllerSW.inputs.inputTime = f'2023-02-22T{hour}:{minute}:{second}.{millisecond}0000-05:00'
            self.TrainControllerSW.writeInputs()

        def engineStatusActivated(self):
            self.TrainControllerSW.inputs.engineStatus = (self.setEngineStatus.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def engineStateActivated(self):
            self.TrainControllerSW.inputs.engineState = (self.setEngineState.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def setCommunicationsStatusActivated(self):
            self.TrainControllerSW.inputs.communicationsStatus = (self.setCommunicationsStatus.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def setStationNameTextChanged(self):
            self.TrainControllerSW.inputs.stationName = self.setStationName.text()
            self.TrainControllerSW.writeInputs()

        def setStationStateActivated(self):
            self.TrainControllerSW.inputs.stationState = (self.setStationState.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def currentSpeedSliderRelease(self):
            self.TrainControllerSW.inputs.currentSpeed = self.currentSpeedSlider.value()
            self.TrainControllerSW.writeInputs()

        def setEmergencyBrakeStateActivated(self):
            self.TrainControllerSW.inputs.emergencyBrakeState = (self.setEmergencyBrakeState.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def setServiceBrakeStateActivated(self):
            self.TrainControllerSW.inputs.serviceBrakeState = (self.setServiceBrakeState.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def setServiceBrakeStatusActivated(self):
            self.TrainControllerSW.inputs.serviceBrakeStatus = (self.setServiceBrakeStatus.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def commandedSpeedSliderRelease(self):
            self.TrainControllerSW.inputs.commandedSpeed = self.commandedSpeedSlider.value()
            self.TrainControllerSW.writeInputs()

        def setAuthorityTextChanged(self):
            self.TrainControllerSW.inputs.authority = int(self.setAuthority.text() if self.setAuthority.text() != "" else 0)
            self.TrainControllerSW.writeInputs()

        def setSpeedLimitValueChanged(self):
            self.TrainControllerSW.inputs.speedLimit = self.setSpeedLimit.value()
            self.TrainControllerSW.writeInputs()

        def setTemperatureValueChanged(self):
            self.TrainControllerSW.inputs.temperature = self.setTemperature.value()
            self.TrainControllerSW.writeInputs()

        def setInternalLightStateActivated(self):
            self.TrainControllerSW.inputs.internalLightsState = (self.setInternalLightState.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def setExternalLightStateActivated(self):
            self.TrainControllerSW.inputs.externalLightsState = (self.setExternalLightState.currentText() == "Enabled")
            self.TrainControllerSW.writeInputs()

        def setLeftDoorStateActivated(self):
            self.TrainControllerSW.inputs.leftDoorState = (self.setLeftDoorState.currentText() == "Opened")
            self.TrainControllerSW.writeInputs()

        def setRightDoorStateActivated(self):
            self.TrainControllerSW.inputs.rightDoorState = (self.setRightDoorState.currentText() == "Opened")
            self.TrainControllerSW.writeInputs()

        def setUndergroundStateActivated(self):
            self.TrainControllerSW.inputs.undergroundState = (self.setUndergroundState.currentText() == "True")
            self.TrainControllerSW.writeInputs()

        def setPlatformSideActivated(self):
            if(self.setPlatformSide.currentText() == "Left"):
                self.TrainControllerSW.inputs.platformSide = 0
            elif(self.setPlatformSide.currentText() == "Right"):
                self.TrainControllerSW.inputs.platformSide = 1
            elif(self.setPlatformSide.currentText() == "Both"):
                self.TrainControllerSW.inputs.platformSide = 2
            else:
                self.TrainControllerSW.inputs.platformSide = 0

            self.TrainControllerSW.writeInputs()

        def ioConnectionToggled(self):
            if (self.toggleOutputToInputConnection.isChecked()):
                self.connectIO = True
            else:
                self.connectIO = False



# Class to create color widgets
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


# Run Test UI Alone
if (__name__ == "__main__"):  
    app = QApplication(sys.argv)

    testWindow = TestWindow()
    testWindow.show()

    app.exec()