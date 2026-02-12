import numpy as np
import matplotlib.pyplot as plt


datos = np.loadtxt('numeros.txt')

plt.hist(datos, bins=10, color='green', edgecolor='black')

plt.title('Histograma de Números Cargados desde datos.txt')
plt.xlabel('Rango de valores (1-100)')
plt.ylabel('Frecuencia')

plt.show()