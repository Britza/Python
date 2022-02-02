import os.path
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

elementos = []

follaEstilo = getSampleStyleSheet()

cabeceira = follaEstilo['Heading4']
cabeceira.pageBreakBefore = 0
cabeceira.keepWithNext = 0
cabeceira.backColor = colors.cornsilk

parragrafo = Paragraph("CABECEIRA DO DOCUMENTO", cabeceira)
elementos.append(parragrafo)

cadea = "Exemplo de utilización de ReportLab con Platypus. " * 500
corpo = follaEstilo['BodyText']
parragrafo2 = Paragraph(cadea, corpo)
elementos.append(parragrafo2)
elementos.append(Spacer(0, 20))

grafica = Image(os.path.relpath("/home/dam2a/Documentos/totoro.jpeg"), width=500, height=150)
elementos.append(grafica)

doc = SimpleDocTemplate("exemploPlatypus.pdf", pagesize=A4, showBoudary=0, allowSplitting=1, title="Frases con Platypus", author="Britza")
doc.build(elementos)


