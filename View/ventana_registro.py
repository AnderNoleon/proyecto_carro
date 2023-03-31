import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QTextEdit, QVBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Crea el QComboBox y el QTextEdit
        self.combo = QComboBox(self)
        self.combo.addItem('Opción 0')
        self.combo.addItem('Opción 1')
        self.combo.addItem('Opción 2')
        self.combo.addItem('Opción 3')
        self.combo.currentIndexChanged.connect(self.updateTextEdit)

        self.textEdit = QTextEdit(self)

        # Crea el layout y agrega los widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.combo)
        vbox.addWidget(self.textEdit)

        # Configura el layout de la ventana
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Ejemplo QComboBox y QTextEdit')
        self.show()

    def updateTextEdit(self):
        selected = self.combo.currentText()

        if selected == 'Opción 0':
            self.textEdit.setPlainText('')
        elif selected == 'Opción 1':
            self.textEdit.setPlainText('Has seleccionado la opción 1.')
        elif selected == 'Opción 2':
            self.textEdit.setPlainText('Has seleccionado la opción 2.')
        elif selected == 'Opción 3':
            self.textEdit.setPlainText('Has seleccionado la opción 3.')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())