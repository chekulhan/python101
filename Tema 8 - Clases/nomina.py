class Sistema_de_Nominas:
    def __init__(self, empleados):
        self.empleados = empleados

    def __str__(self):
        return "Sistema de Nominas para Nazaret"
    
    def calcular_nominas(self):
        print('Calculando nominas')
        print("==================")
        total = 0.
        for empleado in self.empleados:
            print(f"Nomina para : {empleado.nombre} - {empleado.apellido}")
            nomina = round(empleado.calcular_nomina(), 2)
            print(f"- $ : {nomina}")
            print('')
            total += nomina
        print(f"Total a pagar: {total} ")

class Empleado:
    def __init__(self, nombre, apellido, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo = sueldo
    
    def calcular_nomina(self):
        return self.sueldo

class Programador(Empleado):
    def __init__(self, nombre, apellido, sueldo, lenguaje):
        super().__init__(nombre, apellido, sueldo)
        self.lenguaje = lenguaje

    def calcular_nomina(self) -> float:
        nomina = self.sueldo * 1.05
        return nomina 
