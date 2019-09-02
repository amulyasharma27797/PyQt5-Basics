from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QTableWidget"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.creating_tables()
        self.show()

    def creating_tables(self):

        vbox = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(3)

        tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        tableWidget.setItem(0, 1, QTableWidgetItem("Email"))
        tableWidget.setItem(0, 2, QTableWidgetItem("Phone No."))

        tableWidget.setItem(1, 0, QTableWidgetItem("John"))
        tableWidget.setItem(1, 1, QTableWidgetItem("john@gmail.com"))
        tableWidget.setItem(1, 2, QTableWidgetItem("8756985214"))

        tableWidget.setItem(2, 0, QTableWidgetItem("Happy"))
        tableWidget.setItem(2, 1, QTableWidgetItem("happy@gmail.com"))
        tableWidget.setItem(2, 2, QTableWidgetItem("8756985215"))

        vbox.addWidget(tableWidget)

        self.setLayout(vbox)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
