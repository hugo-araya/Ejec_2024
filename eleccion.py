
ent = open('elecciones.txt')
linea1 = ent.readline().rstrip('\n')
linea2 = ent.readline().rstrip('\n')
print(linea1)
print(linea2)
coaliciones = linea1.split(';')
coalicion = []
for coal in coaliciones:
    coalicion.append(coal.split(":"))
partidos = []
for coal in coalicion:
    part = coal[1].split('-')
    for p in part:
        partidos.append([p, 0])
votos = linea2.split('$')
for voto in votos:
    for elem in partidos:
       if voto == elem[0]:
            elem[1] = elem[1] + 1

print('Votos por partido')
for partido in partidos:
    print(partido[0]+' : '+str(partido[1]))

# print(coaliciones)
# print(coalicion)
# print(partidos)
# print(votos)


