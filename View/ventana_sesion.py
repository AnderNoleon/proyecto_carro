import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore, QtWidgets
from View import Main_window
from server.conexion_sql import conecciones
import datetime


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
        self.btn_entrar.clicked.connect(self.bloquear_tipo)

    def abrirr(self):
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

    def abrir(self):
        usuario = self.txt_login.text()
        contra = self.txt_password.text()

        cursor = self.conn.cursor()
        query = "SELECT * FROM usuario WHERE usuario = %s AND contrasena = %s"
        cursor.execute(query, (usuario, contra))
        result = cursor.fetchone()

        if result:
            # Mostrar la ventana principal
            self.ventana_principal.show()
            self.hide()

            # Obtener el puesto del usuario
            puesto = result[5]

            # Actualizar el objeto QLineEdit en la ventana principal
            self.ventana_principal.txt_admin_menu.setText(usuario)
            self.ventana_principal.txt_tipo_ver.setText(puesto)

        else:
            QMessageBox.critical(self, "Error de inicio de sesión", "Usuario o contraseña incorrectos")

    def bloquear_tipo(self):
        if self.ventana_principal.txt_tipo_ver.text() == "Vendedor":
            print("ENTRO")
            # Deshabilitar los botones que se deben bloquear para los vendedores
            self.ventana_principal.bt_inicio.setEnabled(False)
            self.ventana_principal.bt_tres.setEnabled(False)

        elif self.ventana_principal.txt_tipo_ver.text() == "Gerente":
            print("Nada")
            # No hacer nada si el valor es diferente de "Vendedor"
            pass


