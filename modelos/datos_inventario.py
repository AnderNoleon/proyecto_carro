from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from controladores.inventarioCon import RegistrarInventario

# el eliminar, corregir


class ModeloInventario():
    def __int__(self):
        self.inventario = RegistrarInventario()
        # self.tabla_pre_venta.itemSelectionChanged.connect(self.cargar_datos_seleccionados)
        # self.row_seleccionada = None

    def listar_inventario(self, tabla):
        self.inventario = RegistrarInventario()
        table = tabla
        inventario = self.inventario.obtener_producto()
        table.setRowCount(0)
        for row_number, row_data in enumerate(inventario):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def crearInventario(self, usuario, contrasena, nombre, apellido, puesto):
        self.usuario = RegistrarInventario()
        if usuario and contrasena and nombre and apellido and puesto:
            print("-DATOS ENVIANDOS---")
            self.usuario.insertarUsuario(usuario, contrasena,nombre,apellido,puesto)

    def eliminar_inventario(self, table):
        self.usuario = RegistrarInventario()
        table = table
        if table.currentItem() != None:
            cod = table.currentItem().text()
            product = self.usuario.getUsuario(cod)
            if product:
                self.usuario.eliminarUsuario(cod)
        self.listar_Usuario(table)

    def subir_invetario(self, tabla):
        self.inventario = RegistrarInventario()
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
                self.inventario.subirproducto(prod[1], prod[2], prod[3], prod[4], prod[5], prod[6])
        self.listar_inventario(tabla)

