from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.usuarioCon import RegistrarUsuario
import hashlib

# el eliminar, corregir


class ModeloUsuario():
    def __int__(self):
        self.usuario = RegistrarUsuario()

    def listar_Usuario(self, tabla):
        self.usuario = RegistrarUsuario()
        table = tabla
        usuarios = self.usuario.obtener_usuario()
        table.setRowCount(0)
        for row_number, row_data in enumerate(usuarios):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

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

    def crearUsuario(self, usuario, contrasena, nombre, apellido, puesto):
        self.usuario = RegistrarUsuario()
        if usuario and contrasena and nombre and apellido and puesto:
            print("-DATOS ENVIADOS---")
            QMessageBox.information(None, "Usuario", "El Usuario está en la base de datos")
            hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
            print(f"{usuario}+{hashed_password}+{nombre}+{apellido}+{puesto}")
            self.usuario.insertarUsuario(usuario, hashed_password, nombre, apellido, puesto)