# Este archivo contiene las clases que definen las enfermedades.


# CLASE RESFRIO.-
# ==============
class Resfrio:
	"""Clase cuando el paciente se encuentra resfriado"""
	
	# DATOS DEL PACIENTE.-
	def __init__(self, edad, estatura, peso, sexo):
		self.edad     = edad
		self.estatura = estatura
		self.peso     = peso
		self.sexo     = sexo	

	# TRATAMIENTO A SEGUIR.-
	def tratamiento(self):
		medicamento = 'Aspirina'
		# La dosis del medicamento es la estatura dividida el peso del paciente.
		dosis	    = float(self.peso)/float(self.estatura)
		dosis       = round(dosis)
		print('Tome',dosis,'[mg] de', medicamento,'.') 

	# CATEGORÍA MÉDICA EN LA QUE QUEDA EL PACIENTE.-
	def categoria(self):
		self.categoria = 3
		self.dias      = 4	



# CLASE JAQUECA.-
# ==============
class Jaqueca:
	"""Clase cuando el paciente se encuentra con jaqueca"""
	
	# DATOS DEL PACIENTE.-
	def __init__(self, edad, estatura, peso, sexo):
		self.edad     = edad
		self.estatura = estatura
		self.peso     = peso
		self.sexo     = sexo	

	# TRATAMIENTO A SEGUIR.-
	def tratamiento(self):
		medicamento = 'Tapsin'  
		# La dosis del medicamento es la estatura dividida el peso del paciente.
		dosis	    = float(self.peso)/float(self.estatura)
		dosis       = round(dosis)
		print('Tome',dosis,'[mg] de', medicamento,'.') 

	# CATEGORÍA MÉDICA EN LA QUE QUEDA EL PACIENTE.-
	def categoria(self):
		self.categoria = 3
		self.dias      = 1	





# CLASE GASTROENTERITIS.-
# ======================
class Gastroenteritis:
	"""Clase cuando el paciente se encuentra con gastroenteritis"""
	
	# DATOS DEL PACIENTE.-
	def __init__(self, edad, estatura, peso, sexo):
		self.edad     = edad
		self.estatura = estatura
		self.peso     = peso
		self.sexo     = sexo	

	# TRATAMIENTO A SEGUIR.-
	def tratamiento(self):
		medicamento = 'Diaren'  
		# La dosis del medicamento es la estatura dividida el peso del paciente.
		dosis	    = float(self.peso)/float(self.estatura)
		dosis       = round(dosis)
		print('Tome',dosis,'[mg] de', medicamento,'.') 

	# CATEGORÍA MÉDICA EN LA QUE QUEDA EL PACIENTE.-
	def categoria(self):
		self.categoria = 1


