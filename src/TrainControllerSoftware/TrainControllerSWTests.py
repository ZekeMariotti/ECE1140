# tests file for TrainControllerSW

from distutils.cmd import Command
import sys
import json

from TrainControllerSW import TrainControllerSW
from TrainControllerMainUI import MainWindow
from Integration.TMTCSignals import *
from Integration.TimeSignals import *
from TrainModelFolder.TrainModelMainUI import *
from TrainModelFolder.TrainModelTestUI import *
import Integration.Conversions as Conversions

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from datetime import *
from time import *

# Tests
passed = 0
failed = 0

# Test that emergency brake sends and receives correct signals
def emergencyBrakeCommandTest():
    try:
        mainUI.emergencyBrakeDisableClick()
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.emergencyBrakeCommand == False), "emergencyBrakeCommandTest Failed"

        mainUI.emergencyBrakeEnableClick()
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.emergencyBrakeCommand == True), "emergencyBrakeCommandTest Failed"

        mainUI.TrainControllerTestUI.setEmergencyBrakeState.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setEmergencyBrakeStateActivated()
        mainUI.mainEventLoop()
        assert ("DISABLED" in mainUI.emergencyBrakeState.text()), "emergencyBrakeCommandTest Failed"

        mainUI.TrainControllerTestUI.setEmergencyBrakeState.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setEmergencyBrakeStateActivated()
        mainUI.mainEventLoop()
        assert ("ENABLED" in mainUI.emergencyBrakeState.text()), "emergencyBrakeCommandTest Failed"
        
        print("emergencyBrakeCommandTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that service brake sends and receives correct signals
def serviceBrakeCommandTest():
    try:
        mainUI.serviceBrakeDisableClick()
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.serviceBrakeCommand == False), "serviceBrakeCommandTest Failed"
        
        mainUI.serviceBrakeEnableClick()
        mainUI.TrainControllerSW.writeOutputs()
        assert (mainUI.TrainControllerTestUI.serviceBrakeCommand == True), "serviceBrakeCommandTest Failed"

        mainUI.TrainControllerTestUI.setServiceBrakeStatus.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setServiceBrakeStatusActivated()

        mainUI.TrainControllerTestUI.setServiceBrakeState.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setServiceBrakeStateActivated()
        mainUI.mainEventLoop()
        assert ("DISABLED" in mainUI.serviceBrakeState.text()), "serviceBrakeCommandTest Failed"
        
        mainUI.TrainControllerTestUI.setServiceBrakeState.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setServiceBrakeStateActivated()
        mainUI.mainEventLoop()
        assert ("ENABLED" in mainUI.serviceBrakeState.text()), "serviceBrakeCommandTest Failed"
        
        print("serviceBrakeCommandTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that the RTC is received correctly
def realTimeClockTest():
    try:
        mainUI.TrainControllerTestUI.setRealTime.setDateTime(QDateTime(2023, 4, 19, 12, 23, 47, 122))
        mainUI.mainEventLoop()
        assert(mainUI.realTimeClock.text() == (f'Time: {mainUI.TrainControllerTestUI.setRealTime.time().hour()}:{mainUI.TrainControllerTestUI.setRealTime.time().minute()}:{mainUI.TrainControllerTestUI.setRealTime.time().second()}')), "realTimeClockTest Failed"
        
        print("realTimeClockTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that engine state is set properly
def engineStateTest():
    try:
        mainUI.TrainControllerTestUI.setEngineStatus.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.engineStatusActivated()
        mainUI.mainEventLoop()
        assert("FAILURE" in mainUI.engineState.text()), "engineStateTest Failed"

        mainUI.TrainControllerTestUI.setEngineStatus.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.engineStatusActivated()
        mainUI.mainEventLoop()
        assert("ON" in mainUI.engineState.text()), "engineStateTest Failed"

        print("engineStateTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that lights send and receive correct signals
def lightsTest():
    try:
        mainUI.internalLightsEnableClick()
        mainUI.externalLightsEnableClick()
        mainUI.mainEventLoop()
        assert((mainUI.TrainControllerTestUI.internalLightCommand and mainUI.TrainControllerTestUI.externalLightCommand) == True), "lightsTest Failed"

        mainUI.internalLightsDisableClick()
        mainUI.externalLightsDisableClick()
        mainUI.mainEventLoop()
        assert((mainUI.TrainControllerTestUI.internalLightCommand and mainUI.TrainControllerTestUI.externalLightCommand) == False), "lightsTest Failed"

        mainUI.TrainControllerTestUI.setInternalLightState.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setExternalLightState.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setInternalLightStateActivated()
        mainUI.TrainControllerTestUI.setExternalLightStateActivated()
        mainUI.mainEventLoop()
        assert(("OFF" in mainUI.internalLightsState.text()) and ("OFF" in mainUI.externalLightsState.text())), "lightsTest Failed"

        mainUI.TrainControllerTestUI.setInternalLightState.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setExternalLightState.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setInternalLightStateActivated()
        mainUI.TrainControllerTestUI.setExternalLightStateActivated()
        mainUI.mainEventLoop()
        assert(("ON" in mainUI.internalLightsState.text()) and ("ON" in mainUI.externalLightsState.text())), "lightsTest Failed"
        
        print("lightsTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that doors send and receive correct signals
def doorTest():
    try:
        mainUI.leftDoorCloseClick()
        mainUI.rightDoorCloseClick()
        mainUI.TrainControllerSW.writeOutputs()
        assert((mainUI.TrainControllerTestUI.leftDoorCommand and mainUI.TrainControllerTestUI.rightDoorCommand) == False), "doorTest Failed"

        mainUI.leftDoorOpenClick()
        mainUI.rightDoorOpenClick()
        mainUI.TrainControllerSW.writeOutputs()
        assert((mainUI.TrainControllerTestUI.leftDoorCommand and mainUI.TrainControllerTestUI.rightDoorCommand) == True), "doorTest Failed"

        mainUI.TrainControllerTestUI.setLeftDoorState.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setRightDoorState.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setLeftDoorStateActivated()
        mainUI.TrainControllerTestUI.setRightDoorStateActivated()
        mainUI.mainEventLoop()
        assert(("Closed" in mainUI.leftDoorState.text()) and ("Closed" in mainUI.rightDoorState.text())), "doorTest Failed"

        mainUI.TrainControllerTestUI.setLeftDoorState.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setRightDoorState.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setLeftDoorStateActivated()
        mainUI.TrainControllerTestUI.setRightDoorStateActivated()
        mainUI.mainEventLoop()
        assert(("Opened" in mainUI.leftDoorState.text()) and ("Opened" in mainUI.rightDoorState.text())), "doorTest Failed"

        
        print("doorTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that station names work properly
def stationTest():
    try:
        # Sets station state to true
        mainUI.TrainControllerTestUI.setIsBeacon.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setIsBeaconActivated()
        mainUI.mainEventLoop()
        mainUI.TrainControllerTestUI.setIsBeacon.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setIsBeaconActivated()
        mainUI.mainEventLoop()

        mainUI.TrainControllerTestUI.setStationName.setText("testStation23")
        mainUI.TrainControllerTestUI.setStationNameTextChanged()
        mainUI.mainEventLoop()
        assert("Current Station:" in mainUI.station.text()), "stationTest Failed"
        assert("testStation23" in mainUI.station.text()), "stationTest Failed"

        # Sets station state to false
        mainUI.TrainControllerTestUI.setIsBeacon.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setIsBeaconActivated()
        mainUI.mainEventLoop()
        mainUI.TrainControllerTestUI.setIsBeacon.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setIsBeaconActivated()
        mainUI.mainEventLoop()

        mainUI.TrainControllerTestUI.setStationName.setText("testStation52")
        mainUI.TrainControllerTestUI.setStationNameTextChanged()
        mainUI.mainEventLoop()
        assert("Next Station:" in mainUI.station.text()), "stationTest Failed"
        assert("testStation52" in mainUI.station.text()), "stationTest Failed"

        print("stationTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that current speed is received correctly
def currentSpeedTest():
    try:
        mainUI.TrainControllerTestUI.currentSpeedSlider.setValue(20)
        mainUI.TrainControllerTestUI.currentSpeedSliderRelease()
        mainUI.mainEventLoop()
        assert(str(Conversions.metersPerSecondToMilesPerHour(20)) in mainUI.currentSpeed.text()), "currentSpeedTest Failed"

        print("currentSpeedTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that the communications error is displayed correctly
def communicationsFailureTest():
    try:
        mainUI.TrainControllerTestUI.setCommunicationsStatus.setCurrentIndex(0)
        mainUI.TrainControllerTestUI.setCommunicationsStatusActivated()
        mainUI.mainEventLoop()
        assert(mainUI.communicationsError.isVisible() == True), "communicationsFailureTest Failed"

        mainUI.TrainControllerTestUI.setCommunicationsStatus.setCurrentIndex(1)
        mainUI.TrainControllerTestUI.setCommunicationsStatusActivated()
        mainUI.mainEventLoop()
        assert(mainUI.communicationsError.isVisible() == False), "communicationsFailureTest Failed"

        print("communicationsFailureTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that manual mode switch is set properly
def manualModeTest():
    try:
        mainUI.manualModeToggle.setChecked(False)
        mainUI.mainEventLoop()
        assert(mainUI.manualModeToggle.isChecked() == False), "manualModeTest Failed"

        mainUI.manualModeToggle.setChecked(True)
        mainUI.mainEventLoop()
        assert(mainUI.manualModeToggle.isChecked() == True), "manualModeTest Failed"

        print("manualModeTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that commanded speed can be set correctly in manual mode
def commandedSpeedSliderTest():
    try:
        mainUI.manualModeToggle.setChecked(True)
        mainUI.mainEventLoop()

        mainUI.commandedSpeedSlider.setValue(20)
        mainUI.commandedSpeedSliderValueChanged()
        mainUI.mainEventLoop()
        assert(mainUI.TrainControllerSW.commandedSpeedManual == Conversions.kmPerHourToMetersPerSecond(20)), "commandedSpeedSliderTest Failed"

        assert(str(Conversions.metersPerSecondToMilesPerHour(Conversions.kmPerHourToMetersPerSecond(20))) in mainUI.commandedSpeed.text()), "commandedSpeedSliderTest Failed"

        print("commandedSpeedSliderTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that commanded speed is received and shown correctly in automatic mode
def commandedSpeedTest():
    try:
        # Set authority to 5 and manual mode to false to prevent commanded speed from being set automatically
        mainUI.TrainControllerSW.inputs.authority = 5
        mainUI.manualModeToggle.setChecked(False)
        mainUI.mainEventLoop()

        mainUI.TrainControllerTestUI.commandedSpeedSlider.setValue(5)
        mainUI.TrainControllerTestUI.commandedSpeedSliderRelease()
        mainUI.mainEventLoop()
        assert(str(Conversions.metersPerSecondToMilesPerHour(5)) in mainUI.commandedSpeed.text()), "commandedSpeedTest Failed"

        print("commandedSpeedTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that authority is received and shown correctly
def authorityTest():
    try:
        mainUI.TrainControllerTestUI.setAuthority.setText("12")
        mainUI.TrainControllerTestUI.setAuthorityTextChanged()
        mainUI.mainEventLoop()
        assert("12" in mainUI.authority.text()), "authorityTest Failed"

        print("authorityTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1
 
# Test that speed limit is set properly 
def speedLimitTest():
    try:
        mainUI.TrainControllerSW.blockCount = 1
        speedLimit = str(Conversions.metersPerSecondToMilesPerHour(Conversions.kmPerHourToMetersPerSecond(mainUI.TrainControllerSW.blockList[1].speedLimit)))
        assert(speedLimit in mainUI.speedLimit.text()), "speedLimitTest Failed"

        print("speedLimitTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that temperature is received and shown correctly
def temperatureTest():
    try:
        mainUI.TrainControllerTestUI.setTemperature.setValue(25)
        mainUI.TrainControllerTestUI.setTemperatureValueChanged()
        mainUI.mainEventLoop()
        assert("25" in mainUI.temperature.text()), "temperatureTest Failed"
        
        print("temperatureTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1

# Test that Kp and Ki can be set correctly
def kpAndKiTest():
    try:
        mainUI.Kp.setText("123")
        mainUI.Ki.setText("321")
        mainUI.mainEventLoop()
        assert((mainUI.TrainControllerSW.Kp == 123) and (mainUI.TrainControllerSW.Ki == 321)), "kpAndKiTest Failed"

        print("kpAndKiTest Passed")
        global passed
        passed = passed + 1
    except Exception as exception:
        print(str(exception))
        global failed
        failed = failed + 1


if (__name__ == "__main__"):
    # Used to test TrainModel communication
    testTrainModelIntegration = False

    app = QApplication(sys.argv)
    mainUI = MainWindow("Green", 2)
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
    stationTest()
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

    if (testTrainModelIntegration == True):
        trainModelUI = TrainModelUI(2, "Green")
        trainModelUI.show()

        trainModelTestUI = TrainModelTestUI()
        trainModelTestUI.show()

    app.exec()