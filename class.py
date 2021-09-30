import sys
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit


form_class = uic.loadUiType("C:\\Users\\cho03\\Desktop\\programming\\PyQt\\bitui.ui")[0]

class MyWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,300,400)
        self.setWindowTitle("My Program")
        self.setWindowIcon(QIcon("C:\\Users\\cho03\\Desktop\\programming\\PyQt\\icon.png"))
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(100)
        self.timer.timeout.connect(self.timeout)
        self.pushButton.clicked.connect(self.btn_clicked)
        
    def timeout(self):
        current_time = QTime.currentTime()
        str_time = current_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

    def btn_clicked(self):
        BTprice = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(BTprice))

app = QApplication(sys.argv)

window = MyWindow()
window.show()
app.exec_()



