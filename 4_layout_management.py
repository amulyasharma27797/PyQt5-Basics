from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QHBoxLayout, QGroupBox
import sys
from PyQt5 import QtGui, QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Layout Management"
        self.height = 100
        self.width = 400
        self.top = 200
        self.left = 500

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        self.create_layout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def create_layout(self):
        self.groupBox = QGroupBox("What is your favorite sport?")
        hboxlayout = QHBoxLayout()

        button = QPushButton("Football", self)
        button.setIcon(QtGui.QIcon("football.png"))
        button.setIconSize(QtCore.QSize(20, 20))
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Cricket", self)
        button1.setIcon(QtGui.QIcon("cricket.png"))
        button1.setIconSize(QtCore.QSize(20, 20))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button2 = QPushButton("Tennis", self)
        button2.setIcon(QtGui.QIcon("tennis.png"))
        button2.setIconSize(QtCore.QSize(20, 20))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        self.groupBox.setLayout(hboxlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
