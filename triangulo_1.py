# Autor: Yo
def captura():
    l1 = int(input('Ingrese lado 1: '))
    l2 = int(input('Ingrese lado 2: '))
    l3 = int(input('Ingrese lado 3: '))
    return l1, l2, l3

def es_triangulo(l1, l2, l3):
    if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
        salida = True
    else:
        salida = False
    return salida

def tipo_triangulo(l1, l2, l3, es):
    if es == True:
        if (l1 == l2) and (l1 == l3):
            tipo = 'Equilatero'
        else:
            if (l1 != l2) and (l1 != l3) and (l2 != l3):
                tipo = 'Escaleno'
            else:
                tipo = 'Isoceles'
    else:
        tipo = 'No es triangulo'
    return tipo

def mostrar(tipo):
    print (tipo)

if __name__ == '__main__':
    l1, l2, l3 = captura()
    es = es_triangulo(l1, l2, l3)
    tipo = tipo_triangulo(l1, l2, l3, es)
    mostrar(tipo)
