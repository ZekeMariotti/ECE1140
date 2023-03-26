from PyQt6.QtCore import QObject, pyqtSignal

class trainModelTrackModelSignals(QObject):
    # Train Model to Track Model Signals
    passengersExitingSignal = pyqtSignal(int)
    currBlockSignal = pyqtSignal(int)
    prevBlockSignal = pyqtSignal(int)
    
    # Track Model to Train Model Signals
    authoritySignal = pyqtSignal(int)
    commandedSpeedSignal = pyqtSignal(float)
    passengersEnteringSignal = pyqtSignal(int)
    beaconSignal = pyqtSignal(str, int, str, bool)
    switchSignal = pyqtSignal(bool)
    switchStateSignal = pyqtSignal(bool)
    blockLengthSignal = pyqtSignal(float)
    elevtaionSignal = pyqtSignal(float)