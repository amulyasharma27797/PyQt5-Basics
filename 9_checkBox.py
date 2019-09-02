from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QLabel, QCheckBox
import sys
from PyQt5 import QtGui, QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Check Box"
        self.top = 400
        self.left = 300
        self.height = 100
        self.width = 400

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_check_box()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont('Sanserif', 15))
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def create_check_box(self):
        self.groupBox = QGroupBox("What is your favorite programming language?")
        self.groupBox.setFont(QtGui.QFont('Sanserif', 13))

        hboxlayout = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon('python.png'))
        self.check1.setIconSize(QtCore.QSize(20, 20))
        self.check1.toggled.connect(self.on_checkbox_toggled)
        hboxlayout.addWidget(self.check1)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QtGui.QIcon('java.png'))
        self.check2.setIconSize(QtCore.QSize(20, 20))
        self.check2.toggled.connect(self.on_checkbox_toggled)
        hboxlayout.addWidget(self.check2)

        self.check3 = QCheckBox("C++")
        self.check3.setIcon(QtGui.QIcon('cpp.png'))
        self.check3.setIconSize(QtCore.QSize(20, 20))
        self.check3.toggled.connect(self.on_checkbox_toggled)
        hboxlayout.addWidget(self.check3)

        self.check4 = QCheckBox("C#")
        self.check4.setIcon(QtGui.QIcon('csharp.png'))
        self.check4.setIconSize(QtCore.QSize(20, 20))
        self.check4.toggled.connect(self.on_checkbox_toggled)
        hboxlayout.addWidget(self.check4)

        self.groupBox.setLayout(hboxlayout)

    def on_checkbox_toggled(self):
        if self.check1.isChecked():
            self.label.setText("You have Selected " + self.check1.text())

        if self.check2.isChecked():
            self.label.setText("You have Selected " + self.check2.text())

        if self.check3.isChecked():
            self.label.setText("You have Selected " + self.check3.text())

        if self.check4.isChecked():
            self.label.setText("You have Selected " + self.check4.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
