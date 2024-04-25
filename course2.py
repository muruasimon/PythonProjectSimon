import matplotlib.pyplot as plt
import pandas as pd

# Fixing the file path
file_path = "C:/Simon/OneDrive/Python/Análisis de Datos con Pandas y Python/ventasTotales.csv"

# Reading the CSV file
tabla = pd.read_csv(file_path, skiprows=5, delimiter=';')

# Filtering data for 'Comestibles' category
linegraphics = tabla[tabla.Categoría == 'Comestibles']

# Plotting the value counts of 'Artículo' column
linegraphics.Artículo.value_counts().plot(kind='pie')

# Display the plot
plt.show()
