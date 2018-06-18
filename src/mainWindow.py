import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication



class mainWindow(object):
    def setupUi(self, mW):
        #mW.setObjectName("Moomas")
        mW.setGeometry(50,50,500,500)
        mW.setWindowTitle("Moomas Finanzen")
        mW.setWindowIcon(QIcon("static/RDS.png"))
        self.test(mW)
        
    def test(self, mW):
        print("hello")
        cmdTest = QPushButton("Quit", mW)
        cmdTest.clicked.connect(self.close_application)
        cmdTest.resize(100,100)
        cmdTest.move(100,100)
        #self.show()
        
    def close_application(self):
        print("whoaa shutdown app!!!")
        sys.exit()



