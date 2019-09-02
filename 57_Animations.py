from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame
import sys
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Animations"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton("Start", self)
        self.button.move(30, 30)
        self.button.clicked.connect(self.animate)

        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.setGeometry(150, 30, 100, 100)

        self.show()

    def animate(self):
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(0, 0, 100, 30))
        self.anim.setEndValue((QRect(250, 250, 100, 30)))
        self.anim.start()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
