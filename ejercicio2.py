class stormtrooper:

    def _init_(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
    
    def _str_(self):
        return "El stormtrooper {} se ha creado con exito" . format(self.nombre)
    
class calificacion(stormtrooper):
    def _init_(self,nombre , rango, codigo, cohoerte, siglo, escuadra, numero):
        self.nombre = nombre
        self.rango = rango
        self.codigo = codigo
        self.cohoerte = cohoerte
        self.siglo = siglo
        self.escuadra = escuadra
        self.numero = numero

def _str_(self):
        return "El solado {} de rango {}: {} - {}{}{}{}" . format(self.nombre, self.rango, self.codigo, self.cohoerte, self.siglo, self.escuadra, self.numero)

soldado1 = calificacion("T", "Sargento", "GP", "4", "3", "9", "3")
soldado2 = calificacion("John", "Capitan", "CV", "4", "3", "9", "3")
soldado3 = calificacion("Andrew", "Solado raso", "JK", "3", "9", "4", "5")

lista = [soldado1, soldado2, soldado3]

print(soldado1)
print(soldado2)
print(soldado3)