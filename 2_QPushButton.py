from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PyQt5 Push Button"
        top = 100
        left = 100
        height = 250
        width = 300
        iconName = "home.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(top, left, width, height)

        self.UiComponents()

        self.show()

    def UiComponents(self):
        button = QPushButton("Click Me", self)
        button.setGeometry(QRect(100, 100, 111, 28))
        button.setIcon(QtGui.QIcon("home.png"))
        button.setIconSize(QtCore.QSize(20, 20))
        button.setToolTip("This is click me button")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
