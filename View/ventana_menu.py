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
		# self.bt_cuatro.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_cuatro))
		# self.bt_cinco.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_cinco))

		# ver paginas-----
		self.btn_usuario_editar.clicked.connect(self.page_usuario)
		self.btn_usuario_ver.clicked.connect(self.page_usuario_v)
		self.btn_crear_sesion.clicked.connect(self.page_usuario_c)
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
		self.btn_g_u.clicked.connect(
			lambda: self.modelo_usuario.crearUsuario(self.txt_nombre_usuario_c.text(), self.txt_contra_u.text(),
													 self.txt_nombre_u.text(),
													 self.txt_apellido_u.text(),
													 self.txt_puesto_u.text()))

		self.btn_g_u.clicked.connect(self.limpiar_campos_usuario)

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

		# TODO PARA VENTAS
		self.tabla_venta.itemSelectionChanged.connect(self.cargar_datos_seleccionados_venta)
		self.btn_guardar_venta.clicked.connect(self.mostrar_compra_venta)
		self.btn_calcular_venta.clicked.connect(self.mostrar_codigo_venta)
		self.btn_editar_venta.clicked.connect(self.editar_datos_venta)
		self.btn_eliminar_venta_2.clicked.connect(self.eliminar_datos_venta)
		self.btn_finalizar_venta.clicked.connect(self.pasar_datos_tabla)
		self.btn_finalizar_venta.clicked.connect(self.finalizado_venta)
		self.btn_revisar_cliente.clicked.connect(self.revisar_cliente)
		self.btn_guardar_venta_2.clicked.connect(self.detalle_venta)
		# correcto self.btn_finalizar_venta.clicked.connect(self.pasar_datos_tabla)
		self.btn_ver_factura.clicked.connect(self.ultima_venta)
		self.btn_finalizar_venta_2.clicked.connect(self.ultima_detalle)


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

	def page_usuario_c(self):
		self.stackedWidget_2.setCurrentWidget(self.page_crear_u)

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

	def mostrar_coampra(self):
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
	def mostrar_compra(self):
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

	def guardar_datosoficial(self):
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
	                          VALUES (%s, %s, %s, %s, %s)
	                          ON DUPLICATE KEY UPDATE existencia = existencia + VALUES(existencia)"""
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

	# venta
	def mostrar_compra_venta(self):
		codigo = self.txt_codigo_venta.text()
		cantidad = self.txt_carro_venta.text()
		# fecha = self.txt_fecha.text()
		total = self.txt_total_Venta.text()
		usuario = self.txt_usuario_venta.text()
		cliente = self.txt_cliente_venta.text()

		if self.row_seleccionada is None:
			row_position = self.tabla_venta.rowCount()
			self.tabla_venta.insertRow(row_position)
		else:
			row_position = self.row_seleccionada

		self.tabla_venta.setItem(row_position, 0, QTableWidgetItem(codigo))
		self.tabla_venta.setItem(row_position, 1, QTableWidgetItem(cantidad))
		self.tabla_venta.setItem(row_position, 2, QTableWidgetItem(total))
		# self.tabla_venta.setItem(row_position, 3, QTableWidgetItem(fecha))
		# self.tabla_venta.setItem(row_position, 3, QTableWidgetItem(usuario))
		# self.tabla_venta.setItem(row_position, 4, QTableWidgetItem(cliente))

		self.txt_codigo_venta.clear()
		self.txt_carro_venta.clear()
		# self.txt_fecha.clear()
		self.txt_total_Venta.clear()
		# self.txt_usuario_venta.clear()
		# self.txt_cliente_venta.clear()
		self.txt_precio_venta_v.clear()

		self.row_seleccionada = None

	def editar_datos_venta(self):
		if self.row_seleccionada is None:
			QMessageBox.information(self, "Error", "Por favor seleccione una fila para editar.")
			print("error")
			return
		self.mostrar_compra_venta()

	def cargar_datos_seleccionados_venta(self):
		if len(self.tabla_venta.selectedItems()) > 0:
			items = self.tabla_venta.selectedItems()
			self.row_seleccionada = items[0].row()
			self.txt_codigo_venta.setText(self.tabla_venta.item(self.row_seleccionada, 0).text())
			self.txt_carro_venta.setText(self.tabla_venta.item(self.row_seleccionada, 1).text())
			self.txt_total_Venta.setText(self.tabla_venta.item(self.row_seleccionada, 2).text())
			# self.txt_fecha.setText(self.tabla_venta.item(self.row_seleccionada, 3).text())
			# self.txt_cliente_venta.setText(self.tabla_venta.item(self.row_seleccionada, 4).text())

	def eliminar_datos_venta(self):
		if self.row_seleccionada is None:
			QMessageBox.information(self, "Error", "Por favor seleccione una fila para eliminar.")
			return

		reply = QMessageBox.question(self, 'Eliminar fila', '¿Está seguro de que desea eliminar esta fila?',
									 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			self.tabla_venta.removeRow(self.row_seleccionada)
			self.txt_codigo_venta.clear()
			self.txt_carro_venta.clear()
			# self.txt_fecha.clear()
			self.txt_total_Venta.clear()
			# self.txt_cliente_venta.clear()
			self.txt_precio_venta_v.clear()
			self.row_seleccionada = None

	def mostrar_codigo_venta(self):
		try:
			# Obtener la cantidad y el código del carro del QLineEdit correspondiente
			codigo = self.txt_codigo_venta.text()
			cantidad = int(self.txt_carro_venta.text())
			print(f"Código del carro: {codigo}, Cantidad: {cantidad}")

			# Conectarse a la base de datos y obtener la cantidad de existencias y precio de venta del carro seleccion
			self.conn = conecciones()
			with self.conn.cursor() as cursor:
				sql = "SELECT existencia, precio_venta FROM Inventario WHERE codigo_carro = %s"
				cursor.execute(sql, (codigo,))
				result = cursor.fetchone()

			if result is not None:
				existencia, precio = result
				print(f"Existencia: {existencia}, Precio de venta: {precio}")
				self.txt_precio_venta_v.setText(str(precio))

				# Verificar si la cantidad solicitada es mayor a la cantidad en existencia
				if cantidad > existencia:
					# Mostrar un mensaje con la cantidad de existencias disponibles
					mensaje = QMessageBox()
					mensaje.setIcon(QMessageBox.Warning)
					mensaje.setWindowTitle('Error de inventario')
					mensaje.setText(f'Solo hay {existencia} unidades disponibles en inventario.')
					mensaje.exec_()
				else:
					# Realizar la multiplicación y mostrar el resultado en el QLineEdit correspondiente
					total = precio * cantidad
					self.txt_total_Venta.setText(str(total))
			else:
				mensaje = QMessageBox()
				mensaje.setIcon(QMessageBox.Warning)
				mensaje.setWindowTitle('Código no encontrado')
				mensaje.setText(f'El código {codigo} no existe en la base de datos.')
				mensaje.exec_()
			# Cerrar la conexión con la base de datos
			print("Cerrando la conexión a la base de datos...")
			self.conn.close()
		except Exception as e:
			print(f"Error: {e}")

	def finalizado_venta(self):
		# Establecer la conexión una vez
		self.conn = conecciones()
		cursor = self.conn.cursor()

		# Obtener el id del usuario
		usuario = self.txt_usuario_venta.text()
		cursor.execute("SELECT idUsuario FROM Usuario WHERE usuario = %s", (usuario,))
		result = cursor.fetchall()
		if result:
			id_usuario = result[0][0]
			print("El id del usuario", usuario, "es:", id_usuario)
		else:
			print("No se encontró el usuario:", usuario)
			return

		# Obtener el id del cliente
		cliente = self.txt_cliente_venta.text()
		cursor.execute("SELECT idCliente FROM Cliente WHERE nombre_cliente = %s", (cliente,))
		result = cursor.fetchall()
		if result:
			id_cliente = result[0][0]
			print("El id del cliente", cliente, "es:", id_cliente)
		else:
			print("No se encontró el cliente:", cliente)
			return

		# Calcular los totales
		total_cantidad = 0
		total_venta = 0
		for row in range(self.tabla_venta.rowCount()):
			cantidad = int(self.tabla_venta.item(row, 1).text())
			total_cantidad += cantidad
			total = float(self.tabla_venta.item(row, 2).text())
			total_venta += total
		print(f" cantidad {total_cantidad} +  fecha NULL +total {total_venta} +  usuario {id_usuario}  cliente + {id_cliente} ")
		datos = []
		datos.append((total_cantidad, None, total_venta, id_usuario, id_cliente))
		insert_query = """INSERT INTO Venta (cantidad, fecha,Total,Usuario_id,Cliente_id) 
			                            VALUES (%s, %s, %s, %s, %s)"""
		cursor.executemany(insert_query, datos)
		self.conn.commit()

		# Cerrar la conexión después del bucle
		cursor.close()
		self.conn.close()

		self.limpiar_campos_venta()
		self.tabla_venta.setRowCount(0)  # Eliminar las filas de la tabla
		QMessageBox.information(None, "Venta", "Venta Hecha")

	def limpiar_campos_venta(self):
		self.tabla_venta.clearContents()

	def revisar_cliente(self):
		try:
			self.conn = conecciones()
			cursor = self.conn.cursor()
			nombre_cliente = self.txt_cliente_venta.text()
			cursor.execute("SELECT nombre_cliente FROM Cliente WHERE nombre_cliente = %s", (nombre_cliente,))

			# Recuperar resultados
			resultados = cursor.fetchall()

			# Cerrar cursor y conexión

			# Mostrar alerta si el cliente no está en la base de datos
			if len(resultados) == 0:
				QMessageBox.critical(None, "Error", "El cliente no está en la base de datos")
			else:
				QMessageBox.information(None, "Cliente encontrado", "El cliente está en la base de datos")

			cursor.close()
			self.conn.close()

		except Exception as e:
			QMessageBox.critical(None, "Error", "Error al acceder a la base de datos: " + str(e))

	def pasar_datos_tabla(self):
		datos = []
		for fila in range(self.tabla_venta.rowCount()):
			fila_datos = []
			for columna in range(self.tabla_venta.columnCount()):
				item = self.tabla_venta.item(fila, columna)
				fila_datos.append(item.text())
			datos.append(fila_datos)

		# Limpiar la segunda QTableWidget
		self.tabla_venta_detalle.clear()

		# Configurar las columnas y filas en la segunda QTableWidget
		self.tabla_venta_detalle.setColumnCount(len(datos[0]))
		self.tabla_venta_detalle.setRowCount(len(datos))

		# Copiar los nombres de las columnas de la primera QTableWidget a la segunda
		for columna in range(self.tabla_venta.columnCount()):
			nombre_columna = self.tabla_venta.horizontalHeaderItem(columna).text()
			self.tabla_venta_detalle.setHorizontalHeaderItem(columna, QtWidgets.QTableWidgetItem(nombre_columna))

		# Insertar los datos en la segunda QTableWidget
		for fila, fila_datos in enumerate(datos):
			for columna, dato in enumerate(fila_datos):
				item = QtWidgets.QTableWidgetItem(str(dato))
				self.tabla_venta_detalle.setItem(fila, columna, item)

	def detalle_venta1(self):
		try:
			self.conn = conecciones()
			cursor = self.conn.cursor()

			# Obtener el último idVenta en la tabla Venta
			cursor.execute("SELECT MAX(idVenta) FROM Venta")
			ultimo_id_venta = cursor.fetchone()[0]

			# Mostrar detalle de venta
			for fila in range(self.tabla_venta_detalle.rowCount()):
				codigo_carro = self.tabla_venta_detalle.item(fila, 0).text()
				consulta = """
	                SELECT idInventario
	                FROM Inventario
	                WHERE codigo_carro = %s
	            """
				cursor.execute(consulta, (codigo_carro,))
				idInventario = cursor.fetchone()[0]
				cantidad = self.tabla_venta_detalle.item(fila, 1).text()
				precio = self.tabla_venta_detalle.item(fila, 2).text()

				# Insertar detalle de venta en tabla detalle_venta
				consulta = """
	                INSERT INTO detalle_venta (venta_id, inventario_id, codigo, cantidad, sub_total)
	                VALUES (%s, %s, %s, %s, %s)
	            """
				sub_total = 1 * float(precio)
				valores = (ultimo_id_venta, idInventario, codigo_carro, cantidad, sub_total)
				cursor.execute(consulta, valores)
				self.conn.commit()

				print(
					f" IdVenta: {ultimo_id_venta}, IdInventario: {idInventario}, Código de carro: {codigo_carro}, Cantidad: {cantidad}, Precio: {precio}")

			self.limpiar_campos_venta_detalle()

		except Exception as e:
			print(f"Ocurrió un error: {e}")

	def limpiar_campos_venta_detalle1(self):
		self.tabla_venta_detalle.clearContents()

	def detalle_venta(self):
		try:
			self.conn = conecciones()
			cursor = self.conn.cursor()

			# Obtener el último idVenta en la tabla Venta
			cursor.execute("SELECT MAX(idVenta) FROM Venta")
			ultimo_id_venta = cursor.fetchone()[0]

			# Mostrar detalle de venta
			for fila in range(self.tabla_venta_detalle.rowCount()):
				codigo_carro = self.tabla_venta_detalle.item(fila, 0).text()
				consulta = """
	                SELECT idInventario
	                FROM Inventario
	                WHERE codigo_carro = %s
	            """
				cursor.execute(consulta, (codigo_carro,))
				idInventario = cursor.fetchone()[0]
				cantidad = self.tabla_venta_detalle.item(fila, 1).text()
				precio = self.tabla_venta_detalle.item(fila, 2).text()

				# Insertar detalle de venta en tabla detalle_venta
				consulta = """
	                INSERT INTO detalle_venta (venta_id, inventario_id, codigo, cantidad, sub_total)
	                VALUES (%s, %s, %s, %s, %s)
	            """
				sub_total = 1 * float(precio)
				valores = (ultimo_id_venta, idInventario, codigo_carro, cantidad, sub_total)
				cursor.execute(consulta, valores)
				self.conn.commit()

				print(
					f" IdVenta: {ultimo_id_venta}, IdInventario: {idInventario}, Código de carro: {codigo_carro}, Cantidad: {cantidad}, Precio: {precio}")

			self.limpiar_campos_venta_detalle()
			self.tabla_venta_detalle.clearContents()  # Eliminar contenido de la tabla
			self.tabla_venta_detalle.setRowCount(0)  # Eliminar las filas de la tabla
			self.txt_cliente_venta.clear()

		except Exception as e:
			print(f"Ocurrió un error: {e}")

	def limpiar_campos_venta_detalle(self):
		self.tabla_venta_detalle.clearContents()

	def limpiar_campos_usuario(self):
		self.txt_nombre_usuario_c.clear()
		self.txt_contra_u.clear()
		self.txt_nombre_u.clear()
		self.txt_apellido_u.clear()
		self.txt_puesto_u.clear()

	def ultima_venta1(self):
		self.conn = conecciones()
		cursor = self.conn.cursor()
		cursor.execute(
			'SELECT cantidad, fecha, Total, Usuario_id, Cliente_id FROM Venta WHERE idVenta = (SELECT MAX(idVenta) FROM Venta)')
		resultados = cursor.fetchall()
		print(resultados)
		fila = resultados[0]
		self.tabla_factura.setRowCount(1)  # Asignar 1 fila para el registro
		self.tabla_factura.setColumnCount(len(fila))  # Asignar la cantidad adecuada de columnas
		for j, valor in enumerate(fila):
			item = QtWidgets.QTableWidgetItem(str(valor))
			self.tabla_factura.setItem(0, j, item)
		self.conn.close()

	def ultima_venta(self):
		self.conn = conecciones()
		cursor = self.conn.cursor()
		cursor.execute(
			'SELECT Venta.cantidad, Venta.fecha, Venta.Total, Usuario.usuario, Cliente.nombre_cliente FROM Venta JOIN Usuario ON Venta.Usuario_id = idUsuario JOIN Cliente ON Venta.Cliente_id = idCliente WHERE Venta.idVenta = (SELECT MAX(idVenta) FROM Venta)')
		resultados = cursor.fetchall()
		print(resultados)
		fila = resultados[0]
		self.tabla_factura.setRowCount(1)
		self.tabla_factura.setColumnCount(len(fila))
		for j, valor in enumerate(fila):
			item = QtWidgets.QTableWidgetItem(str(valor))
			self.tabla_factura.setItem(0, j, item)
		self.conn.close()

	def ultima_detalle(self):
		datos = []
		for fila in range(self.tabla_venta.rowCount()):
			fila_datos = []
			for columna in range(self.tabla_venta.columnCount()):
				item = self.tabla_venta.item(fila, columna)
				fila_datos.append(item.text())
			datos.append(fila_datos)

		# Limpiar la segunda QTableWidget
		# self.tabla_venta_detalle.clear()

		# Configurar las columnas y filas en la segunda QTableWidget
		self.tabla_factura_2.setColumnCount(len(datos[0]))
		self.tabla_factura_2.setRowCount(len(datos))

		# Copiar los nombres de las columnas de la primera QTableWidget a la segunda
		for columna in range(self.tabla_venta.columnCount()):
			nombre_columna = self.tabla_venta.horizontalHeaderItem(columna).text()
			self.tabla_factura_2.setHorizontalHeaderItem(columna, QtWidgets.QTableWidgetItem(nombre_columna))

		# Insertar los datos en la segunda QTableWidget
		for fila, fila_datos in enumerate(datos):
			for columna, dato in enumerate(fila_datos):
				item = QtWidgets.QTableWidgetItem(str(dato))
				self.tabla_factura_2.setItem(fila, columna, item)
