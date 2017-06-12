
# El módulo "Enfermedades" contiene las clases con las posibles enfermedades y su tratamiento.
import Enfermedades as enf


print('\nHola, soy I-Doc!\n')


# Datos para crear el objeto paciente.-
# ====================================
edad 	= input('¿Cúantos años tienes?\t: ')
estatura= input('¿Cúanto mides [mts]?\t: ')
peso 	= input('¿Cúanto pesas [kg]?\t: ')
sexo	= input('¿Cúal es tu sexo [M/F]?\t: ')



# Recopilación de los síntomas.-
# =============================
print('\nPor favor lee los siguientes síntomas y dime cuales son los tuyos, para ello ingresa un número y luego presiona la tecla "enter", realiza esto cuantas veces sea necesario. Cuando hayas terminado ingresa "0":\n')

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
		print('Este número no es válido, por favor ingresa otro.')



# ASOCIACIÓN DE LOS SÍNTOMAS A LAS ENFERMEDADES INGRESADAS.-
# =========================================================


# Contadores de las enfermedades:
resfrio 	= 0
jaqueca 	= 0
gastroenteritis = 0


for i in sintomas_paciente:
	# Este "for" recorre los síntomas para asociarlos a alguna enfermedad, agregando un contador a cada enfermedad, dependiendo de si el sintoma corresponde o no a ella.
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

# ===========================================================================
# PARA PRUEBA, DESPUES BORRAR ESTO
print('resfrio 		=', resfrio)
print('jaqueca 		=', jaqueca)
print('gastroenteritis 	=', gastroenteritis)
# ===========================================================================


# RELACION CONTADOR ENFERMEDAD CON CANTIDAD DE SINTOMAS.-
# ======================================================

# Al conocer cual es la enfermedad que tiene el mayor contador, se crea el el objeto "paciente" con ella.

if resfrio > jaqueca and resfrio > gastroenteritis:
	# Caso cuando el paciente se encuentra resfriado.
	paciente = enf.Resfrio(edad,estatura,peso,sexo)
	paciente.tratamiento()
# ===========================================================================
# BORRAR ESTE Y LOS SIGUIENTES "print", ESTÁN PARA VERIFICAR QUE LA CLASE SE INICIE DE MANERA CORRECTA.
	print('Paciente de la clase Resfrio')
# ===========================================================================

elif jaqueca > resfrio and jaqueca > gastroenteritis:
	# Caso cuando el paciente se encuentra con jaqueca.
	paciente = enf.Jaqueca(edad,estatura,peso,sexo)
	paciente.tratamiento()
	print('Paciente de la clase Jaqueca')

elif gastroenteritis > resfrio and gastroenteritis > jaqueca:
	# Caso cuando el paciente se encuentra con gastroenteritis.
	paciente = enf.Gastroenteritis(edad,estatura,peso,sexo) 
	paciente.tratamiento()
	print('Paciente de la clase Gastroenteritis')

else:
	# Caso cuando el paciente se encuentra con múltiples síntomas y no se pudo determinar con certeza a qué enfermeda específica corresponde.
	print('\nSu enfermedad parece grave, por favor diríjase a Urgencias.\n')

