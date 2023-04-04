from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, QLineEdit, \
    QPushButton, QMessageBox
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agregar, editar y eliminar datos en una tabla")
        self.layout = QVBoxLayout()

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(['Nombre', 'Edad'])
        self.tabla.setSelectionBehavior(QTableWidget.SelectRows)
        self.tabla.itemSelectionChanged.connect(self.cargar_datos_seleccionados)

        self.nombre = QLineEdit()
        self.edad = QLineEdit()

        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.clicked.connect(self.guardar_datos)

        self.btn_editar = QPushButton("Editar")
        self.btn_editar.clicked.connect(self.editar_datos)

        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_datos)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn_guardar)
        hbox.addWidget(self.btn_editar)
        hbox.addWidget(self.btn_eliminar)

        self.layout.addWidget(self.nombre)
        self.layout.addWidget(self.edad)
        self.layout.addLayout(hbox)
        self.layout.addWidget(self.tabla)

        self.setLayout(self.layout)

        self.row_seleccionada = None

    def cargar_datos_seleccionados(self):
        if len(self.tabla.selectedItems()) > 0:
            items = self.tabla.selectedItems()
            self.row_seleccionada = items[0].row()
            self.nombre.setText(self.tabla.item(self.row_seleccionada, 0).text())
            self.edad.setText(self.tabla.item(self.row_seleccionada, 1).text())

    def guardar_datos(self):
        nombre = self.nombre.text()
        edad = self.edad.text()

        if not nombre or not edad:
            return

        if self.row_seleccionada is None:
            row_position = self.tabla.rowCount()
            self.tabla.insertRow(row_position)
        else:
            row_position = self.row_seleccionada

        self.tabla.setItem(row_position, 0, QTableWidgetItem(nombre))
        self.tabla.setItem(row_position, 1, QTableWidgetItem(edad))

        self.nombre.clear()
        self.edad.clear()
        self.row_seleccionada = None

    def editar_datos(self):
        if self.row_seleccionada is None:
            QMessageBox.information(self, "Error", "Por favor seleccione una fila para editar.")
            return

        self.guardar_datos()

    def eliminar_datos(self):
        if self.row_seleccionada is None:
            QMessageBox.information(self, "Error", "Por favor seleccione una fila para eliminar.")
            return

        reply = QMessageBox.question(self, 'Eliminar fila', '¿Está seguro de que desea eliminar esta fila?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.tabla.removeRow(self.row_seleccionada)
            self.nombre.clear()
            self.edad.clear()
            self.row_seleccionada = None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

import mysql.connector


# ...

class MainWindow(QWidget):
    # ...

    def guardar_datos(self):
        nombre = self.nombre.text()
        edad = self.edad.text()

        if not nombre or not edad:
            return

        cnx = mysql.connector.connect(user='usuario', password='contraseña',
                                      host='localhost',
                                      database='basedatos')

        cursor = cnx.cursor()

        if self.row_seleccionada is None:
            insert_query = "INSERT INTO datos (nombre, edad) VALUES (%s, %s)"
            data = (nombre, edad)
            cursor.execute(insert_query, data)
        else:
            update_query = "UPDATE datos SET nombre=%s, edad=%s WHERE id=%s"
            data = (nombre, edad, self.tabla.item(self.row_seleccionada, 0).text())
            cursor.execute(update_query, data)

        cnx.commit()
        cursor.close()
        cnx.close()

        self.nombre.clear()
        self.edad.clear()
        self.row_seleccionada = None