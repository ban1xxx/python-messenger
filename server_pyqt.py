# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 120, 391, 191))
        self.groupBox.setObjectName("groupBox")
        self.tableWidget_clients = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_clients.setGeometry(QtCore.QRect(40, 20, 311, 161))
        self.tableWidget_clients.setObjectName("tableWidget_clients")
        self.tableWidget_clients.setColumnCount(3)
        self.tableWidget_clients.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clients.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clients.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_clients.setHorizontalHeaderItem(2, item)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 320, 391, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_service_info = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_service_info.setGeometry(QtCore.QRect(10, 20, 371, 231))
        self.textBrowser_service_info.setObjectName("textBrowser_service_info")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 10, 391, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_status_key = QtWidgets.QLabel(self.groupBox_3)
        self.label_status_key.setGeometry(QtCore.QRect(270, 30, 61, 16))
        self.label_status_key.setObjectName("label_status_key")
        self.label_status_value = QtWidgets.QLabel(self.groupBox_3)
        self.label_status_value.setGeometry(QtCore.QRect(270, 60, 61, 16))
        self.label_status_value.setObjectName("label_status_value")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_ip.setGeometry(QtCore.QRect(30, 30, 111, 20))
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.lineEdit_port = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_port.setGeometry(QtCore.QRect(30, 60, 111, 20))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.pushButton_stop_server = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_stop_server.setGeometry(QtCore.QRect(160, 60, 71, 21))
        self.pushButton_stop_server.setObjectName("pushButton_stop_server")
        self.pushButton_start_server = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_start_server.setGeometry(QtCore.QRect(160, 30, 71, 21))
        self.pushButton_start_server.setObjectName("pushButton_start_server")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server"))
        self.groupBox.setTitle(_translate("MainWindow", "Clients"))
        item = self.tableWidget_clients.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Login"))
        item = self.tableWidget_clients.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last time"))
        item = self.tableWidget_clients.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last IP"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Service info"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Parameters"))
        self.label_status_key.setText(_translate("MainWindow", "Status:"))
        self.label_status_value.setText(_translate("MainWindow", "Not started"))
        self.lineEdit_ip.setText(_translate("MainWindow", "127.0.0.1"))
        self.lineEdit_ip.setPlaceholderText(_translate("MainWindow", "IP address to listen"))
        self.lineEdit_port.setText(_translate("MainWindow", "7777"))
        self.lineEdit_port.setPlaceholderText(_translate("MainWindow", "Port to listen"))
        self.pushButton_stop_server.setText(_translate("MainWindow", "Stop server"))
        self.pushButton_start_server.setText(_translate("MainWindow", "Start server"))
