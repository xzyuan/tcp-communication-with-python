import sys
import socket
import time
import struct
def showMsg(string):
    logtime = time.strftime("%Y_%m_%d %H:%M:%S", time.localtime())
    print(logtime +'   '+ string)
    # self.ui.textEdit.append(string)

address = ("192.168.0.9",502)
address_spin = ("192.168.0.10",2000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
# print("连接成功\n")

# data = bytes('', 'UTF-8')
arr = [0x0f,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
data =struct.pack('8B',arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7])

try:
    s.send(data)
    data = s.recv(1024)
    print(data)
except Exception:
    s.close()
    print('通讯出错')
s.close()



