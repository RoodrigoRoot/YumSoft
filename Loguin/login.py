from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QPushButton, QMainWindow
import DB.constants as ct
from PyQt5.QtGui import QFont
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys
from DB.connection import connection_DB
from MainWindow.MainWindow import Ui_MainWindow
from logger import logger
from .utils import LoginMethods




class Dialog(QDialog):
    
    def show_main(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()  
    
    def __init__(self):
        QDialog.__init__(self)
        try:
            if connection_DB():
                uic.loadUi("UI/login.ui",self)
                self.PBClose.clicked.connect(self.button_error_conection)
                self.pbEnter.clicked.connect(self.clicked_botton_enter)
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
                self.label.setText("Problemas de conexión en DB")
                self.pushButton.setText("Aceptar")
                self.pushButton.clicked.connect(self.button_error_conection)
                
        except Exception as e:
            logger.warning("Loguin.login.Dialog", str(e))
    
    def keyPressEvent(self, event):
        if LoginMethods.access_system(self.LEPassword_login):
            self.show_main()
            self.close()
        else:
            self.a()
            
    def clicked_botton_enter(self):
        if LoginMethods.access_system(self.LEPassword_login):
            self.show_main()
            self.close()
        else:
            self.a()
        
    def button_error_conection(self):
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    app.exec_()
    




