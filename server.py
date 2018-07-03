import sys
import socket
import time
import threading
from mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

class GUI(QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_start.clicked.connect(self.listen)
        self.ui.btn_quit.clicked.connect(QCoreApplication.instance().quit)
        self.ui.btn_quit.clicked.connect(self.closeConnection)
        self.ui.btn_close.clicked.connect(self.closeConnection)
        self.setWindowTitle('服务器')

    def start(self):
        def tcplink(sock, addr):
            print ('Accept new connection from %s:%s...' % addr)
            # sock.send(b'Welcome!')
            while True:
                # dataLen = sock.recv(1024)
                data = sock.recv(1024)
                # if len(bytes.decode(data)) != bytes.decode(dataLen):
                #     break
                time.sleep(1)
                # if not data or bytes.decode(data) == 'exit':
                #     print('exit')
                #     break
                sock.send(data)
                self.showMsg(bytes.decode(data))
            sock.close()
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global ret
        ret = True
        try:
            s.bind(('192.168.125.102', 1000))
            self.ui.btn_start.setEnabled(False)
            s.listen(5)
            self.showMsg('start listening')
            while ret:
                # 接受一个新连接:
                sock, addr = s.accept()
                # 创建新线程来处理TCP连接:
                t = threading.Thread(target=tcplink, args=(sock, addr))
                t.start()
        except Exception:
            if ret:
                self.showMsg('start listening failed')


    def listen(self):
        t1 = threading.Thread(target=self.start)
        t1.start()

    def showMsg(self,string):
        logtime = time.strftime("%Y_%m_%d %H:%M:%S", time.localtime())
        self.ui.textEdit.append(str(logtime)+'   '+string)

    def closeConnection(self):
        ret = False
        s.close()
        self.showMsg("stop listening")
        self.ui.btn_start.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())
