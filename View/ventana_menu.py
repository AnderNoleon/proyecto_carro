from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QTextEdit, QVBoxLayout, QTableWidgetItem, QMessageBox
import sys
from View import diseño
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
# from View import Main_login
from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5 import uic, QtCore, QtWidgets
from modelos.datos_cliente import ModeloCliente
from modelos.datos_usuario import ModeloUsuario
from modelos.datos_proveedor import ModeloPrincipal
from controladores.clienteCon import RegistarCliente
from controladores.inventarioCon import RegistrarInventario
from modelos.datos_inventario import ModeloInventario
from server.conexion_sql import conecciones


class Main_window(QMainWindow):
	def __init__(self):
		# cliente
		super(Main_window, self).__init__()
		uic.loadUi("View/menu.ui", self)
		self.modelo_compra = ModeloPrincipal()
		self.modelo_cliente = ModeloCliente()
		self.registrar_cliente = RegistarCliente()
		self.modelo_usuario = ModeloUsuario()
		self.cliente_id = self.registrar_cliente.obtener_ultimo_id_cliente()
		self.modelo_inventario = ModeloInventario()
		self.conn = conecciones()

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
		# ver paginas ---- INVENTARIO
		self.btn_crear_inventario.clicked.connect(self.page_inventario_c)
		self.btn_ver_inventario.clicked.connect(self.page_inventario_v)
		# ver paginas ---- VENTA
		self.btn_crear_venta.clicked.connect(self.page_ventas_c)
		self.btn_ver_venta.clicked.connect(self.page_ventas_v)


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
		self.btn_eliminar_cliente_2.clicked.connect(lambda: self.modelo_cliente.eliminar_cliente(self.tabla_cliente))
		self.btn_editar_cliente_2.clicked.connect(lambda: self.modelo_cliente.subir_clientes(self.tabla_cliente))
		self.cb_tipo.currentIndexChanged.connect(self.actualizar_txt_tipo)


		# TODO PARA INVENTARIO
		self.tabla_pre_venta.itemSelectionChanged.connect(self.cargar_datos_seleccionados)
		self.row_seleccionada = None

		#self.btn_guardar_in.clicked.connect(lambda: self.modelo_inventario.mostrar_compra(self.tabla_pre_venta))
		self.btn_guardar_in.clicked.connect(self.mostrar_compra)
		self.btn_editar_in.clicked.connect(self.editar_datos)
		self.btn_eliminar_in.clicked.connect(self.eliminar_datos)
		self.btn_finalizar_in.clicked.connect(self.guardar_datos)
		self.btn_calcular_pro.clicked.connect(self.calcular_precio)
		self.btn_calcular_pro.clicked.connect(self.ver_total_de_productos)
		self.btn_finalizar_in.clicked.connect(lambda: self.modelo_compra.crearProducto(self.txt_marca_pro.text(), self.txt_total_tabla.text()))
		self.btn_guardar_in_2.clicked.connect(self.detalle)
		self.btn_ver_inventaro_tabla.clicked.connect(lambda: self.modelo_inventario.listar_inventario(self.tabla_pre_venta_3))

		# USUARIO BLOQUE LA
		#self.bt_menu.clicked.connect(self.bloquear_tipo)



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

	def page_inventario_v(self):
		self.stackedWidget_4.setCurrentWidget(self.page_inve_v)

	def page_inventario_c(self):
		self.stackedWidget_4.setCurrentWidget(self.page_inven_c)

	def page_ventas_c(self):
		self.stackedWidget_5.setCurrentWidget(self.page_venta_c)

	def page_ventas_v(self):
		self.stackedWidget_5.setCurrentWidget(self.page_venta_v)

	def borrar_cliente(self):
		self.txt_nombre_cliente.clear()
		self.txt_nit.clear()
		self.txt_celular.clear()
		self.txt_direccion.clear()
		self.txt_tipo.clear()
		self.cb_tipo.setCurrentIndex(0)

	def mostrar_compra(self):
		codigo = self.txt_codigo_in.text()
		carro = self.txt_carro_in.text()
		cantidad = self.txt_cantidad_in.text()
		precioc = self.txt_pc_in.text()
		preciov = self.txt_pv_in.text()
		# row_position = self.tabla_pre_venta.rowCount()
		# self.tabla_pre_venta.insertRow(row_position)

		if self.row_seleccionada is None:
			row_position = self.tabla_pre_venta.rowCount()
			self.tabla_pre_venta.insertRow(row_position)
		else:
			row_position = self.row_seleccionada

		self.tabla_pre_venta.setItem(row_position, 0, QTableWidgetItem(codigo))
		self.tabla_pre_venta.setItem(row_position, 1, QTableWidgetItem(carro))
		self.tabla_pre_venta.setItem(row_position, 2, QTableWidgetItem(cantidad))
		self.tabla_pre_venta.setItem(row_position, 3, QTableWidgetItem(precioc))
		self.tabla_pre_venta.setItem(row_position, 4, QTableWidgetItem(preciov))
		self.txt_codigo_in.clear()
		self.txt_carro_in.clear()
		self.txt_cantidad_in.clear()
		self.txt_pc_in.clear()
		self.txt_pv_in.clear()
		self.row_seleccionada = None

	# cambiar por el que esta arriba , esta mas completo
	def mostrar_compraa(self):
		codigo = self.txt_codigo_in.text()
		carro = self.txt_carro_in.text()
		cantidad = self.txt_cantidad_in.text()
		precioc = self.txt_pc_in.text()
		preciov = self.txt_pv_in.text()

		if int(cantidad) <= 10:
			if self.row_seleccionada is None:
				row_position = self.tabla_pre_venta.rowCount()
				self.tabla_pre_venta.insertRow(row_position)
			else:
				row_position = self.row_seleccionada

			self.tabla_pre_venta.setItem(row_position, 0, QTableWidgetItem(codigo))
			self.tabla_pre_venta.setItem(row_position, 1, QTableWidgetItem(carro))
			self.tabla_pre_venta.setItem(row_position, 2, QTableWidgetItem(cantidad))
			self.tabla_pre_venta.setItem(row_position, 3, QTableWidgetItem(precioc))
			self.tabla_pre_venta.setItem(row_position, 4, QTableWidgetItem(preciov))
			self.txt_codigo_in.clear()
			self.txt_carro_in.clear()
			self.txt_cantidad_in.clear()
			self.txt_pc_in.clear()
			self.txt_pv_in.clear()
			self.row_seleccionada = None
		else:
			# Si la cantidad es mayor a 10, mostrar un mensaje de error al usuario
			QMessageBox.warning(self, "Error", "La cantidad de existencias debe ser 10 o menos.")

	def cargar_datos_seleccionados(self):
		if len(self.tabla_pre_venta.selectedItems()) > 0:
			items = self.tabla_pre_venta.selectedItems()
			self.row_seleccionada = items[0].row()
			self.txt_codigo_in.setText(self.tabla_pre_venta.item(self.row_seleccionada, 0).text())
			self.txt_carro_in.setText(self.tabla_pre_venta.item(self.row_seleccionada, 1).text())
			self.txt_cantidad_in.setText(self.tabla_pre_venta.item(self.row_seleccionada, 2).text())
			self.txt_pc_in.setText(self.tabla_pre_venta.item(self.row_seleccionada, 3).text())
			self.txt_pv_in.setText(self.tabla_pre_venta.item(self.row_seleccionada, 4).text())

	def editar_datos(self):
		if self.row_seleccionada is None:
			QMessageBox.information(self, "Error", "Por favor seleccione una fila para editar.")
			print("error")
			return

		self.mostrar_compra()

	def eliminar_datos(self):
		if self.row_seleccionada is None:
			QMessageBox.information(self, "Error", "Por favor seleccione una fila para eliminar.")
			return

		reply = QMessageBox.question(self, 'Eliminar fila', '¿Está seguro de que desea eliminar esta fila?',
									 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			self.tabla_pre_venta.removeRow(self.row_seleccionada)
			self.txt_codigo_in.clear()
			self.txt_carro_in.clear()
			self.txt_cantidad_in.clear()
			self.txt_pc_in.clear()
			self.txt_pv_in.clear()
			self.row_seleccionada = None

	def guardar_datos_t(self):
		codigo = self.txt_codigo_in.text()
		carro = self.txt_carro_in.text()
		cantidad = self.txt_cantidad_in.text()
		precioc = self.txt_pc_in.text()
		preciov = self.txt_pv_in.text()

		try:
			self.conn = conecciones()
			cursor = self.conn.cursor()

			if not cantidad.isdigit():
				# Si el campo existencia no es un número, no se puede insertar en la base de datos
				raise ValueError("La cantidad debe ser un número entero")

			if self.tabla_pre_venta.currentRow() == -1:
				# No hay fila seleccionada, se inserta un nuevo registro
				insert_query = """INSERT INTO inventario (codigo_carro, producto, existencia, precio_costo, precio_venta) 
	                            VALUES (%s, %s, %s, %s, %s)"""
				data = (codigo, carro, cantidad, precioc, preciov)
				cursor.execute(insert_query, data)
			else:
				# Se actualiza la fila seleccionada
				self.row_seleccionada = self.tabla_pre_venta.currentRow()
				update_query = """UPDATE inventario 
	                            SET codigo_carro = %s, producto = %s, existencia = %s,
	                            precio_costo = %s, precio_venta = %s 
	                            WHERE idInventario = %s"""
				data = (
				codigo, carro, cantidad, precioc, preciov, self.tabla_pre_venta.item(self.row_seleccionada, 0).text())
				cursor.execute(update_query, data)

			self.conn.commit()
			self.mostrar_datos()
			self.limpiar_campos()

		except ValueError as ve:
			print(f"Error al guardar datos en la base de datos: {ve}")
		except Exception as e:
			print(f"Error al guardar datos en la base de datosd: {e}")

	# VER DATOS DEL INVENTARIO

	def mostrar_datos_carro(self):
		cursor = self.conn.cursor()
		select_query = "SELECT * FROM inventario"
		cursor.execute(select_query)
		data = cursor.fetchall()
		self.tabla_pre_venta.setRowCount(0)
		for row in data:
			self.tabla_pre_venta.insertRow(0)
			self.tabla_pre_venta.setItem(0, 0, QTableWidgetItem(str(row[0])))
			self.tabla_pre_venta.setItem(0, 1, QTableWidgetItem(row[1]))
			self.tabla_pre_venta.setItem(0, 2, QTableWidgetItem(str(row[2])))
			self.tabla_pre_venta.setItem(0, 3, QTableWidgetItem(str(row[3])))
			self.tabla_pre_venta.setItem(0, 4, QTableWidgetItem(str(row[4])))

	def guardar_datos(self):
		try:
			self.conn = conecciones()
			cursor = self.conn.cursor()

			# Recorrer el QTableWidget y agregar los datos a una lista de tuplas
			datos = []
			for fila in range(self.tabla_pre_venta.rowCount()):
				codigo = self.tabla_pre_venta.item(fila, 0).text()
				carro = self.tabla_pre_venta.item(fila, 1).text()
				cantidad = self.tabla_pre_venta.item(fila, 2).text()
				precioc = self.tabla_pre_venta.item(fila, 3).text()
				preciov = self.tabla_pre_venta.item(fila, 4).text()
				if not cantidad.isdigit():
					# Si el campo existencia no es un número, no se puede insertar en la base de datos
					raise ValueError("La cantidad debe ser un número entero")
				datos.append((codigo, carro, cantidad, precioc, preciov))

			# Insertar los datos en la base de datos
			insert_query = """INSERT INTO inventario (codigo_carro, producto, existencia, precio_costo, precio_venta) 
	                            VALUES (%s, %s, %s, %s, %s)"""
			cursor.executemany(insert_query, datos)
			self.conn.commit()

			# Borrar los datos del QTableWidget
			self.tabla_pre_venta.clearContents()
			self.tabla_pre_venta.setRowCount(0)

			self.limpiar_campos()

		except ValueError as ve:
			print(f"Error al guardar datos en la base de datos: {ve}")
		except Exception as e:
			print(f"Error al guardar datos en la base de datos: {e}")

	def limpiar_campos(self):
		self.txt_codigo_in.setText("")
		self.txt_carro_in.setText("")
		self.txt_cantidad_in.setText("")
		self.txt_pc_in.setText("")
		self.txt_pv_in.setText("")
		self.tabla_pre_venta.clearContents()

	def calcular_precio(self):
		cantidad = int(self.txt_cantidad_in.text())
		precio = float(self.txt_pc_in.text())
		total = cantidad * precio
		self.txt_total_pro.setText(str(total))

	def ver_total_de_productos(self):
		# Inicializar la variable total
		total = 0
		# Recorrer las filas de la tabla_pre_venta
		for fila in range(self.tabla_pre_venta.rowCount()):
			# Obtener los valores de existencia y precio_costo de la fila actual
			existencia = int(self.tabla_pre_venta.item(fila, 2).text())
			precio_costo = float(self.tabla_pre_venta.item(fila, 3).text())

			# Calcular el subtotal de la fila actual
			subtotal = existencia * precio_costo

			# Sumar el subtotal al total acumulado
			total += subtotal

		# Mostrar el resultado
		print("El total de la multiplicación de existencia y precio_costo es:", total)
		self.txt_total_tabla.setText(str(total))

	def detalle_inventario_compra(self):
		try:
			# Crear cursor para ejecutar consultas
			self.conn = conecciones()
			cursor = self.conn.cursor()

			# Obtener el último ID de Inventario y Detalle_vi
			cursor.execute("SELECT MAX(idInventario) FROM Inventario")
			max_id_inv = cursor.fetchone()[0]
			cursor.execute("SELECT MAX(Ventario) FROM detalle_vi")
			max_id_det = cursor.fetchone()[0]

			# Completar los datos faltantes en Detalle_vi
			while max_id_det < max_id_inv:
				max_id_det += 1
				cursor.execute(
					"INSERT INTO detalle_vi (Ventario, prove, cantidad, Total) VALUES ( %s, %s, %s, %s)",
					(max_id_det, max_id_det, 1, 0))

			# Obtener los datos de la última Compra
			cursor.execute("SELECT MAX(idCompra), empresa, Total FROM Compra")
			max_id_com, empresa, total_com = cursor.fetchone()

			# Obtener los datos de los productos comprados recientemente
			cursor.execute("SELECT idInventario, existencia, precio_costo FROM Inventario WHERE idInventario > %s",
						   (max_id_inv - 1,))
			productos = cursor.fetchall()

			# Calcular el total de la última compra
			total_det = sum(p[1] * p[2] for p in productos)

			# Insertar los datos en la tabla Detalle_vi
			cursor.execute(
				"INSERT INTO detalle_vi (Ventario, prove, cantidad, Total) VALUES ( %s, %s, %s, %s)",
				(max_id_com, empresa, len(productos), total_det))

			# Actualizar el total en la tabla Compra
			cursor.execute("UPDATE Compra SET Total = %s WHERE idCompra = %s", (total_com + total_det, max_id_com))

			# Hacer commit de las transacciones
			self.conn.commit()

			# Cerrar el cursor y la conexión
			cursor.close()
			self.conn.close()

		except Exception as e:
			print("Error:", e)
			self.conn.rollback()

	def detalle(self):
		self.conn = conecciones()
		cursor = self.conn.cursor()

		# Contar registros en la tabla Inventario
		cursor.execute("SELECT COUNT(idInventario) FROM Inventario")
		num_inventario = cursor.fetchone()[0]

		# Contar registros en la tabla detalle_vi
		cursor.execute("SELECT COUNT(Ventario) FROM detalle_vi")
		num_detalle = cursor.fetchone()[0]

		# Obtener el último idCompra en la tabla Compra
		cursor.execute("SELECT MAX(idCompra) FROM Compra")
		ultimo_id_compra = cursor.fetchone()[0]

		# Mostrar resultados en un print
		print(f"Registros en Inventario: {num_inventario}")
		print(f"Registros en detalle_vi: {num_detalle}")
		print(f"Último idCompra: {ultimo_id_compra}")

		# Obtener los números que faltan en detalle_vi
		cursor.execute(
			"SELECT idInventario, existencia, precio_costo FROM Inventario WHERE idInventario NOT IN (SELECT Ventario FROM detalle_vi)")
		numeros_faltantes = cursor.fetchall()

		# Mostrar los números que faltan y calcular el total
		if numeros_faltantes:
			print("Números faltantes en detalle_vi:")
			for numero in numeros_faltantes:
				idInventario = numero[0]
				existencia = numero[1]
				precio_costo = numero[2]
				total = existencia * precio_costo
				cursor.execute(
					f"INSERT INTO detalle_vi (Ventario, prove, cantidad, total) VALUES ({idInventario}, {ultimo_id_compra}, {existencia}, {total})")
				self.conn.commit()
				print(f"Numero {idInventario} agregado a detalle_vi")
		else:
			QMessageBox.information(self, "Error", "No hay compras vinculadas")
			print("No hay números faltantes en detalle_vi.")

			# cursor.execute(f"INSERT INTO detalle_vi (prove) VALUES ({ultimo_id_compra})")
			# self.conn.commit()
			# print(f"Se ha insertado el valor de último idCompra en la tabla detalle_vi.")

	def actualizar_txt_tipo(self, index):
		# Obtener el texto seleccionado en el ComboBox
		texto_seleccionado = self.cb_tipo.currentText()

		# Obtener el valor asociado al texto seleccionado
		valores = {
			"Cargo Expreso": "1",
			"Guatex": "2",
			"Transportador": "3",
			"Recoger": "4"
		}
		valor_seleccionado = valores.get(texto_seleccionado)

		# Actualizar el texto del QLineEdit con el valor seleccionado
		self.txt_tipo.setText(valor_seleccionado)




