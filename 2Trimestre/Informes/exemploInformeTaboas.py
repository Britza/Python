from reportlab.platypus import SimpleDocTemplate, Spacer,PageBreak, Table,TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import sqlite3 as dbapi

doc = SimpleDocTemplate("exemploTaboas.pdf", pagesize=A4)

guion = []

taboa = Table([['', 'Ventas', 'Compras'],
              ['Xaneiro', 123, 456],
              ['Febreiro', 2500, 2555],
              ['Marzo', 1400, 990]],
              colWidths=80, rowHeights=30)
taboa.setStyle([('TEXTCOLOR', (0, 1), (0, -1), colors.blue),
                ('TEXTCOLOR', (1, 1), (2, -1), colors.green),
                ('BACKGROUND', (1, 1), (-1, -1), colors.beige),
                ('BOX', (1, 1), (-1, -1), 1.25, colors.yellowgreen),
                ('INNERGRID', (1, 1), (-1, -1), 1, colors.orangered),
                ('VALING', (0, 0), (-1, -1), 'MIDDLE')])

guion.append(taboa)
guion.append(Spacer(0, 15))

p = Paragraph("Este é un texto dun parragrafo\nCon varias liñas")
i = Image('/home/dam2a/Documentos/cmamo.png')

datos = [['Arriba\nEsquerda', '', '02', '03', '04'],
         ['', 'Outro dato', '12', p, '14'],
         ['', '', '02', '03', '04'],
         ['20', '21', '22', 'Abaixo\nDereita'],
         ['30', '31', '32', '', '']]
estilo = [('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
          ('BACKGROUND', (0, 0), (-1, -1), colors.palegreen),
          ('SPAN', (0, 0), (1, 1)),
          ('BACKGROUND', (2, -2), (-1, -1), colors.pink),
          ('SPAN', (-2, -2), (-1, -1))]

taboa2 = Table(data=datos, style=estilo)

guion.append(taboa2)

try:
    bbdd = dbapi.connect("baseDatos.dat")
    cursor = bbdd.cursor()

    usuarios = []
    usuarios.append(("Nome", "DNI", "Dirección"))
    cursor.execute("""SELECT * FROM usuarios""")
    for rexistro in cursor.fetchall():
        usuarios.append((rexistro[1], rexistro[0], rexistro[2]))

except dbapi.DatabaseError as e:
    print("Erro na base de datos: " + str(e))

    taboaUsuarios = Table(usuarios)


doc.build(guion)




