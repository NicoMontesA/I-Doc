#Reportlab es la biblioteca que permite la creacion del PDF de la receta medica, de acuerdo a la enfermedad detectada

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

aux = canvas.Canvas("RecetaPrueba.pdf")

aux.drawString(300,800,"I-DOC")
aux.drawString(200,780,"Tu Especialista en Enfermedades Comunes")
aux.drawString(50,750,"Nombre:")
aux.drawString(50,730,"Edad:")
aux.drawString(50,710,"Estatura:")
aux.drawString(50,690,"Peso:")
aux.drawString(50,670,"Sexo:")

#drawImage(archivo, x, y, width=None, height=None)
aux.drawImage("LogoDoc.jpg",400,650,width=100, height=None)



aux.showPage()
aux.save()
