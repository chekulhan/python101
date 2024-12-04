import nomina

if __name__ == "__main__":
    print("Bievenidos al sistema de nominas")
    


    jon = nomina.Empleado("Jon", "Smith", 1000)
    maria = nomina.Programador("Maria", "Smith", 1000, "Python")
    empleados = [jon, maria]
    sistema = nomina.Sistema_de_Nominas(empleados)
    print(sistema)

    sistema.calcular_nominas()
    
