from PyQt6.QtCore import QObject, pyqtSignal

class trainModelSignals(QObject):

    # Train Model Main UI Signals
    commButtonPressedSignal = pyqtSignal()
    engineButtonPressedSignal = pyqtSignal()
    brakeButtonPressedSignal = pyqtSignal()
    eBrakePressedSignal = pyqtSignal()
    tempChangedSignal = pyqtSignal(float)

    # Test UI Signal
    updateOutputs = pyqtSignal()

trainSignals = trainModelSignals()

# define inside