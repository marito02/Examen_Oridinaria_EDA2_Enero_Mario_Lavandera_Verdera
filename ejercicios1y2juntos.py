class stormtrooper():

    def _init_(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango 
        print (f"El stormtrooper {self.nombre} se ha creado correctamente")
    def _str_(self):
        return (f"El stormtrooper {self.nombre} con rango {self.rango}")
    def calificacion(self):
        def _init_(self,nombre , rango, codigo, cohoerte, siglo, escuadra, numero):
            self.nombre = nombre
            self.rango = rango
            self.codigo = codigo
            self.cohoerte = cohoerte
            self.siglo = siglo
            self.escuadra = escuadra
            self.numero = numero
        def __str__(self):
            return (f"el soldado {self.nombre} con rango {self.rango} y con codigo {self.codigo} tiene un id de {self.cohoerte} con un siglo de {self.siglo} y una escuadra de {self.escuadra} con numero de trooper {self.trooper}")


soldado1 = stormtrooper("Alberto", "Coronel", "FN", 7, 1, 4, 6)
soldado2 = stormtrooper("Pedro", "Cabo", "KT", 5, 2, 8, 3)
soldado3 = stormtrooper("Juan", "Comandante", "QS", 4, 6, 3, 9)

lista = [soldado1, soldado2, soldado3]

print(soldado1.calificacion())
print(soldado2.calificacion())
print(soldado3.calificacion())