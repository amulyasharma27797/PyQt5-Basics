from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu
import sys
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Context Menu"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)

        newAction = contextMenu.addAction("New")
        openAction = contextMenu.addAction("Open")
        quitAction = contextMenu.addAction("Close")

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAction:
            self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
