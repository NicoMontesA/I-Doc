
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Form(QWidget):
    # Se crea una nueva clase "Form", la cual hereda las características de la clase "QWidget".

    def __init__(self, parent=None):
	# El constructor por defecto no tiene "parent", por lo tanto se crea uno.
        super(Form, self).__init__(parent)


        nameLabel = QLabel("Nombre:")			# Etiqueta.
        self.nameLine = QLineEdit()			# Caja para recibir una entrada.
        self.submitButton = QPushButton("Guardar")	# Boton para enviar.

        ageLabel = QLabel("Edad:")
        self.ageLine = QLineEdit()
        self.submitButton2 = QPushButton("Guardar")

        heightLabel = QLabel("Estatura [mts.]:")
        self.heightLine = QLineEdit()
        self.submitButton3 = QPushButton("Guardar")

        weightLabel = QLabel("Peso [kg.]:")
        self.weightLine = QLineEdit()
        self.submitButton4 = QPushButton("Guardar")

        sexLabel = QLabel("Sexo [M/F]:")
        self.sexLine = QLineEdit()
        self.submitButton5 = QPushButton("Guardar")


	# ELEMENTOS VENTANA 1: RECEPCIÓN DE ANTECEDENTES PERSONALES.-
	# ==========================================================
        buttonLayout1 = QVBoxLayout()		# QVBoxLayout() alinea los widgets de forma vertical.
	
	# Elementos que componen "nameLabel"
        buttonLayout1.addWidget(nameLabel)			
        buttonLayout1.addWidget(self.nameLine)
#        buttonLayout1.addWidget(self.submitButton)

	# Elementos que componen "ageLabel"
        buttonLayout1.addWidget(ageLabel)
        buttonLayout1.addWidget(self.ageLine)
#        buttonLayout1.addWidget(self.submitButton2)

	# Elementos que componen "heightLabel"
        buttonLayout1.addWidget(heightLabel)
        buttonLayout1.addWidget(self.heightLine)
#        buttonLayout1.addWidget(self.submitButton3)

	# Elementos que componen "weightLabel"
        buttonLayout1.addWidget(weightLabel)
        buttonLayout1.addWidget(self.weightLine)
#        buttonLayout1.addWidget(self.submitButton4)

	# Elementos que componen "sexLabel"
        buttonLayout1.addWidget(sexLabel)
        buttonLayout1.addWidget(self.sexLine)

        buttonLayout1.addWidget(self.submitButton)


	# ELEMENTOS VENTANA 2: RECEPCIÓN DE SÍNTOMAS.-
	# ===========================================
        buttonLayout2 = QVBoxLayout()		    	# Crea la ventana                
	
	# Elementos que componen la ventana: "nameLabel"
        buttonLayout2.addWidget(nameLabel)		
        buttonLayout2.addWidget(self.nameLine)
        buttonLayout2.addWidget(self.submitButton)




	# Llama a la función "submitContact" al presionar el botón "submitButton". 
        self.submitButton.clicked.connect(self.submitContact)

	# QGridLayout() ordena los widgets con coordenadas cartesianas.
        mainLayout = QGridLayout()
        # mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addLayout(buttonLayout1, 0, 1)

	# setLayout determina "mainLayout" como la ventana principal.
        self.setLayout(mainLayout)
        self.setWindowTitle("I-Doc")


    def submitContact(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field",
                                    "Please enter a name and address.")
            return
        else:
            QMessageBox.information(self, "Success!",
                                    "Hello %s!" % name)



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()
    print('\n\nSe inicio objeto screen\n\n')

    sys.exit(app.exec_())


