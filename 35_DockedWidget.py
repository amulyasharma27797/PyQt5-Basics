from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDockWidget, QListWidget, QTextEdit, QMainWindow
import sys
from PyQt5 import QtGui


class DockDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Docked Widget"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300

        self.setWindowIcon(QtGui.QIcon("home.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createDockWidget()
        self.show()

    def createDockWidget(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        file.addAction("New")
        file.addAction("Save")
        file.addAction("Close")

        self.dock = QDockWidget("Dockable", self)
        self.listwidget = QListWidget()

        list1 = ["Python", "C++", "Java", "C#"]

        self.listwidget.addItems(list1)

        self.dock.setWidget(self.listwidget)

        self.setCentralWidget(QTextEdit())

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)


App = QApplication(sys.argv)
window = DockDialog()
sys.exit(App.exec())
