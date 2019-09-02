from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QVBoxLayout, QDial, QSpinBox
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Spin Box"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()

        self.spinBox = QSpinBox()
        self.spinBox.valueChanged.connect(self.spin_changed)
        vbox.addWidget(self.spinBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def spin_changed(self):
        spinValue = self.spinBox.value()
        self.label.setText("Current Value is: " + str(spinValue))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
