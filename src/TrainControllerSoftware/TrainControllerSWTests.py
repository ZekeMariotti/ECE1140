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
from datetime import *
from time import *

# Tests
passed = 0
failed = 0

# Test that emergency brake command sends correct signal
def emergencyBrakeCommandTest():
    try:
        mainUI.TrainControllerSW.outputs.emergencyBrakeCommand = False
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.emergencyBrakeCommand == False), "emergencyBrakeCommandTest Failed"

        mainUI.TrainControllerSW.outputs.emergencyBrakeCommand = True
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.emergencyBrakeCommand == True), "emergencyBrakeCommandTest Failed"
        print("emergencyBrakeCommandTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that service brake command sends correct signal
def serviceBrakeCommandTest():
    try:
        mainUI.TrainControllerSW.outputs.serviceBrakeCommand = False
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.serviceBrakeCommand == False), "serviceBrakeCommandTest Failed"

        mainUI.TrainControllerSW.outputs.serviceBrakeCommand = True
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.serviceBrakeCommand == True), "serviceBrakeCommandTest Failed"
        print("serviceBrakeCommandTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def realTimeClockTest():
    try:
        time = datetime.now()
        mainUI.TrainControllerTestUI.setRealTime.setDateTime(time)
        sleep(1)
        
        print(f'Time: {time.hour}:{time.minute}:{time.second}')
        print(mainUI.realTimeClock.text())

        assert(mainUI.realTimeClock.text() == (f'Time: {time.hour}:{time.minute}:{time.second}')), "realTimeClockTest Failed"
        print("realTimeClockTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def engineStateTest():
    try:
        assert(), "engineStateTest Failed"
        print("engineStateTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def lightsTest():
    try:
        assert(), "lightsTest Failed"
        print("lightsTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def doorTest():
    try:
        assert(), "doorTest Failed"
        print("doorTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def nextStationTest():
    try:
        assert(), "nextStationTest Failed"
        print("nextStationTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def currentSpeedTest():
    try:
        assert(), "currentSpeedTest Failed"
        print("currentSpeedTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def communicationsFailureTest():
    try:
        assert(), "communicationsFailureTest Failed"
        print("communicationsFailureTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def manualModeTest():
    try:
        assert(), "manualModeTest Failed"
        print("manualModeTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def commandedSpeedSliderTest():
    try:
        assert(), "commandedSpeedSliderTest Failed"
        print("commandedSpeedSliderTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def commandedSpeedTest():
    try:
        assert(), "commandedSpeedTest Failed"
        print("commandedSpeedTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def authorityTest():
    try:
        assert(), "authorityTest Failed"
        print("authorityTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def speedLimitTest():
    try:
        assert(), "speedLimitTest Failed"
        print("speedLimitTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def temperatureTest():
    try:
        assert(), "temperatureTest Failed"
        print("temperatureTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# 
def kpAndKiTest():
    try:
        assert(), "kpAndKiTest Failed"
        print("kpAndKiTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1


if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    mainUI = MainWindow()
    mainUI.show()

    if (mainUI.testUI):
        mainUI.TrainControllerTestUI.show()

    print("")

    # Test that the Test UI is created
    assert (mainUI.testUI == True), "Test UI must be enabled (self.testUI = True)"

    # Run tests
    emergencyBrakeCommandTest()
    serviceBrakeCommandTest()
    realTimeClockTest()
    engineStateTest()
    lightsTest()
    doorTest()
    nextStationTest()
    currentSpeedTest()
    communicationsFailureTest()
    manualModeTest()
    commandedSpeedSliderTest()
    commandedSpeedTest()
    authorityTest()
    speedLimitTest()
    temperatureTest()
    kpAndKiTest()
    
    print(f'\nTotal Tests: {passed+failed}\nTests passed: {passed}\nTests Failed: {failed}')
    app.exec()