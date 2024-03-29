import sys
from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5 import uic

formcl=uic.loadUiType('0329.ui')[0]

class mywin(QMainWindow,formcl):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('연습프로그램')

if __name__=='__main__':
    app=QApplication(sys.argv)
    my=mywin()
    my.show()
    sys.exit(app.exec_())




