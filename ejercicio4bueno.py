class artefacto:
    def _init_(self,nombre,peso,precio,fechacad):
        self.peso=peso
        self.nombre=nombre
        self.precio=precio
        self.fechacad=fechacad
        print ("el artefacto se ha creado con exito")
    def _str_(self):
        return f'Se ha creado el artefacto {self.nombre}, con peso {self.peso}, que cuesta {self.precio} euros y caduca el {self.fechacad}'