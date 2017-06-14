#Uso de la libreria Reportlab para la creación de PDF, de acuerdo a la
# enfermedad detectada

from reportlab.pdfgen import canvas

aux = canvas.Canvas("Receta.pdf")

aux.drawImage("d:\\python\\pdf\\Logo.I-Doc.jpg",50,200,600,600)
aux.drawString(50,200,"EJEMPLO DE INSERCION DE IMAGEN EN PDF")

aux.showPage() 
aux.save()
