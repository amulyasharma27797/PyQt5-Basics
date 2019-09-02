from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox, QVBoxLayout
import sys
from PyQt5 import QtGui
import pymysql as mdb


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Database Connection"
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

        self.btn = QPushButton("DB Connection")
        self.btn.clicked.connect(self.db_connect)
        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.show()

    def db_connect(self):
        try:
            db = mdb.connect('localhost', 'root', 'password', 'PyQt')
            QMessageBox.about(self, "Connection", "Database Connected Sucessfuly")

        except mdb.Error as e:
            QMessageBox.about(self, "Connect", "Failed to Connect to the Database")
            sys.exit()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
