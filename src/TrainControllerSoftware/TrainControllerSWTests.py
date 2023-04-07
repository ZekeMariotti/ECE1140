# tests file for TrainControllerSW

from distutils.cmd import Command
import sys
import json
from TrainControllerSW import TrainControllerSW
from TrainControllerMainUI import MainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    mainUI = MainWindow()
    mainUI.show()

    if (mainUI.testUI):
        mainUI.TrainControllerTestUI.show()

    app.exec()