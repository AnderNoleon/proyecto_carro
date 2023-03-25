from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_superior = QtWidgets.QFrame(self.centralwidget)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_superior.setStyleSheet("background-color: rgb(240, 255, 103)")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_menu = QtWidgets.QPushButton(self.frame_superior)
        self.bt_menu.setMinimumSize(QtCore.QSize(200, 35))
        self.bt_menu.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bt_menu.setStyleSheet("QPushButton{\n"
"background -color: #aa00ff;\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(25, 25))
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout_2.addWidget(self.bt_menu)
        spacerItem = QtWidgets.QSpacerItem(451, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bt_minimizar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_minimizar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bt_minimizar.setStyleSheet("QPushButton{\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #e87400;\n"
"background -color: #dad697:\n"
"}")
        self.bt_minimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("menos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QtCore.QSize(32, 32))
        self.bt_minimizar.setObjectName("bt_minimizar")
        self.horizontalLayout_2.addWidget(self.bt_minimizar)
        self.bt_restaurar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_restaurar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bt_restaurar.setStyleSheet("QPushButton{\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #e87400;\n"
"background -color: #dad697:\n"
"}")
        self.bt_restaurar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pestana.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QtCore.QSize(32, 32))
        self.bt_restaurar.setObjectName("bt_restaurar")
        self.horizontalLayout_2.addWidget(self.bt_restaurar)
        self.bt_maximizar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_maximizar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bt_maximizar.setStyleSheet("QPushButton{\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #e87400;\n"
"background -color: #dad697:\n"
"}")
        self.bt_maximizar.setText("")
        self.bt_maximizar.setIcon(icon2)
        self.bt_maximizar.setIconSize(QtCore.QSize(32, 32))
        self.bt_maximizar.setObjectName("bt_maximizar")
        self.horizontalLayout_2.addWidget(self.bt_maximizar)
        self.bt_cerrar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_cerrar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bt_cerrar.setStyleSheet("QPushButton{\n"
"border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #e87400;\n"
"background -color: #dad697:\n"
"}")
        self.bt_cerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../imagenes/cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cerrar.setIcon(icon3)
        self.bt_cerrar.setIconSize(QtCore.QSize(32, 32))
        self.bt_cerrar.setObjectName("bt_cerrar")
        self.horizontalLayout_2.addWidget(self.bt_cerrar)
        self.verticalLayout.addWidget(self.frame_superior)
        self.frame_inferior = QtWidgets.QFrame(self.centralwidget)
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_lateral = QtWidgets.QFrame(self.frame_inferior)
        self.frame_lateral.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_lateral.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_lateral.setStyleSheet("QFrame{\n"
"background-color:#ffe893;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:#ffe893;\n"
"border-top-left-radius: 20px;\n"
"border-buttom-left-radius: 20px;\n"
"\n"
"font:  75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QpushButton: hover{\n"
"background -color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"rgb(255, 232, 147)\n"
"font:  75 12pt \"Arial Narrow\";\n"
"\n"
"}")
        self.frame_lateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lateral.setObjectName("frame_lateral")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_lateral)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_dos = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_dos.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_dos.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bt_dos.setStyleSheet("QPushButton{\n"
"background -color: #aa00ff;\n"
"font: 87 7pt \"Arial Black\";\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 7pt \"Arial Black\";\n"
"}")
        self.bt_dos.setObjectName("bt_dos")
        self.verticalLayout_3.addWidget(self.bt_dos)
        self.bt_cuatro = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_cuatro.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_cuatro.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bt_cuatro.setStyleSheet("QPushButton{\n"
"background -color: #aa00ff;\n"
"font: 87 7pt \"Arial Black\";\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 7pt \"Arial Black\";\n"
"}")
        self.bt_cuatro.setObjectName("bt_cuatro")
        self.verticalLayout_3.addWidget(self.bt_cuatro)
        self.bt_tres = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_tres.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_tres.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bt_tres.setStyleSheet("QPushButton{\n"
"background -color: #aa00ff;\n"
"font: 87 7pt \"Arial Black\";\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 7pt \"Arial Black\";\n"
"}")
        self.bt_tres.setObjectName("bt_tres")
        self.verticalLayout_3.addWidget(self.bt_tres)
        self.bt_cinco = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_cinco.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_cinco.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bt_cinco.setStyleSheet("QPushButton{\n"
"background -color: #aa00ff;\n"
"font: 87 7pt \"Arial Black\";\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 7pt \"Arial Black\";\n"
"}")
        self.bt_cinco.setObjectName("bt_cinco")
        self.verticalLayout_3.addWidget(self.bt_cinco)
        self.bt_uno = QtWidgets.QPushButton(self.frame_lateral)
        self.bt_uno.setMinimumSize(QtCore.QSize(0, 40))
        self.bt_uno.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bt_uno.setStyleSheet("QPushButton{\n"
"background -color: #aa00ff;\n"
"font: 87 7pt \"Arial Black\";\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 7pt \"Arial Black\";\n"
"}")
        self.bt_uno.setObjectName("bt_uno")
        self.verticalLayout_3.addWidget(self.bt_uno)
        spacerItem1 = QtWidgets.QSpacerItem(20, 266, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frame_lateral)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame_lateral)
        self.frame_contenedor = QtWidgets.QFrame(self.frame_inferior)
        self.frame_contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenedor.setObjectName("frame_contenedor")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_uno = QtWidgets.QWidget()
        self.page_uno.setObjectName("page_uno")
        self.stackedWidget.addWidget(self.page_uno)
        self.page_dos = QtWidgets.QWidget()
        self.page_dos.setObjectName("page_dos")
        self.stackedWidget.addWidget(self.page_dos)
        self.page_tres = QtWidgets.QWidget()
        self.page_tres.setObjectName("page_tres")
        self.stackedWidget.addWidget(self.page_tres)
        self.page_cuatro = QtWidgets.QWidget()
        self.page_cuatro.setObjectName("page_cuatro")
        self.stackedWidget.addWidget(self.page_cuatro)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_contenedor)
        self.verticalLayout.addWidget(self.frame_inferior)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_menu.setText(_translate("MainWindow", "Menu"))
        self.bt_dos.setText(_translate("MainWindow", "Inicio"))
        self.bt_cuatro.setText(_translate("MainWindow", "Proveedor"))
        self.bt_tres.setText(_translate("MainWindow", "Inventario"))
        self.bt_cinco.setText(_translate("MainWindow", "Venta"))
        self.bt_uno.setText(_translate("MainWindow", "Cliente"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


