import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap

from stegano import lsb

qtcreator_file = "main.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

imagename = ""

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        #self.setupUi(self)
        self.encryptImagesButton.clicked.connect(self.encryptImgs)
        self.decryptImagesButton.clicked.connect(self.decryptImgs)
        self.quitButton.clicked.connect(self.quitApplication)

    def encryptImgs(self): #Quit button has been pressed         
        self.close()

    def decryptImgs(self): #Quit button has been pressed         
        self.close()

    def quitApplication(self): #Quit button has been pressed         
        self.close()

    
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())