Escenario: Eres un analista de datos en una tienda minorista y te han asignado la tarea de analizar los datos de ventas para mejorar el rendimiento de la tienda. 
Necesitas:
- Ingerir los datos desde un archivo CSV que contiene los datos de ventas de la tienda.
- Limpiar los datos, eliminando cualquier entrada inválida o faltante.
- Analizar los datos, identificando tendencias como:
 - Ventas totales por mes.
 - Productos más vendidos.
 - Rendimiento de ventas por tienda.
- Presentar los resultados de manera clara para que el equipo de gestión pueda tomar decisiones basadas en los datos.


Fecha,Tienda,Producto,Cantidad Vendida,Precio por Unidad,Ventas Totales,Columna Extra
2024-01-01,Madrid,Camiseta,5,20,100,
2024-01-01,San Sebastián,Jeans,3,40,120,
2024-01-02,Madrid,Camiseta,8,20,160,
2024-01-03,San Sebastián,Chaqueta,2,60,120,
2024-02-01,Madrid,Jeans,4,40,160,
2024-02-03,San Sebastián,Camiseta,10,20,200,
2024-02-05,Madrid,Chaqueta,1,60,60,
2024-03-01,Madrid,Camiseta,7,20,140,
2024-03-02,San Sebastián,Chaqueta,3,60,180,
2024-03-05,Madrid,Jeans,5,40,200,
2024-01-01,Madrid,Camiseta,5,20,100,
2024-02-05,Madrid,Chaqueta,1,60,60,
2024-03-03,Madrid,Camiseta,6,20,120,
2024-03-05,San Sebastián,Jeans,4,40,160,
2024-03-01,San Sebastián,Jeans,4,40,160,
2024-02-01,Madrid,Camiseta,NaN,20,NaN,
2024-02-02,Madrid,Camiseta,8,20,160,







# RESPUESTAS ------------------------ :

Pasos para el Proyecto
1. Ingesta de los Datos:
Usa Pandas para cargar los datos desde un archivo CSV.

import pandas as pd

# Cargar el conjunto de datos
df = pd.read_csv('ventas_tienda.csv')
2. Limpieza de los Datos:
Manejo de Datos Faltantes:
Asegúrate de que no haya valores faltantes en las columnas importantes como Producto, Cantidad Vendida o Ventas Totales.


# Verificar valores faltantes
df.isnull().sum()

# Eliminar filas con valores faltantes en columnas cruciales
df = df.dropna(subset=['Producto', 'Cantidad Vendida', 'Ventas Totales'])
Corregir Tipos de Datos:
Asegúrate de que las columnas numéricas estén en el tipo de dato adecuado.


# Convertir 'Cantidad Vendida' y 'Ventas Totales' a numérico
df['Cantidad Vendida'] = pd.to_numeric(df['Cantidad Vendida'], errors='coerce')
df['Ventas Totales'] = pd.to_numeric(df['Ventas Totales'], errors='coerce')
Manejo de Valores Atípicos:
Para simplificar, filtra los valores atípicos en las columnas de Cantidad Vendida y Ventas Totales.


# Eliminar filas donde 'Cantidad Vendida' o 'Ventas Totales' sean negativos o excesivamente grandes
df = df[df['Cantidad Vendida'] > 0]
df = df[df['Ventas Totales'] > 0]
3. Análisis de los Datos:
a. Ventas Totales por Mes:

# Convertir la columna 'Fecha' a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Agregar una columna 'Mes'
df['Mes'] = df['Fecha'].dt.to_period('M')

# Calcular las ventas totales por mes
ventas_por_mes = df.groupby('Mes')['Ventas Totales'].sum().reset_index()
print(ventas_por_mes)
b. Productos Más Vendidos:


# Calcular la cantidad total vendida por producto
productos_mas_vendidos = df.groupby('Producto')['Cantidad Vendida'].sum().sort_values(ascending=False).reset_index()
print(productos_mas_vendidos)
c. Ventas por Tienda:


# Calcular las ventas totales por tienda
ventas_por_tienda = df.groupby('Tienda')['Ventas Totales'].sum().reset_index()
print(ventas_por_tienda)
4. Presentación de los Resultados:
Presenta los resultados en un formato legible, como imprimiendo los resultados o utilizando gráficos.

python

import matplotlib.pyplot as plt

# Gráfico de Ventas Totales por Mes
plt.figure(figsize=(10, 6))
plt.bar(ventas_por_mes['Mes'].astype(str), ventas_por_mes['Ventas Totales'], color='skyblue')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales por Mes')
plt.xticks(rotation=45)
plt.show()

# Gráfico de Productos Más Vendidos
plt.figure(figsize=(10, 6))
plt.bar(productos_mas_vendidos['Producto'], productos_mas_vendidos['Cantidad Vendida'], color='salmon')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')
plt.title('Productos Más Vendidos')
plt.xticks(rotation=45)
plt.show()

# Gráfico de Ventas por Tienda
plt.figure(figsize=(10, 6))
plt.bar(ventas_por_tienda['Tienda'], ventas_por_tienda['Ventas Totales'], color='green')
plt.xlabel('Tienda')
plt.ylabel('Ventas Totales')
plt.title('Ventas por Tienda')
plt.show()

5. Conclusión:

¿Qué mes tuvo las mayores ventas?
¿Qué productos son los más vendidos?
¿Qué tienda tiene mejor rendimiento?
