from PyQt6.QtCore import QObject, pyqtSignal

class trainModelTrackModelSignals(QObject):
    passengersExitingSignal = pyqtSignal(int, int)
    currBlockSignal = pyqtSignal(int, int)

    authoritySignal = pyqtSignal(int, int)
    commandedSpeedSignal = pyqtSignal(int, float)
    passengersEnteringSignal = pyqtSignal(int, int)
    undergroundStateSignal = pyqtSignal(int, bool)
    beaconSignal = pyqtSignal(int, str, int, str, bool, int, bool)
    switchSignal = pyqtSignal(int, int)
    switchStateSignal = pyqtSignal(int, int)
    blockLengthSignal = pyqtSignal(int, float)
    elevationSignal = pyqtSignal(int, float)

TMTkMSignals = trainModelTrackModelSignals()