class Employee:
  # constructor
  def __init__(self, name, salary):
    # public data members
    self.name = name
    self.__salary = salary

  # public instance methods
  def __str__(self):
    # accessing public data member
    print("Name: ", self.name, 'Salary:', self.__salary)

  def calcular_nomina(self):
    return self.__salary * 1.1


class Programador(Employee):

  def __init__(self, name, salary, lenguaje):
    super().__init__(name, salary)
    self.lenguaje = lenguaje

    #def calcular_nomina(self):
    #    return self.salary * 1.2

class Analista(Employee):

  def __init__(self, name, salary, dominio):
    super().__init__(name, salary)
    self.dominio = dominio

    def calcular_nomina(self):
        return self.salary * 1.2


class Sistema_Nominas:

  def calcular_nominas(self, empleados):
    print('Calculando nominas')
    print('===================')
    for empleado in empleados:
        # no es perfect, pero va de momento
        if "Analista" in str(type(empleado)):
            print(f'Nomina para : {empleado.name} - {empleado.dominio}')
        else:
            print(f'Nomina para : {empleado.name} - {empleado.lenguaje}')
       

        print(f'- $ : {empleado.calcular_nomina()}')
        print('')


empleados = []
# rellenar la lista de empleados con datos de diferentes tipos de empleados

jon = Programador("jon", 2500, "Python")
maria = Programador("maria", 2400, "Java")
pep = Analista("pepe", 5000, "Finanzas")


empleados.append(jon)
empleados.append(maria)
empleados.append(pep)


# Ejecutar el metodo para calcular los salarios
nominas = Sistema_Nominas()
nominas.calcular_nominas(empleados)
