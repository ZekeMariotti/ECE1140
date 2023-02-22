from PyQt6.QtCore import QObject, pyqtSignal

class trainModelSignals(QObject):

    # Train Model Main UI Signals
    commButtonPressedSignal = pyqtSignal()
    engineButtonPressedSignal = pyqtSignal()
    brakeButtonPressedSignal = pyqtSignal()
    eBrakePressedSignal = pyqtSignal()
    tempChangedSignal = pyqtSignal(float)
    eBrakeToTestUI = pyqtSignal(bool)
    velocityToTestUI = pyqtSignal(float)

    # Train Model Test UI Signals
    power = pyqtSignal(float)
    serviceBrake = pyqtSignal(bool)
    emergencyBrake = pyqtSignal(bool)
    leftDoors = pyqtSignal()
    rightDoors = pyqtSignal()
    internalLights = pyqtSignal()
    externalLights = pyqtSignal()
    stationLabel = pyqtSignal(str)
    realTimeClock = pyqtSignal(str)
    passengersEntering = pyqtSignal(int)
    elevation = pyqtSignal(float)
    underground = pyqtSignal()
    stationState = pyqtSignal()
    blockLength = pyqtSignal(float)
    updateOutputs = pyqtSignal()
    communicationsFailure = pyqtSignal()
    sBrakeFailure = pyqtSignal()
    passengersOff = pyqtSignal(int)

trainSignals = trainModelSignals()