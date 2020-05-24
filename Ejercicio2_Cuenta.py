class Cuenta:

    cantidad = 0.0

    def __init__(self, cedula_titular, nombre_titular, fecha_apertura, cantidad):
        self.cedula_titular = cedula_titular
        self.nombre_titular = nombre_titular
        self.fecha_apertura = fecha_apertura
        self.cantidad = cantidad

    def __str__(self):
        return str(self.__dict__)

    def get_cedula_titular(self):
        return self._cedula_titular

    def set_cedula_titular(self, cedula_titular):
        self.cedula_titular = cedula_titular

    def get_nombre_titular(self):
        return self._nombre_titular

    def set_nombre_titular(self, nombre_titular):
        self.nombre_titular = nombre_titular

    def get_fecha_apertura(self):
        return self._fecha_apertura

    def set_fecha_apertura(self, fecha_apertura):
        self.fecha_apertura = fecha_apertura

    def get_cantidad(self):
        return self._cantidad
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.cantidad = self.cantidad + cantidad

    def retirar(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad = self.cantidad - cantidad
        else:
          print("Se retiró ", self.cantidad - (cantidad - self.cantidad))
          self.cantidad = 0.0


cuenta = Cuenta(1038099682, "Anyi Vilaró", "16/04/2020", 62500)
#cuenta.retirar(62800)
cuenta.ingresar(5000)
print(cuenta)

