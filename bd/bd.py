import sqlite3 as dbapi

'''
print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle) #"select * from taboa1 where dni=? and cidade=?
'''

"""
Standard error
-warning
-Error
    -InterfaceError
    -Database Error
        -Datan errror
        -Operational Error
        -Integrity Error
        -Internal Error
        -Programing Error
        -Not supported Error
"""

try:
    bbdd = dbapi.connect("baseDatos.dat")
    # print(bbdd)
    cursor = bbdd.cursor()
    '''
    cursor.execute("""CREATE TABLE usuarios (dni text,
                                             nome text,
                                             direccion text)""")
    '''
    # print(cursor)
    '''
    cursor.execute("""INSERT INTO usuarios VALUES('252523K','Ana Gil', 'Rosalia')""")
    cursor.execute("""INSERT INTO usuarios VALUES('2525287G','Ana Moure', 'Garcia Barbon')""")

    bbdd.commit()
    '''
    cursor.execute("""SELECT * FROM usuarios""")
    for rexistro in cursor.fetchall():
        print("Nome: " + rexistro[1])
        print("DNI: " + rexistro[0])
        print("Direccion: " + rexistro[2])

    # SQL injection

    # dni = "2525287G' or ''='"
    dni = "2525287G' and ''='"
    '''
    cursor.execute("""SELECT * FROM usuarios WHERE dni = '""" + dni +"""'""")


    for usuario in cursor.fetchall():
        print(usuario)
    '''

    cursor.execute("""SELECT * FROM usuarios WHERE dni = ?""", (dni,))

    for usuario in cursor.fetchall():
        print(usuario)

except dbapi.DatabaseError as e:
    print("Erro na base de datos: " + str(e))

