from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QToolBox, QWidget
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 ToolBox"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 100

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color:yellow")

        self.init_ui()
        self.show()

    def init_ui(self):
        vbox = QVBoxLayout()
        toolbox = QToolBox()
        toolbox.setStyleSheet("background-color:green")
        vbox.addWidget(toolbox)

        label = QLabel()
        toolbox.addItem(label, "Python")

        label = QLabel()
        toolbox.addItem(label, "Java")

        label = QLabel()
        toolbox.addItem(label, "C++")

        self.setLayout(vbox)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
