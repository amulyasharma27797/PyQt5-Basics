from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter, QLineEdit
import sys
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Splitters"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.setStyleSheet("background-color: red")

        lineedit = QLineEdit()
        lineedit.setStyleSheet("background-color: yellow")

        splitter1.addWidget(left)
        splitter1.addWidget(lineedit)
        splitter1.setSizes([200, 200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setStyleSheet("background-color: green")

        hbox.addWidget(splitter2)

        self.setLayout(hbox)

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
