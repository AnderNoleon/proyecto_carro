from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from server.conexion_sql import conecciones
from controladores.proveedorCon import R_proveedor


class ModeloPrincipal():
    def __int__(self, principal):
        self.producto = R_proveedor()
        self.principal = principal

    def crearProducto(self, empresa, total):
        self.producto = R_proveedor()
        if empresa and total:
            print("mandando datos")
            self.producto. insertarProveedor(empresa, total)