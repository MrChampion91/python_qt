import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

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

        # button 1
        self.btnUpdate = QPushButton("press", self)
        # self.btnUpdate.move(80, 1)
        self.btnUpdate.clicked.connect(self.updateButton1)

        # button 2
        self.btnUpdate = QPushButton("color", self)
        self.btnUpdate.move(0, 25)
        self.btnUpdate.clicked.connect(self.updateButton2)

    def updateButton1(self):
        res = QMessageBox.information(self, " ", self.ledText.text()) #warning information
        #self.setWindowTitle(self.ledText.text())
        print(res)

    def updateButton2(self):
        color = QColorDialog.getColor(QColor("red"), self, "choose Color")
        #self.QColorDialog.setCurrentColor(color)
        print(color)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # create app
    dlgMain = DlgMain()  # create main window
    dlgMain.show()

    sys.exit(app.exec_())  # event loop