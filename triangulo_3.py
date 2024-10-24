# Autor: Yo
def captura():
    l = []
    l1 = int(input('Ingrese lado 1: '))
    l2 = int(input('Ingrese lado 2: '))
    l3 = int(input('Ingrese lado 3: '))
    l.append(l1)
    l.append(l2)
    l.append(l3)
    return l

def es_triangulo(l):
    l1 = l[0]
    l2 = l[1]
    l3 = l[2]
    if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
        salida = True
    else:
        salida = False
    return salida

def tipo_triangulo(l):
    l1 = l[0]
    l2 = l[1]
    l3 = l[2]
    if (l1 == l2) and (l1 == l3):
        tipo = 'Equilatero'
    else:
        if (l1 != l2) and (l1 != l3) and (l2 != l3):
            tipo = 'Escaleno'
        else:
            tipo = 'Isoceles'
    return tipo

def mostrar(tipo):
    print (tipo)

if __name__ == '__main__':
    l = captura()
    es = es_triangulo(l)
    if es == True:
        tipo = tipo_triangulo(l)
    else:
        tipo = 'No es Triangulo'
    mostrar(tipo)