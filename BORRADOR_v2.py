
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import Enfermedades as enf
import os
from CreacionReceta import *


# CLASE PARA GENERAR LA VENTANA N1: RECEPCIÓN DE DATOS.-   
# ======================================================    
class Recepcion_Datos(QWidget):
	"""Esta clase esta destinada a la ventana en la cual se recepcionan los datos del paciente"""	
	# Nueva clase "Recepcion_Datos", la cual hereda las características de la clase "QWidget".

	def __init__(self, parent=None):

		# El constructor por defecto no tiene "parent", por lo tanto se crea uno.
		super(Recepcion_Datos, self).__init__(parent)


		nameLabel = QLabel("Nombre:")			# Etiqueta.
		self.nameLine = QLineEdit()			# Caja para recibir una entrada.
		self.submitButton = QPushButton("Guardar")	# Boton para enviar.

		ageLabel = QLabel("Edad:")
		self.ageLine = QLineEdit()

		heightLabel = QLabel("Estatura [mts.]:")
		self.heightLine = QLineEdit()

		weightLabel = QLabel("Peso [kg.]:")
		self.weightLine = QLineEdit()

		sexLabel = QLabel("Sexo [M/F]:")
		self.sexLine = QLineEdit()


		# ELEMENTOS VENTANA 1: RECEPCIÓN DE ANTECEDENTES PERSONALES.-
		# ==========================================================
		buttonLayout1 = QVBoxLayout()	# QVBoxLayout() alinea los widgets de forma vertical.
	
		# Elementos que componen "nameLabel"
		buttonLayout1.addWidget(nameLabel)			
		buttonLayout1.addWidget(self.nameLine)

		# Elementos que componen "ageLabel"
		buttonLayout1.addWidget(ageLabel)
		buttonLayout1.addWidget(self.ageLine)

		# Elementos que componen "heightLabel"
		buttonLayout1.addWidget(heightLabel)
		buttonLayout1.addWidget(self.heightLine)

		# Elementos que componen "weightLabel"
		buttonLayout1.addWidget(weightLabel)
		buttonLayout1.addWidget(self.weightLine)

		# Elementos que componen "sexLabel"
		buttonLayout1.addWidget(sexLabel)
		buttonLayout1.addWidget(self.sexLine)

        	# Se crea el botón
		buttonLayout1.addWidget(self.submitButton)



		# ENTREGA UNA APLIACACIÓN AL BOTON "submitButton" AL SER PRESIONADO.- 
		self.submitButton.clicked.connect(self.submitContact)


		# QGridLayout() ordena los widgets con coordenadas cartesianas.
		mainLayout = QGridLayout()
		# mainLayout.addWidget(nameLabel, 0, 0)
		mainLayout.addLayout(buttonLayout1, 0, 1)


		# setLayout determina "mainLayout" como la ventana principal.
		self.setLayout(mainLayout)
		self.setWindowTitle("I-Doc")

		# Mensaje de saludo inicial.-
		QMessageBox.information(self, "Empty Field", "Hola, soy I-Doc 👨‍🔬 \n\nEstaré encantado de ayudarte!")



	def submitContact(self):
		ventana2.show()
		self.nombre 	= self.nameLine.text()
		self.nombre 	= self.nombre.strip()		# Corrije la entrada de espacios antes y despues del nombre.

		self.edad 	= self.ageLine.text()
		self.edad 	= self.edad.strip()

		self.estatura	= self.heightLine.text()
		self.estatura 	= self.estatura.replace(',','.') # Corrije la entrada anterior si se ingresó un punto en vez de una coma.
		self.estatura 	= self.estatura.strip()

		self.peso 	= self.weightLine.text()
		self.peso 	= self.peso.strip()

		self.sexo 	= self.sexLine.text()
		self.sexo 	= self.sexo.strip()

		if self.nombre == "" or self.edad == "" or self.estatura == "" or self.peso == "" or self.sexo == "":
			QMessageBox.information(self, "Empty Field",
                                    "Por favor, revise que haya llenado todos los acápites para poder continuar.")




