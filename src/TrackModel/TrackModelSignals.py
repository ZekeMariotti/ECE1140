from PyQt6.QtCore import QObject, pyqtSignal

class trackModelSignals(QObject):
    blockTrainNumber = pyqtSignal([int, int, int, int, int, int, int, int, int, int, int, int, int, int, int])
    
    powerPressedSignal = pyqtSignal()
    brokenRailPressedSignal = pyqtSignal()
    trackCircuitPressedSignal = pyqtSignal()
    testUIFloatSignal = pyqtSignal(float)
    testUIIntSignal = pyqtSignal(int)
    testUIBoolSignal = pyqtSignal(int)

trackSignals = trackModelSignals()
