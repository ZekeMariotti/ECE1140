from sys import argv
from PyQt6.QtWidgets import QWidget, QLabel, QApplication

class BasicForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupGUI()

    def setupGUI(self):
        self.label = QLabel("HELLO WORLD!\n")
        self.label.setParent(self)

if __name__ == "__main__":
    app = QApplication(argv)

    form = BasicForm()
    form.show()

    app.exec()