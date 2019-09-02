from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QFontDialog, QColorDialog
import sys
from PyQt5.Qt import QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 ColorDialog"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_editor()
        self.create_menu()

        self.show()

    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")

        printAction = QAction(QIcon("print.png"), "Print", self)
        printAction.triggered.connect(self.print_dialog)
        fileMenu.addAction(printAction)

        copyAction = QAction(QIcon("copy.png"), "Copy", self)
        copyAction.setShortcut("Ctrl+C")
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon("cut.png"), "Cut", self)
        cutAction.setShortcut("Ctrl+X")
        editMenu.addAction(cutAction)

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

        fontAction = QAction(QIcon("font.svg"), "Font", self)
        fontAction.setShortcut("Ctrl+F")
        fontAction.triggered.connect(self.font_dialog)
        viewMenu.addAction(fontAction)

        colorAction = QAction(QIcon("color.png"), "Color", self)
        viewMenu.addAction(colorAction)
        colorAction.triggered.connect(self.color_dialog)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)
        toolbar.addAction(fontAction)
        toolbar.addAction(colorAction)
        toolbar.addAction(printAction)

    def exit_window(self):
        self.close()

    def create_editor(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

    def font_dialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

    def color_dialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def print_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
