import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon



class mainWindow(object):
    def setupUi(self, mW):
        #mW.setObjectName("Moomas")
        mW.setGeometry(50,50,500,500)
        mW.setWindowTitle("Moomas Finanzen")
        mW.setWindowIcon(QIcon("static/RDS.png"))        



