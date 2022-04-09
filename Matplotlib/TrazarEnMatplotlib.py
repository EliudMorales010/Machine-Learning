import matplotlib.pyplot as plt
import numpy as np

# Funcion plot():
'''
Se utiliza para dibujar puntos (marcadores) en un diagrama
Por defecto dibuja una linea de punto a punto
Toma parametros:
Parametro 1: Es una matriz  que contiene los puntos en el eje x
Parámetro 2: Es una matriz que contiene los puntos en el eje y

Si necesitamos trazar una línea de (1, 3) a (8, 10), 
tenemos que pasar dos matrices [1, 8] y [3, 10] a la función de trazado.

El eje x es el eje horizontal.
El eje y es el eje vertical.
'''

# Ejemplo: 
xpuntos = np.array([1, 8])
ypuntos = np.array([3, 10])
plt.plot(xpuntos, ypuntos)
plt.show()

# Trazado sin linea:
'''
Para trazar solo los marcadores, 
puede usar el parámetro de notación de cadena de método abreviado 'o', que significa 'anillos'
'''
xpuntos = np.array([1, 8])
ypuntos = np.array([3, 10])
plt.plot(xpuntos, ypuntos, 'o')
plt.show()

