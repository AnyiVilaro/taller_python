class Contador:

    def __init__(self, contador=0):
        self.contador = contador

    def constructor_copia(self, contador=0):
        self.contador = contador

    def __str__(self):
        return self.contador

    def set_contador(self, contador):
        self.contador = contador

    def get_contador(self):
        return self.contador

    def disminuir(self, disminucion):
        valor_contador = self.get_contador()
        total_contador = valor_contador - disminucion
        self.set_contador(total_contador)
        return total_contador

    def incrementar(self, aumento):
        valor_contador = self.get_contador()
        total_contador = valor_contador + aumento
        self.set_contador(total_contador)
        return total_contador

contador = 23
refcontador = Contador(contador)
print("Contador: ", contador)
print("Disminuir: ",refcontador.disminuir(5))
print("Contador: ", refcontador.get_contador())
print("Incrementar: ",refcontador.incrementar(5))

