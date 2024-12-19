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


# Ejercicio: 
# Agregar un tax rate y precio final al dataframe
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Headphones'],
    'Price': [1000, 500, 300, 150]
}


# group by
df_grouped = df.groupby('Ciudad')['Año'].agg('sum').reset_index()

df_grouped = df.groupby('Ciudad')['Año'].agg(['sum', 'mean', 'count']).reset_index()
df_grouped.head()



# Respuestas
def agregar_anos(years):
  return years + 2 

df["Año"] = df["Año"].apply(agregar_anos).head()




def addTax(df, tax_rate):
  df["Tax"] = df["Price"] * (tax_rate)
  return df

def calculateFinalPrice(df):
  df["FinalPrice"] = df["Price"] + df["Tax"]
  df["FinalPrice"] = df["FinalPrice"].apply(lambda x: f"${x:,.2f}") # format to currency
  return df

df = addTax(df, .12) # apply 12 % tax
df = calculateFinalPrice(df) # calculate final price

df.pipe(addTax, .12).pipe(calculateFinalPrice).head()
