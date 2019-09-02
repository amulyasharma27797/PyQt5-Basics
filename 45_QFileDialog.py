from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QFileDialog"
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
        self.btn = QPushButton("Browse Image")
        self.btn.clicked.connect(self.browse_image)
        vbox.addWidget(self.btn)

        self.label = QLabel("")
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()

    def browse_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home\\',
                                            'Image files (*.png *.gif')  # home\\ -> directory not catching

        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
