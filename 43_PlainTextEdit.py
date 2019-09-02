from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit
import sys
from PyQt5 import QtGui


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Plain Text Edit"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        
        plainTextEdit = QPlainTextEdit()
        plainTextEdit.setPlaceholderText("Happy Writing...")
        # plainTextEdit.setReadOnly(True)

        text = "Hello this is a simple text"
        plainTextEdit.appendPlainText(text)

        plainTextEdit.setUndoRedoEnabled(False)

        vbox.addWidget(plainTextEdit)
        self.setLayout(vbox)

        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
