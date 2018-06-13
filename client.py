import sys
import socket
import time
from client_mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import *

class GUI(QMainWindow):

    # ret = 0

    def __init__(self):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_send.clicked.connect(self.Send_msg)
        self.ui.btn_connect.clicked.connect(self.Connect)

    def printTest(self):
        str1 = b'Welcome! Hello!'
        self.showMsg(bytes.decode(str1))

    def Connect(self):
        address = ('192.168.125.118', 12225)
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(address)
            self.showMsg('connected successfully')
            # self.ret = 1
        except Exception:
            s.close()
            # self.ret = 0
            self.showMsg('closed with exception')

    def Send_msg(self):
        # if self.ret == 0:
        data = bytes(self.ui.lineEdit_command.text(), 'UTF-8')
        self.showMsg(bytes.decode(data)+'    sent')
        try:
            # dataLength = bytes(hex(len(data)), encoding="utf-8")
            # s.send(dataLength)
            s.send(data)
            recvInfo = bytes.decode(s.recv(1024))
            time.sleep(1)
            self.showMsg(recvInfo+'    received')
            # s.close()
        except Exception:
            s.close()
            self.showMsg('错误关闭')



    def showMsg(self,string):
        logtime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        self.ui.textEdit.append(str(logtime)+'   '+string)
        # self.ui.textEdit.append(string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

