import pandas as pd
tabla = pd.read_csv('C:/Simon\OneDrive/Python\Análisis de Datos con Pandas y Python/ventasTotales.csv', skiprows=5, delimiter=';')
print(tabla)

#tabla.shape()

#print(tabla.head())
#print(tabla.tail())
#print(tabla.info())

#print(tabla.Vendedor.value_counts(ascending=True))
#print(tabla.Región.value_counts(ascending=True, dropna=False))
#print(tabla.Vendedor.sort_values())

#print(tabla.sort_values(by=['Vendedor', 'Ganancia']))

#print(tabla[(tabla.Artículo == 'Gorras') & (tabla.Región == 'Norte')])

print(tabla[tabla.Vendedor.str.startswith('A')])

