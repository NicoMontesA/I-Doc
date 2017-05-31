
class paciente:
	"""Crea la clase paciente con sus atributos"""
	
	def __init__(self, edad, estatura, peso, sexo):
		self.edad = edad
		self.estatura = estatura
		self.peso = peso
		self.sexo = sexo


print('\nHola, soy I-Doc!\n')

edad 	= input('¿Cúantos años tienes?\t: ')
estatura= input('¿Cúanto mides [mts]?\t: ')
peso 	= input('¿Cúanto pesas [kg]?\t: ')
sexo	= input('¿Cúal es tu sexo [M/F]?\t: ')

paciente1 = paciente(edad, estatura, peso, sexo)

print('\nPor favor lee los siguientes síntomas y dime cuales son los tuyos, cuando hayas terminado ingresa "0":\n')

print("""
1.Dolor de cabeza.\n2.Mucosa.\n3.Dolor de estómago.\n4.Tos.\n5.Indigestión.\n6.Decaimiento.\n7.Frio.\n""")

a = True
sintomas_paciente = []

while a == True:
	nuevo_sintoma = input()
	
	if nuevo_sintoma == '0':
		a = False
	else:
		sintomas_paciente.append(nuevo_sintoma)

	






