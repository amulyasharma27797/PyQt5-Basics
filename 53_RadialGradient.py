from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon, QLinearGradient, QRadialGradient
from PyQt5.QtCore import Qt, QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Radial Gradient"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)

        painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))

        radial = QRadialGradient(QPoint(100, 100), 100)

        radial.setColorAt(0.4, Qt.white)
        radial.setColorAt(0.8, Qt.green)
        radial.setColorAt(1.0, Qt.black)

        painter.setBrush(QBrush(radial))

        painter.drawRect(0, 0, 200, 200)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
