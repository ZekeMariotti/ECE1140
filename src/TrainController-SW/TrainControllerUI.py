# Main UI for the Train Controller Software

from distutils.cmd import Command
import sys

from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import *

# Class for the main window
class MainWindow(QMainWindow):

        # Constructor 
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Train Controller")
            self.resize(QSize(1366, 768))
            self.setMinimumSize(1050, 550)

            self.windowWidth = self.frameGeometry().width()
            self.windowHeight = self.frameGeometry().height()
            self.buttonWidth = round(0.13*self.windowWidth)
            self.buttonHeight = round(0.06*self.windowHeight)
            self.labelWidth = self.buttonWidth*2
            self.labelHeight = round(self.buttonHeight*1.3)             
                
            self.station = self.stationSetup()
            self.currentSpeed = self.currentSpeedSetup()
            self.manualSpeedOverride = self.manualSpeedOverrideSetup()
            self.realTimeClock = self.realTimeClockSetup()
            self.engineState = self.engineStateSetup()
            self.emergencyBrakeState = self.emergencyBrakeStateSetup()
            self.emergencyBrakeEnable = self.emergencyBrakeEnableSetup()
            self.emergencyBrakeDisable = self.emergencyBrakeDisableSetup()
            self.serviceBrakeState = self.serviceBrakeStateSetup()
            self.serviceBrakeEnable = self.serviceBrakeEnableSetup()
            self.serviceBrakeDisable = self.serviceBrakeDisableSetup()
            self.commandedSpeedSlider = self.commandedSpeedSliderSetup()  
            self.commandedSpeed = self.commandedSpeedSetup()
            self.authority = self.authoritySetup()
            self.speedLimit = self.speedLimitSetup()
            self.temperature = self.temperatureSetup()


                
        # widget setups
        def stationSetup(self):
            station = QLabel()
            station.setText("Current Station: {station}")
            station.setFixedSize(QSize(round(self.labelWidth*1.6), self.labelHeight*2))
            station.setAlignment(Qt.AlignmentFlag.AlignCenter)
            station.setWordWrap(True)
            station.move(round(self.frameGeometry().width()*0.5-station.frameGeometry().width()*.5), round(self.frameGeometry().height()*0.05-station.frameGeometry().height()*0.5))
            station.setParent(self)
            return station

        def currentSpeedSetup(self):
            currentSpeed = QLabel()
            currentSpeed.setText("Current Speed: {speed} MPH")
            currentSpeed.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*0.5)))
            currentSpeed.setAlignment(Qt.AlignmentFlag.AlignCenter)
            currentSpeed.setWordWrap(True)
            currentSpeed.move(round(self.frameGeometry().width()*0.5-currentSpeed.frameGeometry().width()*.5), round(self.frameGeometry().height()*0.15-currentSpeed.frameGeometry().height()*0.5))
            currentSpeed.setParent(self)
            return currentSpeed

        def manualSpeedOverrideSetup(self):
            manualSpeedOverride = QLabel()
            manualSpeedOverride.setText("Manual Speed Override:")
            manualSpeedOverride.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*0.5)))
            manualSpeedOverride.setAlignment(Qt.AlignmentFlag.AlignCenter)
            manualSpeedOverride.setWordWrap(True)
            manualSpeedOverride.move(round(self.frameGeometry().width()*0.5-manualSpeedOverride.frameGeometry().width()*.5), round(self.frameGeometry().height()*0.3-manualSpeedOverride.frameGeometry().height()*0.5))
            manualSpeedOverride.setParent(self)
            return manualSpeedOverride

        def realTimeClockSetup(self):
            realTimeClock = QLabel()
            realTimeClock.setText("Time: {time}")
            realTimeClock.setFixedSize(QSize(self.labelWidth, round(self.labelHeight*0.5)))
            realTimeClock.setAlignment(Qt.AlignmentFlag.AlignCenter)
            realTimeClock.setWordWrap(True)
            realTimeClock.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.05-realTimeClock.frameGeometry().height()*0.5))
            realTimeClock.setParent(self)
            return realTimeClock

        def engineStateSetup(self):
            engineState = QLabel()
            engineState.setText("Engine State:\n{state}")
            engineState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            engineState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            engineState.setWordWrap(True)
            engineState.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.15-engineState.frameGeometry().height()*0.5))
            engineState.setParent(self)
            return engineState
        
        def emergencyBrakeStateSetup(self):
            emergencyBrakeState = QLabel()
            emergencyBrakeState.setText("Emergency Brake:\n{State}")
            emergencyBrakeState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            emergencyBrakeState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            emergencyBrakeState.setWordWrap(True)
            emergencyBrakeState.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.25-emergencyBrakeState.frameGeometry().height()*0.6))
            emergencyBrakeState.setParent(self)
            return emergencyBrakeState

        def emergencyBrakeEnableSetup(self):
            emergencyBrakeEnable = QPushButton("Enable\nEmergency Brake")
            emergencyBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            emergencyBrakeEnable.clicked.connect(self.emergencyBrakeEnableClick)
            emergencyBrakeEnable.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.3-emergencyBrakeEnable.frameGeometry().height()*0.5))
            emergencyBrakeEnable.setParent(self)
            return emergencyBrakeEnable

        def emergencyBrakeDisableSetup(self):
            emergencyBrakeDisable = QPushButton("Disable\nEmergency Brake")
            emergencyBrakeDisable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            emergencyBrakeDisable.clicked.connect(self.emergencyBrakeDisableClick)
            emergencyBrakeDisable.move(round(self.frameGeometry().width()*0.05+emergencyBrakeDisable.frameGeometry().width()), round(self.frameGeometry().height()*0.3-emergencyBrakeDisable.frameGeometry().height()*0.5))
            emergencyBrakeDisable.setParent(self)
            return emergencyBrakeDisable

        def serviceBrakeStateSetup(self):
            serviceBrakeState = QLabel()
            serviceBrakeState.setText("Service Brake:\n{State}")
            serviceBrakeState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            serviceBrakeState.setWordWrap(True)
            serviceBrakeState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            serviceBrakeState.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.4-serviceBrakeState.frameGeometry().height()*0.6))
            serviceBrakeState.setParent(self)
            return serviceBrakeState

        def serviceBrakeEnableSetup(self):
            serviceBrakeEnable = QPushButton("Enable\nService Brake")
            serviceBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            serviceBrakeEnable.clicked.connect(self.serviceBrakeEnableClick)
            serviceBrakeEnable.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.45-serviceBrakeEnable.frameGeometry().height()*0.5))
            serviceBrakeEnable.setParent(self)
            return serviceBrakeEnable

        def serviceBrakeDisableSetup(self):
            serviceBrakeDisable = QPushButton("Disable\nService Brake")
            serviceBrakeDisable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            serviceBrakeDisable.clicked.connect(self.serviceBrakeDisableClick)
            serviceBrakeDisable.move(round(self.frameGeometry().width()*0.05+serviceBrakeDisable.frameGeometry().width()), round(self.frameGeometry().height()*0.45-serviceBrakeDisable.frameGeometry().height()*0.5))
            serviceBrakeDisable.setParent(self)
            return serviceBrakeDisable

        def commandedSpeedSliderSetup(self):
            commandedSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            commandedSpeedSlider.setFixedSize(QSize(round(self.labelWidth*1.2), round(self.labelHeight*0.5)))
            commandedSpeedSlider.sliderReleased.connect(self.commandedSpeedSliderRelease)
            commandedSpeedSlider.setRange(0, 100)
            commandedSpeedSlider.setSingleStep(1)
            commandedSpeedSlider.move(round(self.frameGeometry().width()*0.5-commandedSpeedSlider.frameGeometry().width()*0.5), round(self.frameGeometry().height()*0.325))
            commandedSpeedSlider.setParent(self)
            return commandedSpeedSlider

        def commandedSpeedSetup(self):
            commandedSpeed = QLabel()
            commandedSpeed.setText("Commanded Speed:\n{speed} MPH")
            commandedSpeed.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            commandedSpeed.setAlignment(Qt.AlignmentFlag.AlignCenter)
            commandedSpeed.setWordWrap(True)
            commandedSpeed.move(round(self.frameGeometry().width()*0.65), round(self.frameGeometry().height()*0.05-commandedSpeed.frameGeometry().height()*0.5))
            commandedSpeed.setParent(self)
            return commandedSpeed

        def authoritySetup(self):
            authority = QLabel()
            authority.setText("Authority:\n{distance} FEET")
            authority.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            authority.setAlignment(Qt.AlignmentFlag.AlignCenter)
            authority.setWordWrap(True)
            authority.move(round(self.frameGeometry().width()*0.65), round(self.frameGeometry().height()*0.15-authority.frameGeometry().height()*0.5))
            authority.setParent(self)
            return authority

        def speedLimitSetup(self):
            speedLimit = QLabel()
            speedLimit.setText("Speed Limit:\n{speed} MPH")
            speedLimit.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            speedLimit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            speedLimit.setWordWrap(True)
            speedLimit.move(round(self.frameGeometry().width()*0.65), round(self.frameGeometry().height()*0.25-speedLimit.frameGeometry().height()*0.5))
            speedLimit.setParent(self)
            return speedLimit

        def temperatureSetup(self):
            temperature = QLabel()
            temperature.setText("Temperature:\n{temp} F")
            temperature.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            temperature.setAlignment(Qt.AlignmentFlag.AlignCenter)
            temperature.setWordWrap(True)
            temperature.move(round(self.frameGeometry().width()*0.65), round(self.frameGeometry().height()*0.35-temperature.frameGeometry().height()*0.5))
            temperature.setParent(self)
            return temperature


        # event actions

        # might use for resizing elements - adds 31 to height for some reason
        # def resizeEvent(self, event):
        #    self.windowWidth = self.frameGeometry().width()
        #    self.windowHeight = self.frameGeometry().height()
        #    self.buttonWidth = round(0.13*self.windowWidth)
        #    self.buttonHeight = round(0.06*self.windowHeight)
        #    self.labelWidth = self.buttonWidth*2
        #    self.labelHeight = round(self.buttonHeight*1.3)
        
        #    print("width: " + str(self.frameGeometry().width()) + " Height: " + str(self.frameGeometry().height()))
        #    emergencyBrakeEnable = self.emergencyBrakeEnable
        #    emergencyBrakeEnable.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.3-emergencyBrakeEnable.frameGeometry().height()*0.5))
        #    emergencyBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
        #    QMainWindow.resizeEvent(self, event)
           

        def emergencyBrakeEnableClick(self):
            print("Enable Clicked")

        def emergencyBrakeDisableClick(self):
            print("Disable Clicked")

        def serviceBrakeEnableClick(self):
            print("Enable Clicked")

        def serviceBrakeDisableClick(self):
            print("Disable Clicked")

        def commandedSpeedSliderRelease(self):
            print(self.commandedSpeedSlider.value())

# class to create color widgets
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

app.exec()