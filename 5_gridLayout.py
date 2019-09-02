from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QGroupBox, QGridLayout
import sys
from PyQt5 import QtGui, QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Grid Layout"
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
        self.groupBox = QGroupBox("What is your favorite programming language?")
        gridlayout = QGridLayout()

        button = QPushButton("Python", self)
        button.setIcon(QtGui.QIcon("python.png"))
        button.setIconSize(QtCore.QSize(20, 20))
        button.setMinimumHeight(40)
        gridlayout.addWidget(button, 0, 0)

        button1 = QPushButton("C++", self)
        button1.setIcon(QtGui.QIcon("cpp.png"))
        button1.setIconSize(QtCore.QSize(20, 20))
        button1.setMinimumHeight(40)
        gridlayout.addWidget(button1, 0, 1)

        button2 = QPushButton("Java", self)
        button2.setIcon(QtGui.QIcon("java.png"))
        button2.setIconSize(QtCore.QSize(20, 20))
        button2.setMinimumHeight(40)
        gridlayout.addWidget(button2, 1, 0)

        button3 = QPushButton("C#", self)
        button3.setIcon(QtGui.QIcon("csharp.png"))
        button3.setIconSize(QtCore.QSize(20, 20))
        button3.setMinimumHeight(40)
        gridlayout.addWidget(button3, 1, 1)

        self.groupBox.setLayout(gridlayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
