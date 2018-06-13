# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 323)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit_command = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_command.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.lineEdit_command.setObjectName("lineEdit_command")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 111, 21))
        self.label.setObjectName("label")
        self.btn_send = QtWidgets.QPushButton(self.centralWidget)
        self.btn_send.setGeometry(QtCore.QRect(210, 60, 75, 23))
        self.btn_send.setObjectName("btn_send")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(80, 110, 291, 131))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 21, 41))
        self.label_2.setObjectName("label_2")
        self.btn_connect = QtWidgets.QPushButton(self.centralWidget)
        self.btn_connect.setGeometry(QtCore.QRect(90, 20, 91, 21))
        self.btn_connect.setObjectName("btn_connect")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 419, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "输入命令"))
        self.btn_send.setText(_translate("MainWindow", "发送"))
        self.label_2.setText(_translate("MainWindow", "log"))
        self.btn_connect.setText(_translate("MainWindow", "连接到服务器"))

