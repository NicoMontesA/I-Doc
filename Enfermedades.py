# Este archivo contiene las clases que definen las enfermedades.


# CLASE RESFRIO.-
# ==============
class Resfrio:
	"""Clase cuando el paciente se encuentra resfriado"""
	
	# DATOS DEL PACIENTE.-
	def __init__(self, nombre, edad, estatura, peso, sexo):
		self.nombre   = nombre
		self.edad     = edad
		self.estatura = estatura
		self.peso     = peso
		self.sexo     = sexo
		self.enfermedad = 'Resfrio'

	# TRATAMIENTO A SEGUIR.-
	def tratamiento(self):
		self.medicamento = 'Aspirina'
		# La dosis del medicamento es la estatura dividida el peso del paciente.
		self.dosis	= float(self.peso)/float(self.estatura)
		self.dosis     	= round(self.dosis)
		print('Tome',self.dosis,'[mg] de', self.medicamento,'.') 

	# CATEGORÍA MÉDICA EN LA QUE QUEDA EL PACIENTE.-
	def categoria(self):
		self.categoria = '3'
		self.dias      = '4'	
		print(self.categoria,'por',self.dias,'días')



# CLASE JAQUECA.-
# ==============
class Jaqueca:
	"""Clase cuando el paciente se encuentra con jaqueca"""
	
	# DATOS DEL PACIENTE.-
	def __init__(self, nombre, edad, estatura, peso, sexo):
		self.nombre   = nombre
		self.edad     = edad
		self.estatura = estatura
		self.peso     = peso
		self.sexo     = sexo	
		self.enfermedad = 'Jaqueca'

	# TRATAMIENTO A SEGUIR.-
	def tratamiento(self):
		self.medicamento = 'Tapsin'  
		# La dosis del medicamento es la estatura dividida el peso del paciente.
		self.dosis	 = float(self.peso)/float(self.estatura)
		self.dosis       = round(self.dosis)
		print('Tome',self.dosis,'[mg] de', self.medicamento) 

	# CATEGORÍA MÉDICA EN LA QUE QUEDA EL PACIENTE.-
	def categoria(self):
		self.categoria = '3'
		self.dias      = '1'	
		print(self.categoria, 'por', self.dias, 'días')



# CLASE GASTROENTERITIS.-
# ======================
class Gastroenteritis:
	"""Clase cuando el paciente se encuentra con gastroenteritis"""
	
	# DATOS DEL PACIENTE.-
	def __init__(self, nombre, edad, estatura, peso, sexo):
		self.nombre   = nombre
		self.edad     = edad
		self.estatura = estatura
		self.peso     = peso
		self.sexo     = sexo
		self.enfermedad = 'Gastroenteritis'

	# TRATAMIENTO A SEGUIR.-
	def tratamiento(self):
		self.medicamento = 'Diaren'  
		# La dosis del medicamento es la estatura dividida el peso del paciente.
		self.dosis   = float(self.peso)/float(self.estatura)
		self.dosis   = round(self.dosis)
		print('Tome',self.dosis,'[mg] de',self.medicamento) 

	# CATEGORÍA MÉDICA EN LA QUE QUEDA EL PACIENTE.-
	def categoria(self):
		self.categoria = '1'
		self.dias      = 'Indefinido'
		print(self.categoria,'por',self.dias,'días')

