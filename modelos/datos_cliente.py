from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from controladores.clienteCon import RegistarCliente


class ModeloCliente():
    def __int__(self):
        self.cliente = RegistarCliente()

    def listar_cliente(self, tabla):
        self.cliente = RegistarCliente()
        table = tabla
        clientes = self.cliente.obtener_cliente()
        table.setRowCount(0)
        for row_number, row_data in enumerate(clientes):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def crearcliente(self, nombre, nit, celular, direccion, tipo):
        self.cliente = RegistarCliente()
        if nombre and nit and celular and direccion and tipo:
            print("-DATOS ENVIANDOS---")
            self.cliente.insertarCliente(nombre, nit, celular, direccion, tipo)

    def eliminar_cliente(self, table):
        self.cliente = RegistarCliente()
        table = table
        if table.currentItem() != None:
            cod = table.currentItem().text()
            product = self.cliente.getcliente(cod)
            if product:
                self.cliente.eliminarcliente(cod)
        self.listar_cliente(table)

    def tipo_medio(self):
        self.cb_tipo.currentIndexChanged.connect(self.updateTextEdit)
        selected = self.cb_tipo.currentText()
        if selected == 'Cargo Expreso':
            self.txt_tipo.setPlainText('1')
        elif selected == 'Guatex':
            self.txt_tipo.setPlainText('2')
        elif selected == 'Transportador':
            self.txt_tipo.setPlainText('3')
        elif selected == 'Recoger':
            self.txt_tipo.setPlainText('4')

    def subir_usuarios(self, tabla):
        self.cliente = RegistarCliente()
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
                self.cliente.subirCliente(prod[0], prod[1], prod[2], prod[3], prod[4], prod[5])
        self.listar_cliente(tabla)
