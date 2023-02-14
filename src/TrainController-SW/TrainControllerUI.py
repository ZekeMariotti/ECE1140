# Main UI for the Train Controller Software

from distutils.cmd import Command
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QSlider, QVBoxLayout, QLabel
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor

# Class for the main window
class MainWindow(QMainWindow):

        # Constructor 
        def __init__(self):
                super().__init__()

                self.setWindowTitle("Train Controller")
                self.resize(QSize(1200, 900))
                self.setMinimumSize(QSize(600, 450))

               # layout = QVBoxLayout()                
                
                emergencyBrakeEnable = self.emergencyBrakeEnableSetup()
                commandedSpeedSlider = self.commandedSpeedSliderSetup()                

        # widget setups
        def emergencyBrakeEnableSetup(self):
            emergencyBrakeEnable = QPushButton("Enable Emergency Brake")
            emergencyBrakeEnable.setFixedSize(QSize(175, 50))
            emergencyBrakeEnable.move(500, 500)
            emergencyBrakeEnable.clicked.connect(self.emergencyBrakeEnableClick)
            emergencyBrakeEnable.move(500, 300)
            emergencyBrakeEnable.setParent(self)
            return emergencyBrakeEnable

        def commandedSpeedSliderSetup(self):
            commandedSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            commandedSpeedSlider.setFixedSize(500, 40)
            commandedSpeedSlider.setRange(0, 100)
            commandedSpeedSlider.setSingleStep(1)
            commandedSpeedSlider.move(500, 400)
            commandedSpeedSlider.setParent(self)
            return commandedSpeedSlider


        # event actions
        def emergencyBrakeEnableClick(self):
            print("Button Clicked")

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