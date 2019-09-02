import time

from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar, QVBoxLayout, QHBoxLayout, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 1

            time.sleep(0.3)
            self.change_value.emit(cnt)


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 ProgressBar with QThread"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.init_ui()
        self.show()

    def init_ui(self):
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        self.progressbar.setMaximum(100)
        # self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 8px; padding: 1px}"
        #                                "QProgressBar::chunk {background:green}")

        # self.progressbar.setOrientation(Qt.Vertical)
        # self.progressbar.setVisible(False)
        self.progressbar.setTextVisible(True)
        vbox.addWidget(self.progressbar)

        self.button = QPushButton("Run Progressbar")
        self.button.clicked.connect(self.startProgressBar)
        self.button.setStyleSheet("background-color:yellow")
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
