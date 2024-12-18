import pandas as pd

datos = {
    'Nombre': ['Juan', 'Isabel', 'José', 'David'],
    'Edad': [25, 30, 35, 40],
    'City': ['Nueva York', 'Los Angeles', 'San Sebastián', 'Madrid']
}

df = pd.DataFrame(datos)

# acceder
df[["Edad", "Nombre"]]
df.Nombre

# acceder, filtrar, modificar
df.loc[2]
df.loc[2, "Nombre"]
df.loc[1:2, ["Nombre", "Edad"]]  # rows, cols
df.loc[1:3]
df.loc[:, ["Edad"]] # todos

df.loc[df["Edad"]> 26]
df.loc[(df["Edad"]> 26) & (df["Edad"]< 36)]  # fijate en los ()

# index loc
df.iloc[:, 2]
df.iloc[:, 1:3]
df.iloc[-1, 1:3]

# extraer valores
lista = df.loc[:, "Edad"].to_list()

# query como SQL
df.query('Age > 30')
