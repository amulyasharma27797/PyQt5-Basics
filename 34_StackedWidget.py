from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout, QStackedWidget, QLabel
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

        self.stacked_widget()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def stacked_widget(self):

        vbox = QVBoxLayout()

        self.stackedWidget = QStackedWidget()
        vbox.addWidget(self.stackedWidget)

        for x in range(0, 8):
            label = QLabel("Stacked Child" + str(x))
            label.setFont(QtGui.QFont("Sanserif", 15))
            label.setStyleSheet("color:red")

            self.stackedWidget.addWidget(label)

            self.button = QPushButton("Stack " + str(x))
            self.button.setStyleSheet('background-color:green')

            self.button.page = x
            self.button.clicked.connect(self.btn_clicked)

            vbox.addWidget(self.button)

        self.setLayout(vbox)

    def btn_clicked(self):
        self.button = self.sender()
        self.stackedWidget.setCurrentIndex(self.button.page - 1)


App = QApplication(sys.argv)
window = StackWidget()
sys.exit(App.exec())
