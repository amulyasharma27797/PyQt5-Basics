from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QStackedWidget, QLabel, QMainWindow, \
    QComboBox, QCompleter, QLineEdit
import sys
from PyQt5 import QtGui


class StackWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Completer"
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
        names = ["Afghanistan", "India", "Pakistan", "Japan", "Indonesia", "China", "UAE", "America"]
        completer = QCompleter(names)

        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        vbox.addWidget(self.lineedit)

        self.setLayout(vbox)


App = QApplication(sys.argv)
window = StackWidget()
sys.exit(App.exec())


