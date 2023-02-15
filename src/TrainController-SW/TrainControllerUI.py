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
            self.buttonWidth = 175
            self.buttonHeight = 50
            self.labelWidth = self.buttonWidth*2
            self.labelHeight = round(self.buttonHeight*1.3)
            #self.emergencyBrakeEnable = None 

            self.setWindowTitle("Train Controller")
            self.setFixedSize(QSize(1366, 768))
            #self.setFixedSize(QSize(1920, 1080))
                
            self.emergencyBrakeState = self.emergencyBrakeStateSetup()
            self.emergencyBrakeEnable = self.emergencyBrakeEnableSetup()
            self.emergencyBrakeDisable = self.emergencyBrakeDisableSetup()
            self.commandedSpeedSlider = self.commandedSpeedSliderSetup()       
                
        # widget setups
        def emergencyBrakeStateSetup(self):
            emergencyBrakeState = QLabel()
            emergencyBrakeState.setText("Emergency Brake: {State}")
            emergencyBrakeState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            emergencyBrakeState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            emergencyBrakeState.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.25-emergencyBrakeState.frameGeometry().height()*0.5))
            emergencyBrakeState.setParent(self)
            return emergencyBrakeState

        def emergencyBrakeEnableSetup(self):
            emergencyBrakeEnable = QPushButton("Enable Emergency Brake")
            emergencyBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            emergencyBrakeEnable.clicked.connect(self.emergencyBrakeEnableClick)
            emergencyBrakeEnable.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.3-emergencyBrakeEnable.frameGeometry().height()*0.5))
            emergencyBrakeEnable.setParent(self)
            return emergencyBrakeEnable

        def emergencyBrakeDisableSetup(self):
            emergencyBrakeDisable = QPushButton("Disable Emergency Brake")
            emergencyBrakeDisable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            emergencyBrakeDisable.clicked.connect(self.emergencyBrakeDisableClick)
            emergencyBrakeDisable.move(round(self.frameGeometry().width()*0.05+emergencyBrakeDisable.frameGeometry().width()), round(self.frameGeometry().height()*0.3-emergencyBrakeDisable.frameGeometry().height()*0.5))
            emergencyBrakeDisable.setParent(self)
            return emergencyBrakeDisable

        def commandedSpeedSliderSetup(self):
            commandedSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            commandedSpeedSlider.setFixedSize(300, 40)
            commandedSpeedSlider.setRange(0, 100)
            commandedSpeedSlider.setSingleStep(1)
            commandedSpeedSlider.move(round(self.frameGeometry().width()*0.5-commandedSpeedSlider.frameGeometry().width()*0.5), round(self.frameGeometry().height()*0.5))
            commandedSpeedSlider.setParent(self)
            return commandedSpeedSlider


        # event actions

        # might use for resizing elements
        #def resizeEvent(self, event):
        #    print("window resized")
        #    emergencyBrakeEnable = self.emergencyBrakeEnable
        #    emergencyBrakeEnable.move(round(self.frameGeometry().width()/10-emergencyBrakeEnable.frameGeometry().width()/2), round(self.frameGeometry().height()/3-emergencyBrakeEnable.frameGeometry().height()/2))
        #    QMainWindow.resizeEvent(self, event)
           

        def emergencyBrakeEnableClick(self):
            print("Enable Clicked")

        def emergencyBrakeDisableClick(self):
            print("Disable Clicked")

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