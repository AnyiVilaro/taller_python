from random import randint

class Persona:
    SEXO_PERSONA = "H"
    PESO_IDEAL = 0
    SOBRE_PESO = 1

    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.dni = self.generaDNI()
        self.sexo = "H"
        self.peso = 0
        self.altura = 0

    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.dni = self.generaDNI()
        self.peso = 0
        self.altura = 0

    def __init__(self, nombre="", edad=0, sexo=SEXO_PERSONA, peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = self.generaDNI()
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_sexo(self, sexo):
        self.sexo = sexo

    def set_peso(self, peso):
        self.peso = peso

    def set_altura(self, altura):
        self.altura = altura

    def calcularIMC(self, peso, altura, sobrepeso=SOBRE_PESO, pesoideal=PESO_IDEAL):
        self.set_peso(peso)
        self.set_altura(altura)
        resultado = peso / (pow(altura,2) )

        if resultado < 20:
            return -1
        elif 20 <= resultado <= 25:
            return pesoideal
        elif resultado > 25:
            return sobrepeso

    def esMayorDeEdad(self, edad):
        if edad < 18:
            return "Es menor de edad"
        else:
            return "Es mayor de edad"

    def comprobarSexo(self, sexo):
        if sexo == self.sexo:
            return "Es correcto"
        else:
            return self.set_sexo("H")

    def generaDNI(self):
        dni = randint(10000000, 19999999)
        return dni

    def toString(self):
        return """\
                Nombre: {}
                Edad: {}
                Sexo: {}
                DNI: {}
                Peso: {} kg
                Altura: {} m""".format(self.nombre, self.edad, self.sexo, self.dni, self.peso, self.altura)

persona = Persona("Anyi Vilaró", "32", "M")
print(persona.toString())

if (persona.calcularIMC(60,1.65) == 1 ):
    print("Tiene sobre peso")
    print(persona.toString())

if (persona.calcularIMC(65,1.65) == 0 ):
    print("Tiene peso ideal")
    print(persona.toString())

print("Comprobar sexo: ",persona.comprobarSexo("M"))