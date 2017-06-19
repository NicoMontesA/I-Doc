#===========================APLICACION: I-Doc======================

Esta es una interfaz m�dica que permite clasificar s�ntomas en una enfermedad com�n y sugiere un tratamiento b�sico, adem�s de entregar una receta y una licencia m�dica recomendada.

I.- REQUISITOS.

El sistema desarrollado esta dise�ado para Python 3, adem�s se requieren de las siguientes bibliotecas:

PyQt5 : Biblioteca gr�fica que permite la creaci�n de las ventanas, para la interacci�n m�quina-usuario
Reportlab: Biblioteca que genera el PDF, de acuerdo a los datos ingresados por el paciente y a la enfermedad detectada.

II.- MODULOS.

Enfermedades: Define las clases de las enfermedades Jaqueca, Resfr�o y Gastroenteritis, con sus respectivas funciones y atributos.

Creaci�nReceta: Contiene la funci�n generadora de la receta, tomando los datos de las clases Enfermedades. Entrega un archivo PDF con el nombre Receta + nombre del usuario.pdf 

I-Doc: Aplicaci�n que utiliza los m�dulos de Enfermedades y CreacionReceta.

Motor_Procesamiento: Permite la operaci�n de la aplicaci�n desde el terminal sin la biblioteca de PyQt5 y Reportlab.

III.- INSTALACION DE BIBLIOTECAS.

pip3 install reportlab

pip3 install PyQt5 

IV.- COMO USARLO.

1) Se debe ejecutar desde el terminal el modulo I-Doc.py.

2) El sistema abrir� una ventana solicitando al usuario que ingrese su nombre, edad, peso, estatura y sexo.

3) Se abrir� una nueva ventana en donde el usuario debe ingresar el n�mero que identifica a los s�ntomas que posee.

4) El programa determinar� que enfermedad com�n tiene y generar� un PDF en la carpeta del m�dulo con el diagn�stico, tratamiento a seguir y categor�a m�dica recomendada, la cual adem�s contendr� los datos personales ingresados por el usuario y la fecha de creaci�n del archivo.




