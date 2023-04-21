from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow
from server.conexion_sql import conecciones
from View import Main_window, Menu
import sys


class Main_login(QMainWindow):
    def __init__(self) -> None:
        super(Main_login, self).__init__()
        uic.loadUi("View/loginUi2.ui", self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.conn = conecciones()
        self.ventana_principal = Main_window()

        # Conectar el botón "Entrar"
        self.btn_entrar.clicked.connect(self.abrir)

    def abrir(self):
        usuario = self.txt_login.text()
        contra = self.txt_password.text()
        cursor = self.conn.cursor()
        cursor.execute("select * from usuario where usuario='"+usuario+"' and contrasena ='"+contra+"'")
        result = cursor.fetchone()

        if result:
            # Mostrar la ventana principal
            self.ventana_principal.show()
            self.hide()

            # Acceder y actualizar el objeto QLineEdit en menu.ui
            menu = Menu()
            menu.txt_admin_menu.setText(usuario)

        else:
            print("Contraseña incorrecta")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Main_login()
    login.show()
    sys.exit(app.exec_())