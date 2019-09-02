from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QRadioButton
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QGroupBox"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        groupbox = QGroupBox("Select your Favorite Fruit")
        groupbox.setFont(QtGui.QFont("Sanserif", 15))
        hbox.addWidget(groupbox)

        vbox = QVBoxLayout()

        rad1 = QRadioButton("Apple")
        vbox.addWidget(rad1)

        rad2 = QRadioButton("Banana")
        vbox.addWidget(rad2)

        rad3 = QRadioButton("Melon")
        vbox.addWidget(rad3)

        groupbox.setLayout(vbox)
        self.setLayout(hbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
