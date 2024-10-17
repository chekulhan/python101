lenguajes = ["Python", "Javascript", "Java", "React", "Swift"]

# crear una lista con 
# - lenguajes una longitud de lenguages de 5 o menos 
lista_nueva = [l for l in lenguajes if len(l)<=5]

x = filter(lambda x: len(x)<=5, lenguajes)
print(list(x))
print(lista_nueva)

usuarios = [{"nombre": "Jon", "edad": 25},
            {"nombre": "Isabel", "edad": 65},
            {"nombre": "David", "edad": 41}
            ]
# crear una lista de diccionarios con 
# - usuarios de > 40

users = filter(lambda x: x["edad"]>=40, usuarios)
#[{'nombre': 'Isabel', 'edad': 65}, {'nombre': 'David', 'edad': 41}]
print(list(users))

ventas = [['2021-05-31', 1500],
          ['2021-04-31', 1200],
          ['2021-03-31', 800],
          ['2021-02-28', 8000],
            ]
# entre 1000 y 2000

v = filter(lambda x:x[1]>1000 and x[1]<2000, ventas)
print(list(v))
