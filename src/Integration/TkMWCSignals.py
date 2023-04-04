from PyQt6.QtCore import QObject, pyqtSignal

class trackModelWaysideControllerSignals(QObject):
    # Wayside to track model
    authoritySignal = pyqtSignal(int, int)
    commandedSpeedSignal = pyqtSignal(int, float)
    switchStateSignal = pyqtSignal(int, int)
    signalStateSignal = pyqtSignal(int, int)
    gateStateInput = pyqtSignal(int, int)

    # Track Model to Wayide
    failureSignal = pyqtSignal(int, bool)
    currBlockSignal = pyqtSignal(int, bool)

TkMWCSignals = trackModelWaysideControllerSignals()