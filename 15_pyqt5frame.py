from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet('background-color: yellow')

        hbox = QHBoxLayout()

        btn = QPushButton("Click Me")
        btn.setStyleSheet('color: white')
        btn.setStyleSheet('background-color: green')

        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(0.6)
        frame.setStyleSheet('background-color: red')

        hbox.addWidget(frame)
        hbox.addWidget(btn)

        self.setLayout(hbox)

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
