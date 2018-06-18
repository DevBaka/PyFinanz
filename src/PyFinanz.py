import sys
import os
from PyQt5.QtWidgets import *
from mainWindow import mainWindow
import platform

platform = platform.system()
print(platform)


class PyFinanz(QMainWindow):
    def __init__(self):
        super(PyFinanz, self).__init__()
        self.ui = mainWindow()
        self.ui.setupUi(self)
        
    def closeEvent(self, QCloseEVent):
        print("Closing PyFinanz")
        

app = QApplication(sys.argv)

myapp = PyFinanz()
myapp.show()


#w = QWidget()
#w.setGeometry(50,50,500,500)
#w.setWindowTitle("Moomas Finanzen")
#w.setWindowIcon(QIcon("static/RDS.png"))

#w.show()

sys.exit(app.exec_())