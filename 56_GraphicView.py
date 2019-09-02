from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QGraphicsItem
import sys
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Graphic View"
        self.top = 100
        self.left = 100
        self.width = 600
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_graphic_view()
        self.show()

    def create_graphic_view(self):
        self.scene = QGraphicsScene()

        self.greenBrush = QBrush(Qt.green)
        self.grayBrush = QBrush(Qt.gray)

        self.pen = QPen(Qt.red)

        graphicView = QGraphicsView(self.scene, self)
        graphicView.setGeometry(0, 0, 600, 500)

        self.shapes()

    def shapes(self):
        ellipse = self.scene.addEllipse(20, 20, 200, 200, self.pen, self.greenBrush)
        rect = self.scene.addRect(-100, -100, 200, 200, self.pen, self.grayBrush)

        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)
        ellipse.setFlag(QGraphicsItem.ItemIsSelectable)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
