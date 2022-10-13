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
        self.resize(500, 300)

        #font
        font = QFont("Times New Roman", 14, 75, True)
        self.setFont(font)

        #image
        img = QPixmap("images.jpg")


        # text
        self.ledText = QLineEdit("award", self)
        self.ledText.move(80, 1)

        #lable
        self.lbl = QLabel("lable text", self)
        self.lbl.move(60, 50)

        self.lbl.setPixmap(img) # add image

        # button 1
        self.btn = QPushButton("press", self)
        # self.btn.move(80, 1)
        self.btn.clicked.connect(self.updateButton1)

        # button 2
        self.btn2 = QPushButton("color", self)
        self.btn2.move(0, 25)
        self.btn2.clicked.connect(self.updateButton2)

    def updateButton1(self):
        res = QMessageBox.information(self, " ", self.ledText.text()) #warning information
        font = QFontDialog.getFont()
        self.lbl.setFont(font[0])
        self.lbl.setText(self.ledText.text())
        #self.setWindowTitle(self.ledText.text())
        print(res)
        print(font)

    def updateButton2(self):
        color = QColorDialog.getColor(QColor("red"), self, "choose Color")
        #self.QColorDialog.setCurrentColor(color)

        print(color)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # create app
    dlgMain = DlgMain()  # create main window
    dlgMain.show()

    sys.exit(app.exec_())  # event loop