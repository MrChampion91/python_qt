import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) #create app
dlgMain = QWidget()         #create main window
dlgMain.setWindowTitle("main window")   #set title
dlgMain.show()

app.exec_()