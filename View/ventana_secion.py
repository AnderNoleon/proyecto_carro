import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore, QtWidgets
from server.conexion_sql import conecciones



class Main_login(QMainWindow):
    def __init__(self) -> None:
        super(Main_login, self).__init__()
        uic.loadUi("View/loginUi2.ui", self)
        # uic.loadUi("View/Menu_BD.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.conn = conecciones()
        self.btn_entrar.clicked.connect(self.abrir)



        self.btn_cambio.clicked.connect(self.changeForm)
        self.btn_register.clicked.connect(self.registrar)

    def abrir(self):
        user = self.txt_login.text()
        pw = self.txt_password.text()
        # print(f"{user}+{pw}")

        cursor = self.conn.cursor()
        cursor.execute("select * from usuario where usuario='"+user+"' and password ='"+pw+"'")
        result = cursor.fetchone()
        if result:
            self.ventana_principal.show()
            self.hide()
        else:
            print("Contrseña incorrecta")
