import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5 import uic, QtCore, QtWidgets


class Main_window(QMainWindow):
    def __init__(self) -> None:
        super(Main_window, self).__init__()
        uic.loadUi("View/programa.ui", self)
        #self.ui = Main_login()


        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #mover ventana
        # self.ui.frame_superior.mouseMoveEvent = self.mover_ventana
        # self.frame_superior.mouseMoveEvent = self.mover_ventana

        # acceder a las paginas
        self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        """
        self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
        self.ui.bt_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))
        self.ui.bt_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))
        self.ui.bt_cuatro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cuatro))

        # control barra de titulos
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())

        self.ui.bt_restaurar.hide()


        # menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)

    def control_bt_minimizar(self):
        self.showMinimized()

    def control_bt_normal(self):
        self.showNormal()
        self.ui.bt_restaurar.hide()
        self.ui.bt_maximizar.show()

    def control_bt_maximizar(self):
        self.showMaximized()
        self.ui.bt_maximizar.hide()
        self.ui.bt_restaurar.show()

    def mover_menu(self):
        pass
        """
