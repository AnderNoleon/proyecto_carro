from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLineEdit, QVBoxLayout
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        # Crear el ComboBox y el QLineEdit
        self.cb_tipo = QComboBox()
        self.cb_tipo.addItems(["Cargo Expreso", "Guatex", "Transportador", "Recoger"])
        self.txt_tipo = QLineEdit()

        # Conectar la señal currentIndexChanged al método actualizar_txt_tipo
        self.cb_tipo.currentIndexChanged.connect(self.actualizar_txt_tipo)

        # Crear el layout y añadir los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.cb_tipo)
        layout.addWidget(self.txt_tipo)
        self.setLayout(layout)

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
