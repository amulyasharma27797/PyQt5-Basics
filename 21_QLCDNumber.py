from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QVBoxLayout, QDial, QSpinBox, QLCDNumber, QPushButton
import sys
from random import randint


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QLCDNumber"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.init_ui()
        self.show()

    def init_ui(self):
        vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.display(60)
        self.lcd.setStyleSheet("background-color:green")
        vbox.addWidget(self.lcd)

        self.button = QPushButton("Random Number Generator")
        self.button.setStyleSheet("background-color:yellow")
        self.button.clicked.connect(self.lcd_handler)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def lcd_handler(self):
        random = randint(1, 200)
        self.lcd.display(random)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
