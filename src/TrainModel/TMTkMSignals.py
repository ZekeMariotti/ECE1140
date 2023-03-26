from PyQt6.QtCore import QObject, pyqtSignal

class trainModelTrackModelSignals(QObject):
    # Train Model to Track Model Signals
    passengersExitingSignal = pyqtSignal(int, int)
    currBlockSignal = pyqtSignal(int, int)
    prevBlockSignal = pyqtSignal(int, int)
    
    # Track Model to Train Model Signals
    authoritySignal = pyqtSignal(int, int)
    commandedSpeedSignal = pyqtSignal(int, float)
    passengersEnteringSignal = pyqtSignal(int, int)
    beaconSignal = pyqtSignal(int, str, int, str, bool)
    switchSignal = pyqtSignal(int, bool)
    switchStateSignal = pyqtSignal(int, bool)
    blockLengthSignal = pyqtSignal(int, float)
    elevtaionSignal = pyqtSignal(int, float)