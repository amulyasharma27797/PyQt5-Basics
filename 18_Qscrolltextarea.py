from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
    QFormLayout, QGroupBox, QPushButton, QScrollArea, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self, val):
        super().__init__()

        self.title = "PyQt5 Scroll TextArea"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout = QFormLayout()
        groupBox = QGroupBox("This is a group box")

        labelList = []
        buttonList = []

        for i in range(val):
            labelList.append(QLabel("Label"))
            buttonList.append(QPushButton("Click Me"))
            formLayout.addRow(labelList[i], buttonList[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(40)
    sys.exit(App.exec())
