from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QToolBox, QWidget, QMainWindow, QAction
import sys
from PyQt5.Qt import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QMenuBar"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 300

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_menu()
        self.show()

    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")

        copyAction = QAction(QIcon("copy.png"), "Copy", self)
        copyAction.setShortcut("Ctrl+C")
        fileMenu.addAction(copyAction)

        cutAction = QAction(QIcon("cut.png"), "Cut", self)
        cutAction.setShortcut("Ctrl+X")
        fileMenu.addAction(cutAction)

        saveAction = QAction(QIcon("save.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        exitAction = QAction(QIcon("exit.png"), "Exit", self)
        exitAction.setShortcut("Alt+F4")
        exitAction.triggered.connect(self.exit_window)
        fileMenu.addAction(exitAction)

        pasteAction = QAction(QIcon("paste.png"), "Paste", self)
        pasteAction.setShortcut("Ctrl+V")
        editMenu.addAction(pasteAction)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)

    def exit_window(self):
        self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
