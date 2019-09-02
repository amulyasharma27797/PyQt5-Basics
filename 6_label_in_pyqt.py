from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Labels"
        self.top = 200
        self.left = 500
        self.height = 300
        self.width = 400

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.height, self.width)

        vbox = QVBoxLayout()
        label = QLabel("This is PyQt Label")
        vbox.addWidget(label)

        label2 = QLabel("This is PyQt Application Development")
        label2.setFont(QtGui.QFont('Sanserif', 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
