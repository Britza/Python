
print("Comentarios")

# Comentarios dunha liña
# O seu uso é para comentar instrucción ou partes de código do programa

""" Comentarios multiliña 
utilizanse para documentar o código """

''' Podemos xerar manuais de uso para programadores do noso código
O estilo de "JavaDoc" '''


print("Tipos basicos")

numero = 5
comaFlotante = 24.42
complexos = 7+2j
enterolongo = 2e-100 #2 * 10²

print(type(complexos))
print(type(comaFlotante))
print(type(numero))
print(type(enterolongo))

# O tipo das cadeas e 'str'
print(str (complexos))



cadea = 'Esta é unha "cadea"'
cadea2 = "Esta é 'outra'"

print(cadea +" "+cadea2)

booleanos = True
print(type(booleanos))

# Operadores
# +- -Negación * ** / // %
numero = 2**15 #2¹⁵
print(type(numero))

div = 5.5/2
print(div)

divEnteira = 5.5//2
print(divEnteira)

modulo = 5.5%2
print(modulo)

# Operacións a nivel de bits &|^~ << >>

resultado = 3 & 2
resultado2 = 3|2
resultado3 = 3^2
resultado4 = ~-127
resultado5= 126>>1
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)

# Operacións con cadeas

cadea1 = "ola"
cadea2 = "adeus"
cadea = cadea1 + cadea2
cadea = cadea1 * 3
print(cadea)

# Operación lóxicas and or not

print(True or False)
print(True and False)
print((not True))

# Listas

l = [1,2,3,4,5,6,7,8,9,10,112,113]

l2 = [1,"Dous", 3+4j,2,34,[1,2,3]]

print(l[2])
print(l2[1])
print(l[-2])
print(l2[-1][2])
print(l2[1][1])
print(l2[2])

l [2] =15.9999

print(l)


print(l[1:4])
print(l[1:-1:3])
print(l[1::2])
print(l[:6])

l[2:5] = ["tres", "cuatro", "cinco"]
print(l)
l[2:5] = ["cero"]
print(l)

l3 = list()
l4 = []
l4.append(0)
l3.append(1)


t = (1,2,"tres",[4,5,2+4j])
print(t)
t2 = 2,
print(t2)
print(t[3])
t[3][1] = 9
print(t)

for elemento in t:
    print(elemento)

    l.append("113")
print(l)
print(l.count(113))

# Diccionarios

d = {1: "un",
     2: "dous",
     3: "tres",
     "manuel": "3413526425616"}

print(d[1])
print(d["Manuel"])
d["manuel"] = "23514515"
print(d["manuel"])

print(d.items())
print(d.keys())
print(d.values())
print(d.get("manuel", "clave non encontrada"))

def saudar(lingua):

    def saudar_es():
        print("Hola")

    def saudar_gl():
        print("ola")

    def saudar_en():
        print("Hi")

    def saudar_fr():
        print("salut")


    funcion_saudar = {
        "es": saudar_es(),
        "en": saudar_en(),
        "fr": saudar_fr(),
        "gl": saudar_gl()

    }

    return funcion_saudar[lingua]


    f = saudar("gl")
    f()

    saudar("fr")()

    #Funciones  Lambda

    def suma(x, y):

        return x + y

    s = lambda x, y:x + y

    print( suma(3, 2))
    print(s(3,2))

    def funcion2(x,y,z=1):
        return(x + y) *z
    z= lambda x,y,z=1 : (x+y)*z
    print(z(5,6,2))

    l= [1,4,5,3,2,8]
    c = ['a','b']

    def cadrado (n):
        return n**2

    l2 = map (lambda n: n**2, l)
    l3 = map(cadrado, l)
    for n in l2:
        print(n)


    #Compresión de listas

    l2 = [n**2 for n in l]
    l3 = [n for n in l if n % 2.0 == 0]

    print(l3)

    l4 = [s*v for s in c
              for v in l
              if v > 0]

    print(l4)

    #Xeradores

    l5 = (n**2 for n in l)
    print(l5)

    def meuXerador(n,m,s):

        while(n<=m):
            yield n
            n += s

    xerador = meuXerador(7,15,2)
    print(xerador)

    for n in xerador:
        print(n)

    # for (int i = 7, n<m, i+=s)

    for i in range(7,15,2):
        print(i)

    r = range(7,16,2)
    print(type(r))

    #Cadeas de caracteres

    cadea = "Python para todos"

    print(cadea[1:18:2])

    pritn(cadea.count('o'))
    print(len(cadea))
    print(cadea.find('o',5,14))

    cadea2 = cadea.join('ola','a','todos','no','presente','curso')
    print(cadea2)

    print(cadea.partition(''))
    print(cadea.split(''))
    print(cadea.replace('','_'))
    print(cadea.upper())


    def unha_funcion(parametro1,parametro2):
        print(parametro1)
        print(parametro2)

    unha_funcion("hola", 2.456)
    """unha_funcion(parametro2= 2.456, parametro1="ola")"""

    def unha_funcion(parametro1="hi", parametro2=3.00):
        print(parametro1)
        print(parametro2)

    unha_funcion(parametro1="salut")

    def suma (n1,n2,n3, *numeros):

        suma= n1+n2+n3
        for n in numeros:
            suma=suma + n

        return suma

    print(suma(2,2,2,4,5,5))

    def suma2(n1,n2,**numeros):

        suma = n1 + n2
        for n in numeros.items():
            print(n)
            suma = suma + n[1]
        return suma2

    print(suma2(2,2, numero3 = 3, numero4= 4))