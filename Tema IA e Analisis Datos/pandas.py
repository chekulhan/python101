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


---------------------------

import numpy as np

data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', np.nan, 'Chicago'],
    [None, 40, 'Houston'],
    ['David', 35, None],
    ['David', 35, None]
]

# Column names specified separately
columns = ['Nombre', 'Edad', 'Ciudad']

# Creating the DataFrame
df = pd.DataFrame(data, columns=columns)

df.describe()
df.shape

df_sorted.drop(columns=["Estado"])

df.isnull()
df.Edad.isnull()

# fillna
mean_age = df['Edad'].mean()
df_filled_mean = df['Edad'].fillna(mean_age)

df.drop_duplicates()

df_cleaned = df.dropna(subset=['Edad'])

df_sorted = df.sort_values(by='Edad')

df_sorted["Estado"] = "Activo"
df_sorted['Status'] = df_sorted['Edad'].apply(lambda x: 'Activo' if x > 30 else None)



