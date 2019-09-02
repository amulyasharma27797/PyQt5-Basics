from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout, QLabel
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 WhatIsThis class"
        self.left = 500
        self.top = 200
        self.height = 250
        self.width = 300

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        label = QLabel("Focus and Press SHIFT + F1")
        hbox.addWidget(label)

        button = QPushButton("Click Me", self)
        button.setWhatsThis("This is click me button")
        button.clicked.connect(self.clickme)
        hbox.addWidget(button)

        self.setLayout(hbox)

        self.show()

    def clickme(self):
        sys.exit()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
