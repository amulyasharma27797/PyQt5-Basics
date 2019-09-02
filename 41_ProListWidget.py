import sys

from PyQt5.QtWidgets import QDialog, QListWidget, QVBoxLayout, QPushButton, QHBoxLayout, QInputDialog, QLineEdit, \
    QMessageBox, QApplication


class ProgrammingDialog(QDialog):
    def __init__(self, name, proList = None):
        super(ProgrammingDialog, self).__init__()

        self.name = name

        self.list = QListWidget()

        if proList is not None:
            self.list.addItems(proList)
            self.list.setCurrentRow(0)

        vbox = QVBoxLayout()

        for text, slot in (("Add", self.add),
                            ("Edit", self.edit),
                            ("Remove", self.remove),
                            ("Sort", self.sort),
                            ("Close", self.close)

            ):

            buttons = QPushButton(text)
            buttons.clicked.connect(slot)

            vbox.addWidget(buttons)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addLayout(vbox)
        self.setLayout(hbox)

        self.setWindowTitle("PyQt5 Simple List Project")

    def add(self):
        row = self.list.currentRow()
        title = "Add {0}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)

        if ok and string is not None:
            self.list.insertItem(row, string)

    def edit(self):
        row = self.list.currentRow()
        item = self.list.item(row)

        if item is not None:
            title = "Edit {0}".format(self.name)

            string, ok = QInputDialog.getText(self, title, title,
                                              QLineEdit.Normal, item.text())

            if ok and string is not None:
                item.setText(string)

    def remove(self):
        row = self.list.currentRow()
        item = self.list.item(row)

        if item is None:
            return

        reply = QMessageBox.question(self, "Remove {0}".format(
            self.name), "Remove {0} '{1}'?".format(
            self.name, str(item.text())),
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            item = self.list.takeItem(row)

            del item

    def sort(self):
        self.list.sortItems()

    def close(self):
        self.accept()


if __name__ == "__main__":
    programming = ["Python", "Java", "C#", "C++", "Ruby", "Kotlin"]

    app = QApplication(sys.argv)
    dialog = ProgrammingDialog("Language", programming)
    dialog.exec_()
