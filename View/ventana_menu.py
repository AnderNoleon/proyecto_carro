from PyQt5.QtWidgets import QMainWindow

import sys
from View import diseño
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5 import uic, QtCore, QtWidgets
from modelos.datos_cliente import ModeloCliente
from controladores.clienteCon import RegistarCliente


class Main_window(QMainWindow):
	def __init__(self):
		# cliente
		super(Main_window, self).__init__()
		uic.loadUi("View/menu.ui", self)
		self.modelo_cliente = ModeloCliente()
		self.registrar_cliente = RegistarCliente()
		self.cliente_id = self.registrar_cliente.obtener_ultimo_id_cliente()

		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		# self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

		# eliminar barra y de titulo - opacidad
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		# SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		# mover ventana
		self.frame_superior.mouseMoveEvent = self.mover_ventana

		# control barra de titulos
		self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
		self.bt_restaurar.clicked.connect(self.control_bt_normal)
		self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
		self.bt_cerrar.clicked.connect(lambda: self.close())
		self.bt_restaurar.hide()

		# acceder a las paginas
		self.bt_inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
		self.bt_uno.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_uno))
		self.bt_dos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_dos))
		self.bt_tres.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_tres))
		self.bt_cuatro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_cuatro))
		self.bt_cinco.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_cinco))

		# menu lateral - no funciona
		self.bt_menu.clicked.connect(self.mover_menu)

		# aa-------------------------
		self.bt_guardar_cliente.clicked.connect(lambda: self.modelo_cliente.crearcliente(self.txt_nombre_cliente.text(), self.txt_nit.text(),
																						self.txt_celular.text(),
																						self.txt_direccion.text(),
																						self.txt_tipo.text()))

	def control_bt_minimizar(self):
		self.showMinimized()

	def control_bt_normal(self):
		self.showNormal()
		self.bt_restaurar.hide()
		self.bt_maximizar.show()

	def control_bt_maximizar(self):
		self.showMaximized()
		self.bt_maximizar.hide()
		self.bt_restaurar.show()

	def mover_ventana(self, event):
		if self.isMaximized() == False:
			if event.buttons() == QtCore.Qt.LeftButton:
				self.move(self.pos() + event.globalPos() - self.clickPosition)
				self.clickPosition = event.globalPos()
				event.accept()

	def mover_menu(self):
		width = self.frame_lateral.width()
		normal = 0

		if width == 0:
			extender = 200
		else:
			extender = normal
			#self.animacion = QPropertyAnimation(self.frame_lateral, b"minimumWidth")
			#print("errorss")
			#self.animacion.setDuration(300)
			#self.animacion.setStartValue(width)
			#self.animacion.setEndValue(extender)
			#self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			#self.animacion.start()

	#  SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

	# mover ventana
	def mousePressEvent(self, event):
		self.clickPosition = event.globalPos()