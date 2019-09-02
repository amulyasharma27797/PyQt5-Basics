from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen, QConicalGradient, QTextDocument
from PyQt5.QtCore import Qt, QPoint, QRect, QRectF


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Conical Gradient"
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

        painter.drawText(100, 100, "Hello PyQt5 App Development")

        rect = QRectF(100, 150, 250, 25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignCenter, "Hello World")

        document = QTextDocument()
        rect2 = QRectF(0, 0, 250, 250)
        document.setTextWidth(rect2.width())
        document.setHtml("<b>Python GUI</b> <i>Development</i> <font size='10' color='red'>Complete Series</font>")

        document.drawContents(painter, rect2)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
