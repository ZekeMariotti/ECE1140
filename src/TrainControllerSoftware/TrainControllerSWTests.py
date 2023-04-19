# tests file for TrainControllerSW

from distutils.cmd import Command
import sys
import json

from TrainControllerSW import TrainControllerSW
from TrainControllerMainUI import MainWindow
from Integration.TMTCSignals import *
from Integration.TimeSignals import *

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# Tests
def emergencyBrakeCommandTest():
    try:
        mainUI.TrainControllerSW.outputs.emergencyBrakeCommand = False
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.emergencyBrakeCommand == False), "emergencyBrakeCommandTest Failed"

        mainUI.TrainControllerSW.outputs.emergencyBrakeCommand = True
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.emergencyBrakeCommand == True), "emergencyBrakeCommandTest Failed"
        print("emergencyBrakeCommandTest Passed")
    except Exception as exception:
        print(str(exception))

def serviceBrakeCommandTest():
    try:
        mainUI.TrainControllerSW.outputs.serviceBrakeCommand = False
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.serviceBrakeCommand == False), "serviceBrakeCommandTest Failed"

        mainUI.TrainControllerSW.outputs.serviceBrakeCommand = True
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.serviceBrakeCommand == True), "serviceBrakeCommandTest Failed"
        print("serviceBrakeCommandTest Passed")
    except Exception as exception:
        print(str(exception))


if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    mainUI = MainWindow()
    mainUI.show()

    if (mainUI.testUI):
        mainUI.TrainControllerTestUI.show()

    print("")

    # Test that the Test UI is created
    assert (mainUI.testUI == True), "Test UI must be enabled (self.testUI = True)"

    # Test that emergency brake command sends correct signal
    emergencyBrakeCommandTest()

    # Test that service brake command sends correct signal
    serviceBrakeCommandTest()
    
    print("")
    app.exec()