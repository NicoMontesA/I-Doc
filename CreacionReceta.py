#reportlab es la biblioteca que permite la creacion del PDF de la receta medica, de acuerdo a la enfermedad detectada

import datetime
import Enfermedades

from reportlab.lib.pagesizes import letter 
from reportlab.pdfgen import canvas
from reportlab.platypus import  Image
from reportlab.lib.colors import blue, gray, black
from reportlab.lib.units import cm


""" Generacion_Receta es la función que crea un PDF con una receta de acuerdo a la enfermedad detectada y con los datos ingresados por el paciente"""

#=======VARIABLES OBTENIDAS DESDE EL MODULO ENFERMEDADES=======

#Datos de prueba:
#self_nombre = "Carolina"
#self_edad = "27"
#self_estatura = "1.68"
#self_peso = "61"
#self_sexo = "F"

#=====NOMBRE DEL ARCHIVO PDF A CREAR Y TAMAÑO DE LA HOJA======

#self_nombre = ventana1.nombre


def Generacion_Receta(self_nombre, self_edad, self_estatura, self_peso, self_sexo,enfermedad,medicamento,dosis,categoria,dias):

    'Generacion_Receta es la función que crea un PDF con una receta de acuerdo a la enfermedad detectada y con los datos ingresados por el paciente'
    Nombre_Archivo  = "Receta" + self_nombre + ".pdf"
    c = canvas.Canvas(Nombre_Archivo,pagesize=letter)
    width, height = letter

#==========ENCABEZADO DE LA RECETA===========================

    #Ancho de linea para todo el archivo
    c.setLineWidth(0.1 * cm)

    # Tipo de letra y tamaño
    c.setFont('Helvetica-Bold',24)
    # Texto y ubicacion
    c.drawCentredString(270,760,"I-DOC")
    # Tipo de letra y tamaño
    c.setFont('Helvetica-Bold',20)
    # Color de la letra 
    c.setFillColor(black)
    # Texto
    c.drawString(100,720,"Tu Especialista en Enfermedades Comunes")
    #Lineas de separacion
    c.line(10,710,550,710)
    c.line(10,705,550,705)


#========================LOGO===============================

    c.drawImage('LogoDoc.jpg',450,610)

#==================DATOS DEL PACIENTE=======================

    # Tipo de letra y tamaño    
    c.setFont('Helvetica-Bold',16)
    # Texto y ubicacion
    c.drawString(50,680,"Nombre:")
    #Color de la letra
    c.setFillColor(gray)
    # Texto y ubicacion
    c.drawString(120,680, self_nombre)
    #Color de la letra
    c.setFillColor(black)
    # Texto y ubicacion
    c.drawString(50,660,"Edad:")
    #Color de la letra
    c.setFillColor(gray)
    # Texto
    c.drawString(100,660, self_edad + " " + "años")
    #Color de la letra
    c.setFillColor(black)
    # Texto
    c.drawString(50,640,"Estatura:")
    #Color de la letra
    c.setFillColor(gray)
    # Texto
    c.drawString(125,640, self_estatura + " " + "mts.")
    #Color de la letra
    c.setFillColor(black)
    # Texto
    c.drawString(50,620,"Peso:")
    #Color de la letra
    c.setFillColor(gray)
    # Texto
    c.drawString(100,620, self_peso + " " + "Kgs.")
    #Color de la letra
    c.setFillColor(black)
    # Texto
    c.drawString(50,600,"Sexo:")
    #Color de la letra
    c.setFillColor(gray)
    # Texto
    c.drawString(100,600,self_sexo)

    #Lineas de separacion
    c.line(10,590,550,590)
    c.line(10,585,550,585)

#================CONTENIDO DE LA RECETA=========================

    # Tipo de letra y tamaño 
    c.setFont('Helvetica-Bold',18)
    #Color de la letra
    c.setFillColor(black)
    # Texto
    c.drawString(200,560,"RECETA MÉDICA")
     #Linea subarallado
    c.line(197,555,355,555)

    # Tipo de letra y tamaño 
    c.setFont('Helvetica-Bold',16)

    # Texto
    c.drawString(50,530,"Diagnóstico:")
     #Color de la letra
    c.setFillColor(blue)
    # Texto
    c.drawString(170,530,enfermedad)
     #Color de la letra
    c.setFillColor(black)
    # Texto
    c.drawString(50,460,"Tratamiento:")
     #Color de la letra
    c.setFillColor(blue)
    # Texto
    c.drawString(170,460,'Tomar'+ ' ' + str(dosis) + ' '+ '[mg] de'+ ' '  + medicamento)
    #Color de la letra
    c.setFillColor(black)
    # Texto
    c.drawString(50,390,"Categoría Médica:")
    #Color de la letra
    c.setFillColor(blue)
    # Texto
    c.drawString(192,390,categoria + ' ' + 'por'+ ' ' + dias + ' ' + 'dias')

    #Lineas de separacion
    c.line(10,330,550,330)
    c.line(10,325,550,325)

#=============FIRMA Y FECHA======================================

    #Insertar fecha y hora de generacion de la receta
     #Color de la letra
    c.setFillColor(black)
    actual = datetime.datetime.today()
    fecha = actual.strftime("%h %d %Y %H:%M:%S")
    textobject = c.beginText()
    textobject.setTextOrigin(50,290)
    textobject.textLines('''Fecha de Emision de la Receta: %s ''' % fecha)
    c.drawText(textobject)
  
    #Firma médico Tratante
    c.drawString(50,250,"Firma Médico Tratante:")
    c.setFont('Times-BoldItalic',16)
    c.drawString(235,250,"I-Doc")

    #Lineas de separacion
    c.line(10,230,550,230)
    c.line(10,225,550,225)

# Finaliza la hoja del archivo
    c.showPage() 
#Guarda el archivo PDF generado
    c.save()          

#Generacion_Receta(self_nombre, self_edad, self_estatura, self_peso, self_sexo)
