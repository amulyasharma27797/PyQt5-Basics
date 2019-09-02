from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout, QLabel, QLineEdit
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

        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont('Sanserif', 15))
        self.lineedit.returnPressed.connect(self.on_pressed)
        hbox.addWidget(self.lineedit)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont('Sanserif', 15))
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()

    def on_pressed(self):
        self.label.setText(self.lineedit.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
