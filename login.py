from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

import sys


class Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setHostName("localhost")
        self.db.setUserName("rod")
        self.db.setPassword("forever11")
        self.db.setDatabaseName("dbpos")
        if self.db.open():
            uic.loadUi("login.ui",self)
        else:
            self.resize(500, 150)
            font = QFont("Dejavu sans", 12, QFont.Bold)
            self.setWindowTitle("Error")
            self.setFont(font)
            self.label = QLabel(self)
            self.label.setGeometry(QtCore.QRect(130, 40, 291, 21))
            self.label.setObjectName("label")
            self.pushButton = QPushButton(self)
            self.pushButton.setGeometry(QtCore.QRect(200, 90, 89, 25))
            self.pushButton.setObjectName("pushButton")
            QtCore.QMetaObject.connectSlotsByName(self)
            self.label.setText("Problemas de conexión")
            self.pushButton.setText("Aceptar")
            self.pushButton.clicked.connect(self.button_error_conection)
        self.PBClose.clicked.connect(self.button_error_conection)

    def button_error_conection(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    app.exec_()
    




