from PyQt6.QtCore import QObject, pyqtSignal

class trackModelSignals(QObject):
    updateSignal = pyqtSignal()
    getSwitchPositionInput = pyqtSignal(int, int, int)
    getGatePositionInput = pyqtSignal(int, int, int)
    getSignalStateInput = pyqtSignal(int, int, int)
    getTempInput = pyqtSignal(float)
    getTrackHeaterInput = pyqtSignal(int)
    getStationOccInput = pyqtSignal(int)
    getTrainBlockInputSignal = pyqtSignal(int, int)
    getTrainLnInput = pyqtSignal(int, int)
    trainChange = pyqtSignal(int)
    getOffInput = pyqtSignal(int, int, int)
    getOnInput = pyqtSignal(int, int)
    getAuthInput = pyqtSignal(int, int)
    getCSpeedInput = pyqtSignal(int, int)
    getRealTimeClockInput = pyqtSignal(str)


    
    powerPressedSignal = pyqtSignal()
    brokenRailPressedSignal = pyqtSignal()
    trackCircuitPressedSignal = pyqtSignal()
    testUIFloatSignal = pyqtSignal(float)
    testUIIntSignal = pyqtSignal(int)
    testUIBoolSignal = pyqtSignal(int)

trackSignals = trackModelSignals()
