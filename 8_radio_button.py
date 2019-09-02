from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QLabel
import sys
from PyQt5 import QtGui, QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Radio Button"
        self.top = 400
        self.left = 300
        self.height = 100
        self.width = 400

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.radio_button()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont('Sanserif', 15))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def radio_button(self):
        self.groupBox = QGroupBox("What is your favorite sport?")
        self.groupBox.setFont(QtGui.QFont('Sanserif', 13))

        hboxlayout = QHBoxLayout()

        self.radiobtn1 = QRadioButton("Football")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.setIcon(QtGui.QIcon('football.png'))
        self.radiobtn1.setIconSize(QtCore.QSize(20, 20))
        self.radiobtn1.setFont(QtGui.QFont('Sanserif', 13))
        self.radiobtn1.toggled.connect(self.on_radio_button)
        hboxlayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("Cricket")
        self.radiobtn2.setIcon(QtGui.QIcon('cricket.png'))
        self.radiobtn2.setIconSize(QtCore.QSize(20, 20))
        self.radiobtn2.setFont(QtGui.QFont('Sanserif', 13))
        self.radiobtn2.toggled.connect(self.on_radio_button)
        hboxlayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("Tennis")
        self.radiobtn3.setIcon(QtGui.QIcon('tennis.png'))
        self.radiobtn3.setIconSize(QtCore.QSize(20, 20))
        self.radiobtn3.setFont(QtGui.QFont('Sanserif', 13))
        self.radiobtn3.toggled.connect(self.on_radio_button)
        hboxlayout.addWidget(self.radiobtn3)

        self.groupBox.setLayout(hboxlayout)

    def on_radio_button(self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("You have selected " + radioBtn.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
