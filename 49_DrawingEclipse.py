from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Eclipse"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))

        # painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))

        painter.drawEllipse(100, 15, 400, 200)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
