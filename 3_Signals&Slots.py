from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Signals and Slots"
        height = 250
        width = 300
        top = 200
        left = 200

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.CreateButton()

        self.show()

    def CreateButton(self):
        button = QPushButton("Close", self)
        button.setGeometry(QRect(100, 100, 111, 28))
        button.setIcon(QtGui.QIcon("home.png"))
        button.clicked.connect(self.ClickMe)

    def ClickMe(self):
        sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
