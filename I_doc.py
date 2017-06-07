
class Paciente:
	"""Crea la clase paciente con sus atributos"""
	
	def __init__(self, edad, estatura, peso, sexo):
		self.edad = edad
		self.estatura = estatura
		self.peso = peso
		self.sexo = sexo


print('\nHola, soy I-Doc!\n')

# Datos para crear el objeto paciente.-
# ====================================
edad 	= input('¿Cúantos años tienes?\t: ')
estatura= input('¿Cúanto mides [mts]?\t: ')
peso 	= input('¿Cúanto pesas [kg]?\t: ')
sexo	= input('¿Cúal es tu sexo [M/F]?\t: ')


# Objeto perteneciente a la clase "Paciente".-
# ===========================================
paciente1 = Paciente(edad, estatura, peso, sexo)


# Recopilación de los síntomas.-
# =============================
print('\nPor favor lee los siguientes síntomas y dime cuales son los tuyos, cuando hayas terminado ingresa "0":\n')

print("""
1.Dolor de cabeza.\n2.Mucosa.\n3.Dolor de estómago.\n4.Tos.\n5.Indigestión.\n6.Decaimiento.\n7.Frio.\n""")



# El siguente "while" llena la lista "sintomas_paciente" con la información recopilada.-
a = True
sintomas_paciente = []

while a == True:
	nuevo_sintoma = input()
	
	if nuevo_sintoma == '0':
		# Caso cuando se da término al ingreso de datos.
		a = False
	elif nuevo_sintoma == '1':
		# Este y los siguientes "elif" llenan la lista según el numero ingresado por el paciente.
		sintomas_paciente.append('Dolor de cabeza')
	elif nuevo_sintoma == '2':
		sintomas_paciente.append('Mucosa')
	elif nuevo_sintoma == '3':
		sintomas_paciente.append('Dolor de estómago')
	elif nuevo_sintoma == '4':
		sintomas_paciente.append('Tos')
	elif nuevo_sintoma == '5':
		sintomas_paciente.append('Indigestión')
	elif nuevo_sintoma == '6':
		sintomas_paciente.append('Decaimiento')
	elif nuevo_sintoma == '7':
		sintomas_paciente.append('Frio')
	else:
		print('Este número no es válido, por favor ingresa otro')



# ASOCIACIÓN DE LOS SÍNTOMAS A LAS ENFERMEDADES INGRESADAS.-
# =========================================================

resfrio 	= 0
jaqueca 	= 0
gastroenteritis = 0

for i in sintomas_paciente:
	
	if i == 'Dolor de cabeza':
		resfrio += 1
		jaqueca += 1

	elif i == 'Mucosa':
		resfrio += 1
		jaqueca += 1

	elif i == 'Dolor de estómago':
		gastroenteritis += 1

	elif i == 'Tos':
		resfrio += 1

	elif i == 'Indigestión':
		gastroenteritis += 1

	elif i == 'Decaimiento':
		resfrio += 1

	elif i == 'Frio':
		resfrio += 1



# RELACION CONTADOR ENFERMEDAD CON CANTIDAD DE SINTOMAS.-
# ======================================================

# Se establecio la relacion N/2+1 para determinar si se tiene la enfermedad o no, donde N representa la cantidad total de síntomas.

  
