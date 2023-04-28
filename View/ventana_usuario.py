#import sys
#import os
#from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5 import uic, QtCore, QtWidgets
#from View import Main_login
#from server.conexion_sql import conecciones
#import datetime


#class Main_re(QMainWindow):
#    def __init__(self) -> None:
#        super(Main_re, self).__init__()
#        uic.loadUi("View/registro.ui", self)
#        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
#        self.conn = conecciones()
#        self.ventana_principal = Main_login()

        # self.btn_regresar.clicked.connect(self.regresar_venta)

    # def regresar_ventana(self):
        # self.ventana_principal.show()
        # self.hide()
        # print("FUNCIONA")
