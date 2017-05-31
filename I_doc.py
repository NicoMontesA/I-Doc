
class paciente:
	"""Crea la clase paciente con sus atributos"""
	
	def __init__(self, edad, estatura, peso, sexo):
		self.edad = edad
		self.estatura = estatura
		self.peso = peso
		self.sexo = sexo


print('Hola, soy I-Doc!, por favor lee los siguientes síntomas y dime cuales son los tuyos\n')

print("""
1.Dolor de cabeza. \t2.Mucosa. \t3.Dolor de estómago. \t4.Tos\n

