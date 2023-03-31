from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QTextEdit, QVBoxLayout
import sys
from View import diseño
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
# from View import Main_login
from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5 import uic, QtCore, QtWidgets
from modelos.datos_cliente import ModeloCliente
from modelos.datos_usuario import ModeloUsuario
from controladores.clienteCon import RegistarCliente


class Main_window(QMainWindow):
	def __init__(self):
		# cliente
		super(Main_window, self).__init__()
		uic.loadUi("View/menu.ui", self)
		self.modelo_cliente = ModeloCliente()
		self.registrar_cliente = RegistarCliente()
		self.modelo_usuario = ModeloUsuario()
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

		# ver paginas-----
		self.btn_usuario_editar.clicked.connect(self.page_usuario)
		self.btn_usuario_ver.clicked.connect(self.page_usuario_v)
		# ver paginas -- CLIENTE
		self.btn_crear_cliente.clicked.connect(self.page_cliente)
		self.btn_editar_cliente.clicked.connect(self.page_cliente_v)


		#self.btn_usuario_ver.clicked.connect

		# menu lateral - no funciona
		self.bt_menu.clicked.connect(self.mover_menu)

		# aa-------------------------
		self.bt_guardar_cliente.clicked.connect(lambda: self.modelo_cliente.crearcliente(self.txt_nombre_cliente.text(), self.txt_nit.text(),
																						self.txt_celular.text(),
																						self.txt_direccion.text(),
																						self.txt_tipo.text()))

		# elegir
		#self.cb_tipo = QComboBox(self)


		# TODO USUARIO el eliminar corregir
		self.btn_listar_usuario.clicked.connect(lambda: self.modelo_usuario.listar_Usuario(self.tabla_usuario))
		self.btn_actualizar_usuario.clicked.connect(lambda: self.modelo_usuario.subir_usuarios(self.tabla_usuario))
		self.btn_eliminar_usuario.clicked.connect(lambda: self.modelo_usuario.eliminar_Usuario(self.tabla_usuario))
		# self.btn_salir_usuario.clicked.connect(self.salir_usuario)
		# self.ventana_inicio = Main_login()

		# TODO PARA CLIENTES
		self.bt_guardar_cliente.clicked.connect(self.borrar_cliente)
		self.btn_lista_cliente.clicked.connect(lambda: self.modelo_cliente.listar_cliente(self.tabla_cliente))
		self.btn_crear_cliente.clicked.connect(lambda: self.modelo_cliente.eliminar_cliente(self.tabla_cliente))


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

	def tipo_medio(self):
		print("er")
		if self.cb_tipo.currentText() == 'Cargo Expreso':
			self.txt_tipo.setPlainText('1')
		elif self.cb_tipo.currentText() == 'Guatex':
			self.txt_tipo.setPlainText('2')
		elif self.cb_tipo.currentText() == 'Transportador':
			self.txt_tipo.setPlainText('3')
		elif self.cb_tipo.currentText() == 'Recoger':
			print("Errro")
			self.txt_tipo.setPlainText('4')

	def page_usuario(self):
		self.stackedWidget_2.setCurrentWidget(self.page_editar_usuario)

	def page_usuario_v(self):
		self.stackedWidget_2.setCurrentWidget(self.page_mostrar_usuario)

	def page_cliente(self):
		self.stackedWidget_3.setCurrentWidget(self.page_crear_cliente)

	def page_cliente_v(self):
		self.stackedWidget_3.setCurrentWidget(self.page_cliente_e)

	def borrar_cliente(self):
		self.txt_nombre_cliente.clear()
		self.txt_nit.clear()
		self.txt_celular.clear()
		self.txt_direccion.clear()
		self.txt_tipo.clear()