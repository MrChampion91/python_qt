import sys
from PyQt5.QtWidgets import *

'''''''''
app = QApplication(sys.argv) #create app
dlgMain = QWidget()         #create main window
#dlgMain = QDialog()
#dlgMain = QMainWindow()

dlgMain.setWindowTitle("main window")   #set title
dlgMain.show()

sys.exit(app.exec_())   #event loop
'''''''''


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("main window")
        self.resize(300, 400)

        # text
        self.ledText = QLineEdit("award", self)
        self.ledText.move(80, 1)

        # button
        self.btnUpdate = QPushButton("press", self)
        # self.btnUpdate.move(80, 1)
        self.btnUpdate.clicked.connect(self.updateButton)

    def updateButton(self):
        self.setWindowTitle(self.ledText.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)  # create app
    dlgMain = DlgMain()  # create main window
    dlgMain.show()

    sys.exit(app.exec_())  # event loop
