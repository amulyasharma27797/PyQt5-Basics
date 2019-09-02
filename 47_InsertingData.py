from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLineEdit, QDialog, QPushButton, QMessageBox
import sys
from PyQt5 import QtGui
import pymysql as mdb


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Inserting Data"
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

        self.name = QLineEdit()
        self.name.setPlaceholderText("Please Enter Your Name")
        self.name.setStyleSheet('background:yellow')
        self.name.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.name)

        self.email = QLineEdit()
        self.email.setPlaceholderText("Please Enter Your Email")
        self.email.setStyleSheet('background:yellow')
        self.email.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.email)

        self.btn = QPushButton("Insert Data")
        self.btn.setStyleSheet('background:green')
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.insert_data)

        vbox.addWidget(self.btn)

        self.setLayout(vbox)

        self.show()

    def insert_data(self):
        con = mdb.connect('localhost', 'root', 'password', 'PyQt')

        with con:
            cur = con.cursor()

            cur.execute("INSERT INTO data(name, email)"
                        "VALUES('%s', '%s')" % (''.join(self.name.text()),
                                            ''.join(self.email.text())))
            # cur.save()

            QMessageBox.about(self, "Inserted", "Data Inserted Successfully")
            self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
