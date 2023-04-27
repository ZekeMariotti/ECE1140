# Main UI for the Train Controller Software

from distutils.cmd import Command
import sys
sys.path.append(__file__.replace("\TrainControllerSoftware\TrainControllerTestUI.py", ""))

import Integration.Conversions as Conversions

from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from TrainControllerSW import TrainControllerSW
from Integration.TMTCSignals import *
from Integration.TimeSignals import *
from Inputs import Inputs
from Outputs import Outputs
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
            self.TrainControllerSW = TrainControllerSW(trainId=2, line="Green", commandedSpeed=0, currentSpeed=0, authority=0, inputTime="2023-02-20T21:52:48.3940347-05:00", 
                                                       undergroundState=False, temperature=0, stationName="setupStationName", platformSide=0, 
                                                       nextStationName="station2", isBeacon=False, externalLightsState=False, internalLightsState=False, leftDoorState=False, 
                                                       rightDoorState=False, serviceBrakeState=False, emergencyBrakeState=False, serviceBrakeStatus=False, engineStatus=False, 
                                                       communicationsStatus=False, power=0, leftDoorCommand=False, rightDoorCommand=False, serviceBrakeCommand=False, 
                                                       emergencyBrakeCommand=False, externalLightCommand=False, internalLightCommand=False, stationAnnouncement="setupStationAnnouncement")    

            self.TrainID = self.TrainControllerSW.trainId

            # Used to automatically update main ui     
            self.connectIO = False  

            # Outputs from main
            self.powerCommand = None
            self.leftDoorCommand = None
            self.rightDoorCommand = None
            self.serviceBrakeCommand = None
            self.emergencyBrakeCommand = None
            self.externalLightCommand = None
            self.internalLightCommand = None
            self.stationAnnouncement = None
            self.stationState = None
            TMTCSignals.commandedPowerSignal.connect(self.commandedPowerSignalHandler)
            TMTCSignals.leftDoorCommandSignal.connect(self.leftDoorCommandSignalHandler)
            TMTCSignals.rightDoorCommandSignal.connect(self.rightDoorCommandSignalHandler)
            TMTCSignals.serviceBrakeCommandSignal.connect(self.serviceBrakeCommandSignalHandler)
            TMTCSignals.emergencyBrakeCommandSignal.connect(self.emergencyBrakeCommandSignalHandler)
            TMTCSignals.externalLightCommandSignal.connect(self.externalLightCommandSignalHandler)
            TMTCSignals.internalLightCommandSignal.connect(self.internalLightCommandSignalHandler)
            TMTCSignals.stationAnnouncementSignal.connect(self.stationAnnouncementSignalHandler)   
            TMTCSignals.stationStateSignal.connect(self.stationStateSignalHandler)    

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

            self.setIsBeaconLabel = self.setIsBeaconLabelSetup()
            self.setIsBeacon = self.setIsBeaconSetup()

            self.setEngineStatusLabel = self.setEngineStatusLabelSetup()
            self.setEngineStatus = self.setEngineStatusSetup()

            self.setCommunicationsStatusLabel = self.setCommunicationsStatusLabelSetup()
            self.setCommunicationsStatus = self.setCommunicationsStatusSetup()

            self.setEmergencyBrakeStateLabel = self.setEmergencyBrakeStateLabelSetup()
            self.setEmergencyBrakeState = self.setEmergencyBrakeStateSetup()

            self.setStationNameLabel = self.setStationNameLabelSetup()
            self.setStationName = self.setStationNameSetup()

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

            self.gridLayout.addWidget(self.setIsBeaconLabel, 2, 0)
            self.gridLayout.addWidget(self.setIsBeacon, 2, 1)

            self.gridLayout.addWidget(self.setEngineStatusLabel, 3, 0)
            self.gridLayout.addWidget(self.setEngineStatus, 3, 1)

            self.gridLayout.addWidget(self.setCommunicationsStatusLabel, 4, 0)
            self.gridLayout.addWidget(self.setCommunicationsStatus, 4, 1)

            self.gridLayout.addWidget(self.setEmergencyBrakeStateLabel, 5, 0)
            self.gridLayout.addWidget(self.setEmergencyBrakeState, 5, 1)

            self.gridLayout.addWidget(self.setServiceBrakeStateLabel, 6, 0)
            self.gridLayout.addWidget(self.setServiceBrakeState, 6, 1)

            self.gridLayout.addWidget(self.setServiceBrakeStatusLabel, 7, 0)
            self.gridLayout.addWidget(self.setServiceBrakeStatus, 7, 1)

            self.gridLayout.addWidget(self.setUndergroundStateLabel, 8, 0)
            self.gridLayout.addWidget(self.setUndergroundState, 8, 1)

            self.gridLayout.addWidget(self.currentSpeedSliderLabel, 1, 2)
            self.gridLayout.addWidget(self.currentSpeedSlider, 1, 3)

            self.gridLayout.addWidget(self.commandedSpeedSliderLabel, 2, 2)
            self.gridLayout.addWidget(self.commandedSpeedSlider, 2, 3)

            self.gridLayout.addWidget(self.setAuthorityLabel, 4, 2)
            self.gridLayout.addWidget(self.setAuthority, 4, 3)

            self.gridLayout.addWidget(self.setStationNameLabel, 5, 2)
            self.gridLayout.addWidget(self.setStationName, 5, 3)

            self.gridLayout.addWidget(self.setTemperatureLabel, 3, 2)
            self.gridLayout.addWidget(self.setTemperature, 3, 3)

            self.gridLayout.addWidget(self.setInternalLightStateLabel, 6, 2)
            self.gridLayout.addWidget(self.setInternalLightState, 6, 3)

            self.gridLayout.addWidget(self.setExternalLightStateLabel, 7, 2)
            self.gridLayout.addWidget(self.setExternalLightState, 7, 3)

            self.gridLayout.addWidget(self.setLeftDoorStateLabel, 9, 0)
            self.gridLayout.addWidget(self.setLeftDoorState, 9, 1)

            self.gridLayout.addWidget(self.setRightDoorStateLabel, 10, 0)
            self.gridLayout.addWidget(self.setRightDoorState, 10, 1)

            self.gridLayout.addWidget(self.setPlatformSideLabel, 8, 2)
            self.gridLayout.addWidget(self.setPlatformSide, 8, 3)

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
        
        def setIsBeaconLabelSetup(self):
            setIsBeaconLabel = QLabel()
            setIsBeaconLabel.setFixedSize(QSize(round(self.labelWidth), round(self.labelHeight)))
            setIsBeaconLabel.setText("IsBeacon: ")
            setIsBeaconLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            setIsBeaconLabel.setParent(self)
            return setIsBeaconLabel
        
        def setIsBeaconSetup(self):
            setIsBeacon = QComboBox()
            setIsBeacon.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setIsBeacon.addItems(["Disabled", "Enabled"])
            setIsBeacon.activated.connect(self.setIsBeaconActivated)
            setIsBeacon.setParent(self)
            return setIsBeacon

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

        # In meters/s
        def commandedSpeedSliderSetup(self):
            commandedSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            commandedSpeedSlider.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonWidth*0.3)))
            commandedSpeedSlider.valueChanged.connect(self.commandedSpeedSliderRelease)
            commandedSpeedSlider.setRange(0, 25)
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
            setTemperature.setRange(-100, 100)
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

            self.showAllOutputs.setText(
                f'Power: {self.powerCommand}\n\n'
                f'Left Door\nCommand: {self.leftDoorCommand}\n\n'
                f'Right Door\nCommand: {self.rightDoorCommand}\n\n'
                f'Service Brake\nCommand: {self.serviceBrakeCommand}\n\n'
                f'Emergency Brake\nCommand: {self.emergencyBrakeCommand}\n\n'
                f'External\nLight Command: {self.externalLightCommand}\n\n'
                f'Internal\nLight Command: {self.internalLightCommand}\n\n'
                f'Station\nAnnouncement:\n{self.stationAnnouncement}\n\n'
            )

            if(self.connectIO == True):
                self.writeInputs()

        def writeInputs(self):   
            TMTCSignals.externalLightsStateSignal.emit(self.TrainID, self.externalLightCommand)
            TMTCSignals.internalLightsStateSignal.emit(self.TrainID, self.internalLightCommand)
            TMTCSignals.leftDoorStateSignal.emit(self.TrainID, self.leftDoorCommand)
            TMTCSignals.rightDoorStateSignal.emit(self.TrainID, self.rightDoorCommand)
            TMTCSignals.serviceBrakeStateSignal.emit(self.TrainID, self.serviceBrakeCommand)
            TMTCSignals.emergencyBrakeStateSignal.emit(self.TrainID, self.emergencyBrakeCommand)
        


        # event actions
        def realTimeChanged(self):
            hour = (f'0{self.setRealTime.time().hour()}' if (self.setRealTime.time().hour() < 10) else self.setRealTime.time().hour())
            minute = (f'0{self.setRealTime.time().minute()}' if (self.setRealTime.time().minute() < 10) else self.setRealTime.time().minute())
            second = (f'0{self.setRealTime.time().second()}' if (self.setRealTime.time().second() < 10) else self.setRealTime.time().second())
            millisecond = (f'00{self.setRealTime.time().msec()}' if (self.setRealTime.time().msec() < 10) else self.setRealTime.time().msec())
            if (int(millisecond) < 100 and int(millisecond) >= 10): 
                millisecond = f'0{millisecond}'

            self.TrainControllerSW.inputs.inputTime = f'2023-02-22T{hour}:{minute}:{second}.{millisecond}0000-05:00'
            rtcSignals.rtcSignal.emit(f'2023-02-22T{hour}:{minute}:{second}.{millisecond}0000-05:00')
        
        def setIsBeaconActivated(self):
            self.TrainControllerSW.inputs.isBeacon = (self.setIsBeacon.currentText() == "Enabled")
            TMTCSignals.isBeaconSignal.emit(self.TrainControllerSW.trainId, self.setIsBeacon.currentText() == "Enabled")
            self.setStationNameTextChanged()

        def engineStatusActivated(self):
            self.TrainControllerSW.inputs.engineStatus = (self.setEngineStatus.currentText() == "Enabled")
            TMTCSignals.engineStatusSignal.emit(self.TrainControllerSW.trainId, self.setEngineStatus.currentText() == "Enabled")

        def setCommunicationsStatusActivated(self):
            self.TrainControllerSW.inputs.communicationsStatus = (self.setCommunicationsStatus.currentText() == "Enabled")
            TMTCSignals.communicationsStatusSignal.emit(self.TrainControllerSW.trainId, self.setCommunicationsStatus.currentText() == "Enabled")

        def setStationNameTextChanged(self):
            if (self.stationState == True):
                self.TrainControllerSW.inputs.stationName = self.setStationName.text()
                TMTCSignals.stationNameSignal.emit(self.TrainControllerSW.trainId, self.setStationName.text())
            else:
                self.TrainControllerSW.inputs.nextStationName = self.setStationName.text()
                TMTCSignals.nextStationNameSignal.emit(self.TrainControllerSW.trainId, self.setStationName.text())

        def currentSpeedSliderRelease(self):
            self.TrainControllerSW.inputs.currentSpeed = self.currentSpeedSlider.value()
            TMTCSignals.currentSpeedSignal.emit(self.TrainControllerSW.trainId, self.currentSpeedSlider.value())

        def setEmergencyBrakeStateActivated(self):
            self.TrainControllerSW.inputs.emergencyBrakeState = (self.setEmergencyBrakeState.currentText() == "Enabled")
            TMTCSignals.emergencyBrakeStateSignal.emit(self.TrainControllerSW.trainId, self.setEmergencyBrakeState.currentText() == "Enabled")

        def setServiceBrakeStateActivated(self):
            self.TrainControllerSW.inputs.serviceBrakeState = (self.setServiceBrakeState.currentText() == "Enabled")
            TMTCSignals.serviceBrakeStateSignal.emit(self.TrainControllerSW.trainId, self.setServiceBrakeState.currentText() == "Enabled")

        def setServiceBrakeStatusActivated(self):
            self.TrainControllerSW.inputs.serviceBrakeStatus = (self.setServiceBrakeStatus.currentText() == "Enabled")
            TMTCSignals.serviceBrakeStatusSignal.emit(self.TrainControllerSW.trainId, self.setServiceBrakeStatus.currentText() == "Enabled")

        def commandedSpeedSliderRelease(self):
            self.TrainControllerSW.inputs.commandedSpeed = self.commandedSpeedSlider.value()
            TMTCSignals.commandedSpeedSignal.emit(self.TrainControllerSW.trainId, self.commandedSpeedSlider.value())

        def setAuthorityTextChanged(self):
            self.TrainControllerSW.inputs.authority = int(self.setAuthority.text() if self.setAuthority.text() != "" else 0)
            TMTCSignals.authoritySignal.emit(self.TrainControllerSW.trainId, int(self.setAuthority.text() if self.setAuthority.text() != "" else 0))

        def setTemperatureValueChanged(self):
            self.TrainControllerSW.inputs.temperature = self.setTemperature.value()
            TMTCSignals.temperatureSignal.emit(self.TrainControllerSW.trainId, self.setTemperature.value())

        def setInternalLightStateActivated(self):
            self.TrainControllerSW.inputs.internalLightsState = (self.setInternalLightState.currentText() == "Enabled")
            TMTCSignals.internalLightsStateSignal.emit(self.TrainControllerSW.trainId, self.setInternalLightState.currentText() == "Enabled")

        def setExternalLightStateActivated(self):
            self.TrainControllerSW.inputs.externalLightsState = (self.setExternalLightState.currentText() == "Enabled")
            TMTCSignals.externalLightsStateSignal.emit(self.TrainControllerSW.trainId, self.setExternalLightState.currentText() == "Enabled")

        def setLeftDoorStateActivated(self):
            self.TrainControllerSW.inputs.leftDoorState = (self.setLeftDoorState.currentText() == "Opened")
            TMTCSignals.leftDoorStateSignal.emit(self.TrainControllerSW.trainId, self.setLeftDoorState.currentText() == "Opened")

        def setRightDoorStateActivated(self):
            self.TrainControllerSW.inputs.rightDoorState = (self.setRightDoorState.currentText() == "Opened")
            TMTCSignals.rightDoorStateSignal.emit(self.TrainControllerSW.trainId, self.setRightDoorState.currentText() == "Opened")

        def setUndergroundStateActivated(self):
            self.TrainControllerSW.inputs.undergroundState = (self.setUndergroundState.currentText() == "True")
            TMTCSignals.undergroundSignal.emit(self.TrainControllerSW.trainId, self.setUndergroundState.currentText() == "True")

        def setPlatformSideActivated(self):
            if(self.setPlatformSide.currentText() == "Left"):
                self.TrainControllerSW.inputs.platformSide = 0
            elif(self.setPlatformSide.currentText() == "Right"):
                self.TrainControllerSW.inputs.platformSide = 1
            elif(self.setPlatformSide.currentText() == "Both"):
                self.TrainControllerSW.inputs.platformSide = 2
            else:
                self.TrainControllerSW.inputs.platformSide = 0

            TMTCSignals.platformSideSignal.emit(self.TrainControllerSW.trainId, self.TrainControllerSW.inputs.platformSide)

        def ioConnectionToggled(self):
            if (self.toggleOutputToInputConnection.isChecked()):
                self.connectIO = True
            else:
                self.connectIO = False

        # Handlers
        def commandedPowerSignalHandler(self, id, power):
            if (id == self.TrainID):
                self.powerCommand = power

        # Left Door Command input handler
        def leftDoorCommandSignalHandler(self, id, state):
            if (id == self.TrainID):
                self.leftDoorCommand = state

        # Right Door Command input handler
        def rightDoorCommandSignalHandler(self, id, state):
            if (id == self.TrainID):
                self.rightDoorCommand = state

        # Service Brake Command input handler
        def serviceBrakeCommandSignalHandler(self, id, state):
            if (id == self.TrainID):
                self.serviceBrakeCommand = state

        # Emergency Brake Command (Train Controller) input handler
        def emergencyBrakeCommandSignalHandler(self, id, state):
            if (id == self.TrainID):
                self.emergencyBrakeCommand = state

        # External Light Command input handler
        def externalLightCommandSignalHandler(self, id, state):
            if (id == self.TrainID):
                self.externalLightCommand = state

        # Internal Light Command input handler
        def internalLightCommandSignalHandler(self, id, state):
            if (id == self.TrainID):
                self.internalLightCommand = state

        # Station Announcement input handler
        def stationAnnouncementSignalHandler(self, id, station):
            if (id == self.TrainID):
                self.stationAnnouncement = station

        # Station State input handler
        def stationStateSignalHandler(self, id, atStation):
            if (id == self.TrainID):
                self.stationState = atStation



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