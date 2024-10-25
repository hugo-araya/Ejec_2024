class Persona:
    def __init__(self, nom, ape):
        self.nombre = nom
        self.ape = ape

    def __str__(self):
        return "Juanito"

    def imprimir(self):
        print ('Nombre:', self.nombre)

if __name__ == '__main__':
    persona1 = Persona("Hugo", "Araya")
    persona1.imprimir()
    persona2 = Persona("Mago", "Valdivia")
    persona2.imprimir()
    p = Persona("No se", "Yo tampoco")
    p.imprimir()
    print(persona1)
