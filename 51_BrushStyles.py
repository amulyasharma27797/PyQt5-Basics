from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Brush Styles"
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
        painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))
        painter.drawRect(10, 100, 150, 100)

        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense1Pattern))
        painter.drawRect(180, 100, 150, 100)

        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.HorPattern))
        painter.drawRect(350, 100, 150, 100)

        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.VerPattern))
        painter.drawRect(10, 220, 150, 100)

        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.BDiagPattern))
        painter.drawRect(180, 100, 150, 100)

        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense3Pattern))
        painter.drawRect(180, 220, 150, 100)

        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense4Pattern))
        painter.drawRect(10, 340, 150, 100)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