# CLASE PARA GENERAR LA VENTANA N2: RECEPCIÓN DE SÍNTOMAS.-
# =========================================================
class Recepcion_Sintomas(QWidget):
	"""Esta clase esta destinada a la ventana en la cual se recepcionan los síntomas del paciente"""	
	# Nueva clase "Recepcion_Sintomas", la cual hereda las características de la clase "QWidget".

	def __init__(self, parent=None):

		# El constructor por defecto no tiene "parent", por lo tanto se crea uno.
		super(Recepcion_Sintomas, self).__init__(parent)
		
		etiquetaSaludo = QLabel('Por favor lee los siguientes síntomas y dime cuales son los tuyos, para ello anota los números separados por una \",\".\nCuando hayas terminado presiona el botón \"Guardar\"')

		etiquetaSintoma = QLabel("Síntomas:")		# Etiqueta.

		posiblesSintomas = QLabel("1.Dolor de cabeza.\t2.Mucosa.\n3.Dolor de estómago.\t4.Tos.\n5.Indigestión.\t\t6.Decaimiento.\n7.Frio.\n""")		

		self.ingresoSintomas = QLineEdit()		# Caja para recibir los síntomas.

		self.guardarSintomas = QPushButton("Guardar")	# Boton para guardar los síntomas.  
		
		self.retirarReceta = QPushButton("Retirar Receta")	# Boton para guardar los síntomas.  


		
		# ELEMENTOS VENTANA 2: RECEPCIÓN DE ANTECEDENTES PERSONALES.-
		# ==========================================================
		buttonLayout1 = QVBoxLayout()	# QVBoxLayout() alinea los widgets de forma vertical.

		# Elementos que componen "etiqueraSaludo"
		buttonLayout1.addWidget(etiquetaSaludo)
	
		# Elementos que componen "etiquetaSintoma"
		buttonLayout1.addWidget(etiquetaSintoma)			

		# Elementos que componen "posiblesSintomas"
		buttonLayout1.addWidget(posiblesSintomas)

		# Elementos que componen "etiquedaSaludo"
		buttonLayout1.addWidget(etiquetaSaludo)

		# Elementos que componen "ingresoSintomas"
		buttonLayout1.addWidget(self.ingresoSintomas)

        	# Se crea el botón "guardarSintomas"
		buttonLayout1.addWidget(self.guardarSintomas)

		# Se crea el botón "retirarReceta"
	#	buttonLayout1.addWidget(self.retirarReceta)


		# ENTREGA UNA APLIACACIÓN AL BOTON "guadarSintomas" AL SER PRESIONADO.- 
		self.guardarSintomas.clicked.connect(self.submitContact)

		# ENTREGA UNA APLIACACIÓN AL BOTON "retirarReceta" AL SER PRESIONADO.- 
	#	self.retirarReceta.clicked.connect(self.abrirReceta)


		# QGridLayout() ordena los widgets con coordenadas cartesianas.
		mainLayout = QGridLayout()
		# mainLayout.addWidget(nameLabel, 0, 0)
		mainLayout.addLayout(buttonLayout1, 0, 1)


		# setLayout determina "mainLayout" como la ventana principal.
		self.setLayout(mainLayout)
		self.setWindowTitle("I-Doc")



	def submitContact(self):
		# "sintomasString" lee lo que se encuentra en la caja "self.ingresoSintomas" y lo transforma en un strng.
		sintomasString = self.ingresoSintomas.text()
		sintomasString = sintomasString.replace(' ','') # Solución en caso que hayan agregado un espacio entre o despues de los numeros.
		sintomasString = sintomasString.strip(',') 	# Solución en caso que hayan comas al inicio o al final del string.


		# "sintomasList" transforma "sintomasString" en una lista con los argumentos.
		sintomas_paciente = sintomasString.split(',')
		
		for i in sintomas_paciente:
			while sintomas_paciente.count(i) > 1:
				sintomas_paciente.remove(i)
				


		# ===================================================================================
		# ESTO ES PARA VERIFICARLO POR EL TERMINAL, BORRAR LUEGO
		print(sintomas_paciente)
		# ===================================================================================
		
		verificador = 0 	# Si es 0, los datos ingresados estan bien, al cambiar a 1 indica error en los datos ingresados.

		for i in sintomas_paciente:
			# Este "for" recorre la lista con los síntomas, verificando si se ingresó uno no válido.
			if i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7':
				QMessageBox.information(self, "Success!","Ingresó un número no válido, por favor ingrese otro.")
				verificador = 1 	# 1 porque hay un error en los datos.

		resfrio		= 0			# Contadores para declarar las enfermedaes.
		jaqueca		= 0
		gastroenteritis = 0

		for i in sintomas_paciente:
			# Este "for" recorre los síntomas para asociarlos a alguna enfermedad, agregando un contador a cada enfermedad, dependiendo de si el sintoma corresponde o no a ella.
			if i == '1':
				# Dolor de cabeza.
				resfrio += 1
				jaqueca += 1

			elif i == '2':
				# Mucosa.
				resfrio += 1
				jaqueca += 1

			elif i == '3':
				# Dolor de estómago.
				gastroenteritis += 1

			elif i == '4':
				# Tos.
				resfrio += 1

			elif i == '5':
				# Indigestión
				gastroenteritis += 1

			elif i == '6':
				# Decaimiento
				resfrio += 1

			elif i == '7':
				# Frio
				resfrio += 1

		# ===================================================================================
		# ESTO ES PARA VERIFICARLO A TRAVÉS DEL TERMINAL, BORRAR LUEGO.
		print('resfrio 		=', resfrio)
		print('jaqueca 		=', jaqueca)
		print('gastroenteritis 	=', gastroenteritis)
		# ===================================================================================



		# RELACION CONTADOR ENFERMEDAD CON CANTIDAD DE SINTOMAS.-
		# ======================================================

		# Al conocer cual es la enfermedad que tiene el mayor contador, se crea el el objeto "paciente" con ella.

		if resfrio > jaqueca and resfrio > gastroenteritis and verificador == 0:
			# Caso cuando el paciente se encuentra resfriado.
			paciente = enf.Resfrio(ventana1.nombre,ventana1.edad,ventana1.estatura,ventana1.peso,ventana1.sexo)
			paciente.tratamiento()
			Generacion_Receta(ventana1.nombre,ventana1.edad,ventana1.estatura,ventana1.peso,ventana1.sexo)

			QMessageBox.information(self, "Success", "Usted tiene RESFRIO, por favor retire su receta y siga el tratamiento indicado.\n\nFue un gusto ayudarlo!")

			# ===========================================================================
			# BORRAR ESTE Y LOS SIGUIENTES "print", ESTÁN PARA VERIFICAR QUE LA CLASE SE INICIE DE MANERA CORRECTA.
			print('Paciente de la clase Resfrio')
			# ===========================================================================

		elif jaqueca > resfrio and jaqueca > gastroenteritis and verificador == 0:
			# Caso cuando el paciente se encuentra con jaqueca.
			paciente = enf.Jaqueca(ventana1.nombre,ventana1.edad,ventana1.estatura,ventana1.peso,ventana1.sexo)
			Generacion_Receta(ventana1.nombre,ventana1.edad,ventana1.estatura,ventana1.peso,ventana1.sexo)
			paciente.tratamiento()

			QMessageBox.information(self, "Success", "Usted tiene JAQUECA, por favor retire su receta y siga el tratamiento indicado.\n\nFue un gusto ayudarlo!")
			print('Paciente de la clase Jaqueca')

		elif gastroenteritis > resfrio and gastroenteritis > jaqueca and verificador == 0:
			# Caso cuando el paciente se encuentra con gastroenteritis.
			paciente = enf.Gastroenteritis(ventana1.nombre,ventana1.edad,ventana1.estatura,ventana1.peso,ventana1.sexo)
			Generacion_Receta(ventana1.nombre,ventana1.edad,ventana1.estatura,ventana1.peso,ventana1.sexo)
			paciente.tratamiento()
			QMessageBox.information(self, "Success", "Usted tiene GASTROENTERITIS, por favor retire su receta y siga el tratamiento indicado.\n\nFue un gusto ayudarlo!")

		elif verificador == 0:
			# Caso cuando el paciente se encuentra con múltiples síntomas y no se pudo determinar con certeza a qué enfermeda específica corresponde.
			QMessageBox.information(self, "Success", "Su caso parece grave. ☠️\n\nPor favor vaya al hospital más cercano!")                                              
			print('\nNo se asignó a una clase, contadores iguales.\n')

		

	def abrirReceta(self):
		# "abrirReceta()" es la función que abre la receta cuando el paciente preciona el boton "retirarReceta".
		os.startfile('RecetaPrueba.pdf') 
		#open('RecetaPrueba.pdf')
	



# EJECUCIÓN DEL CÓDIGO.-
# ======================

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    ventana1 = Recepcion_Datos()
    ventana1.show()
    print('\n\nSe inicio objeto ventana1\n\n')

    ventana2 = Recepcion_Sintomas()
    print('\n\nSe inicio objeto ventana2\n\n')

    sys.exit(app.exec_())



