#===========================APLICACION: I-Doc======================

Esta es una interfaz médica que permite clasificar sí­ntomas en una enfermedad común y sugiere un tratamiento básico, además de entregar una receta y una licencia médica recomendada.

I.- REQUISITOS.

El sistema desarrollado esta diseñado para Python 3, además se requieren de las siguientes bibliotecas:

PyQt5 : Biblioteca gráfica que permite la creación de las ventanas, para la interacción máquina-usuario
Reportlab: Biblioteca que genera el PDF, de acuerdo a los datos ingresados por el paciente y a la enfermedad detectada.

II.- MODULOS.

Enfermedades: Define las clases de las enfermedades Jaqueca, Resfrío y Gastroenteritis, con sus respectivas funciones y atributos.

CreaciónReceta: Contiene la función generadora de la receta, tomando los datos de las clases Enfermedades. Entrega un archivo PDF con el nombre Receta + nombre del usuario.pdf 

I-Doc: Aplicación que utiliza los módulos de Enfermedades y CreacionReceta.

Motor_Procesamiento: Permite la operación de la aplicación desde el terminal sin la biblioteca de PyQt5 y Reportlab.

III.- INSTALACION DE BIBLIOTECAS.

pip3 install reportlab

pip3 install PyQt5 

IV.- COMO USARLO.

1) Se debe ejecutar desde el terminal el modulo I-Doc.py.

2) El sistema abrirá una ventana solicitando al usuario que ingrese su nombre, edad, peso, estatura y sexo.

3) Se abrirá una nueva ventana en donde el usuario debe ingresar el número que identifica a los síntomas que posee.

4) El programa determinará que enfermedad común tiene y generará un PDF en la carpeta del módulo con el diagnóstico, tratamiento a seguir y categoría médica recomendada, la cual además contendrá los datos personales ingresados por el usuario y la fecha de creación del archivo.




