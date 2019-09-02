from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QWidget, QVBoxLayout, QDialogButtonBox, QTabWidget,\
    QLabel, QLineEdit, QGroupBox, QCheckBox, QComboBox
import sys
from PyQt5.QtGui import QIcon


class Tab(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Tab Widget")
        self.setGeometry(500, 300, 400, 250)

        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        tabWidget.addTab(TabContact(), "Contact Details")
        tabWidget.addTab(TabPersonDetails(), "Personal Details")

        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)


class TabContact(QWidget):
    def __init__(self):
        super().__init__()

        nameLabel = QLabel("Name : ")
        nameEdit = QLineEdit()

        phone = QLabel("Phone : ")
        phoneEdit = QLineEdit()

        email = QLabel("Email : ")
        emailEdit = QLineEdit()

        addr = QLabel("Address : ")
        addrEdit = QLineEdit()

        vbox = QVBoxLayout()

        vbox.addWidget(nameLabel)
        vbox.addWidget(nameEdit)

        vbox.addWidget(phone)
        vbox.addWidget(phoneEdit)

        vbox.addWidget(email)
        vbox.addWidget(emailEdit)

        vbox.addWidget(addr)
        vbox.addWidget(addrEdit)

        self.setLayout(vbox)


class TabPersonDetails(QWidget):
    def __init__(self):
        super().__init__()

        groupBox = QGroupBox("Select your Gender")

        list = ["Male", "Female"]

        combo = QComboBox()
        combo.addItems(list)

        vbox = QVBoxLayout()
        vbox.addWidget(combo)

        groupBox.setLayout(vbox)

        groupBox2 = QGroupBox("Select Your Favorite Programming Language")

        python = QCheckBox("Python")
        cpp = QCheckBox("C++")
        java = QCheckBox("Java")
        csharp = QCheckBox("C#")

        vboxp = QVBoxLayout()
        vboxp.addWidget(python)
        vboxp.addWidget(cpp)
        vboxp.addWidget(java)
        vboxp.addWidget(csharp)

        groupBox2.setLayout(vboxp)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupBox2)

        self.setLayout(mainLayout)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    tab_dialog = Tab()
    tab_dialog.show()
    App.exec()
