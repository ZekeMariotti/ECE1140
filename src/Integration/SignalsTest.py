from TrainControllerMainUI import *
from TrainModelMainUI import *
from TrainModelTestUI import *

if __name__ == "__main__":
    app = QApplication(argv)
    testUI = TrainModelTestUI()
    testUI.show()
    mainUI = TrainModelUI(2, "Green")
    mainUI.show()
    #mainUI2 = TrainModelUI(3, "Green")
    #mainUI2.show()
    trainCont = MainWindow(2)
    trainCont.show()
    #trainCont2 = MainWindow(3)
    #trainCont2.show()
    app.exec()