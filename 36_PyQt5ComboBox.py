from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QStackedWidget, QLabel, QMainWindow, \
    QComboBox
import sys
from PyQt5 import QtGui


class StackWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Stacked Widget"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.InitWindow()

        self.show()

    def InitWindow(self):
        vbox = QVBoxLayout()

        self.combo = QComboBox()
        self.combo.addItem("Python")
        self.combo.addItem("Java")
        self.combo.addItem("C++")
        self.combo.addItem("C#")
        self.combo.addItem("Ruby")

        self.combo.currentTextChanged.connect(self.combo_changed)

        self.label = QLabel()
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.setStyleSheet('color:red')

        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def combo_changed(self):
        text = self.combo.currentText()
        self.label.setText("You have selected : " + str(text))


App = QApplication(sys.argv)
window = StackWidget()
sys.exit(App.exec())
