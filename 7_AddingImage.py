from PyQt5.QtWidgets import QDialog, QApplication, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Adding Images"
        self.top = 200
        self.left = 500
        self.height = 400
        self.width = 500

        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.height, self.width)

        vbox = QVBoxLayout()
        label_image = QLabel(self)
        pixmap = QPixmap("home.png")
        label_image.setPixmap(pixmap)

        vbox.addWidget(label_image)

        self.setLayout(vbox)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
