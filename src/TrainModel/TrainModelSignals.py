from PyQt6.QtCore import QObject, pyqtSignal

class trainModelSignals(QObject):
    # Train Model Test UI Signals
    power = pyqtSignal(float)
    serviceBrake = pyqtSignal()
    emergencyBrake = pyqtSignal()
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

    # Train Model Main UI Signals
    commButtonPressedSignal = pyqtSignal()
    engineButtonPressedSignal = pyqtSignal()
    brakeButtonPressedSignal = pyqtSignal()
    eBrakePressedSignal = pyqtSignal()
    tempChangedSignal = pyqtSignal(float)

trainSignals = trainModelSignals()