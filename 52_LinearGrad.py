from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon, QLinearGradient
from PyQt5.QtCore import Qt, QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Linear Gradient"
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

        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))

        grad1 = QLinearGradient(20, 100, 150, 175)

        grad1.setColorAt(0.0, Qt.darkGray)
        grad1.setColorAt(0.5, Qt.green)
        grad1.setColorAt(1.0, Qt.yellow)

        painter.setBrush(QBrush(grad1))

        painter.drawRect(10, 10, 200, 200)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
