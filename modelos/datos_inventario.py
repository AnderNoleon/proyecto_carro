from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from controladores.usuarioCon import RegistrarUsuario

# el eliminar, corregir


class ModeloInventario():
    def __int__(self):
        self.usuario = RegistrarUsuario()
        self.tabla_pre_venta.itemSelectionChanged.connect(self.cargar_datos_seleccionados)
        self.row_seleccionada = None

    def listar_Usuario(self, tabla):
        self.usuario = RegistrarUsuario()
        table = tabla
        usuarios = self.usuario.obtener_usuario()
        table.setRowCount(0)
        for row_number, row_data in enumerate(usuarios):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def crearUsuario(self, usuario, contrasena, nombre, apellido, puesto):
        self.usuario = RegistrarUsuario()
        if usuario and contrasena and nombre and apellido and puesto:
            print("-DATOS ENVIANDOS---")
            self.usuario.insertarUsuario(usuario, contrasena,nombre,apellido,puesto)

    def eliminar_Usuario(self, table):
        self.usuario = RegistrarUsuario()
        table = table
        if table.currentItem() != None:
            cod = table.currentItem().text()
            product = self.usuario.getUsuario(cod)
            if product:
                self.usuario.eliminarUsuario(cod)
        self.listar_Usuario(table)

    def subir_usuarios(self, tabla):
        self.usuario = RegistrarUsuario()
        table = tabla
        products = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number, column_number) != None:
                    fila.append(table.item(row_number, column_number).text())
            if len(fila) > 0:
                products.append(fila)
            fila = []

        if len(products) > 0:
            for prod in products:
                self.usuario.subirUsuario(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5])
        self.listar_Usuario(tabla)

    # PRUEBA de la tabla

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
            # QMessageBox.information(self, "Error", "Por favor seleccione una fila para editar.")
            print("error")
            return

        self.mostrar_compra()
