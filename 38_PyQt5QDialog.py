from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QDialog
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Dialog in Dialog"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        self.btn = QPushButton("Open Second Dialog")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.open_second_dialog)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.show()

    def open_second_dialog(self):
        mydialog = QDialog()
        # mydialog.setModal(True)
        # mydialog.exec()

        mydialog.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
