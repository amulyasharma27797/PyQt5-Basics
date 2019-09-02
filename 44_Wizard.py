from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QWizard
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Wizard"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        button = QPushButton("Launch")
        button.clicked.connect(self.btn_clicked)

        vbox.addWidget(button)

        self.setLayout(vbox)

        self.wizard = QWizard()
        self.wizard.setWindowTitle("Launching...")

        self.show()

    def btn_clicked(self):
        self.wizard.open()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
