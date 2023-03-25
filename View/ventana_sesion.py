import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore, QtWidgets
from View import Main_window
from server.conexion_sql import conecciones


class Main_login(QMainWindow):
    def __init__(self) -> None:
        super(Main_login, self).__init__()
        uic.loadUi("View/loginUi2.ui", self)
        # uic.loadUi("View/Menu_BD.ui", self)
        # forma
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.conn = conecciones()
        self.ventana_principal = Main_window()

        # boton de abrir
        self.btn_entrar.clicked.connect(self.abrir)

    def abrir(self):
        usuario = self.txt_login.text()
        contra = self.txt_password.text()
        cursor = self.conn.cursor()
        cursor.execute("select * from usuario where usuario='"+usuario+"' and contrasena ='"+contra+"'")
        result = cursor.fetchone()
        if result:
            self.ventana_principal.show()
            self.hide()
        else:
            print("Contrseña incorrecta")
