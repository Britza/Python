
#7.1

tupla =(1,2,3,4,5,6,7)
def orden (t):
    ordeados = True
    if len (t) > 1:
        for i in range(0,len(t)-2):
            if t[i]>t[i+1]:
                ordeados = False
                break

    return ordeados

print(orden(tupla))



#7.2.1

f1=(2,4)
f2=(2,3)


def encajar(f1,f2):


    if set(f1) & set(f2):
        return "Las fichas encajan"
    else:
        return "Las fichas no encajan"

print(encajar(f1,f2))

#7.2.2

l3 = "3-4"
l4 = "2-3"


def encaja2(ls1, ls2):
    lista1 = ls1.split('-')
    lista2 = ls2.split('-')

    if set(lista1) & set(lista2):
        return "Las fichas encajan"
    else:
        return "Las fichas no encajan"

print(encaja2(l3, l4))


#7.3.1

nomes = ("patricia","britza","héctor","brais","joel")

def estimar(nomes):

    for n in nomes:
        print("Estimado/a " + n)

estimar(nomes)


#7.3.2



#8.2.1

def vecesQueAparecenAsPalabras(frase):
    diccionario = dict()
    palabras = frase.split()
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra]= diccionario[palabra]+1
        else:
            diccionario[palabra]=1

    return diccionario

vecesQueAparecenAsPalabras("que bonito dia fai hoxe, pese a que chove")

"""
def vecesQueAparecenAsPalabras(frase):
    diccionario = dict()
    palabras = frase.split()
    for palabra in palabras:
        if palabra.lower() in diccionario:
            diccionario[palabra.lower()]= diccionario[palabra.lower()]+1
        else:
            diccionario[palabra.lower()]=1

    return diccionario

vecesQueAparecenAsPalabras("que bonito dia fai hoxe, pese a que chove")"""


#8.4

def cadeaLongaPorCaracteresEnTexto(texto):

    d=dict()
    for i in range (len(texto)):
        if texto[i] in d:
            diccionario[texto[i]]


