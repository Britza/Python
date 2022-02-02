from reportlab.pdfgen import canvas

lenzo = canvas.Canvas("documento.pdf")
lenzo.drawString(0, 0, "Posicion inicial (x,y)=(0,0)")
lenzo.drawString(50, 100, "Posicion inicial (x,y)=(50,100)")
lenzo.drawString(200, 50, "Posicion inicial (x,y)=(200,50)")
lenzo.drawImage("/home/dam2a/Documentos/totoro.jpeg", 0, 0, preserveAspectRatio=True)

lenzo.showPage()
lenzo.save()
