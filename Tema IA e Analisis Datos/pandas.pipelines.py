import pandas as pd

data = {
    'Ciudad': ['New York', 'New York', 'London', 'London'],
    'Año': [2020, 2021, 2020, 2021],
    'Populación': [8.3, 8.4, 9.3, 9.4],
}
df = pd.DataFrame(data)


# si quieres pasar más parametros, hay que usar lambda con apply
# df["Años"].apply(lambda x: agregar_prefijo(x, "PRE_")).head()

def capitalise(text):
  return text.upper()


df["Ciudad"] = df["Ciudad"].apply(capitalise)  
df.head()

# Ejercicio: Aplicar una funcion para añadir 2 años a cada año

# functions para agregar columnas y modiciar el dataframe

def addDefaultValue(df, col, value):
  df[col] = value
  return df

df = addDefaultValue(df, "newcolumn", "new value")
df.head()

def NYValue(df, col, value):
  df.loc[df[col] == "New York", col] = value
  return df

# aplicar un pipeline
df = df.pipe(NYValue, col='Ciudad', value='ABCD').pipe(addDefaultValue, col='col_name', value='default_value')

df.head()




# group by
df_grouped = df.groupby('Ciudad')['Año'].agg('sum').reset_index()

df_grouped = df.groupby('Ciudad')['Año'].agg(['sum', 'mean', 'count']).reset_index()
df_grouped.head()



# Respuestas
def agregar_anos(years):
  return years + 2 

df["Año"] = df["Año"].apply(agregar_anos).head()
