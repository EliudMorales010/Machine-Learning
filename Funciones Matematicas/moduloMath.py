# Modulo math:
import math
'''
Python también tiene un módulo integrado llamado math, 
que amplía la lista de funciones matemáticas

Cuando haya importado el mathmódulo, 
puede comenzar a usar métodos y constantes del módulo.
'''
#######################################################################
# Metodo sqrt():
'''
Devuelve la raiz cuadrada de un numero
'''
# Ejemplo:
x =  math.sqrt(64)
print(x)

#######################################################################
# Metodo ceil():
'''
Este metodo redondea un numero hacia arriba, a su entero mas cercano
'''
# Ejemplo:
x = math.ceil(1.4)
print(x)

#######################################################################
# Metodo floor():
'''
Redondea un numero hacia bajo de su entero mas cercano
'''

# Ejemplo:
y = math.floor(3.4)
print(y)

#######################################################################
# Metodo pi():
'''
Devuelve el valor de PI
'''
# Ejemplo: 
x = math.pi
print(x)

#######################################################################
# Metodo fmod():
'''
Devuelve el resto (modulo) de x / y:
- si se ingresa algun 0 en x o en y marca un ValueError
- si no es un numero marcará y TypeError
'''
# Ejemplo:
print(math.fmod(20, 4))
print(math.fmod(20, 3))
print(math.fmod(-10, 3))
print(math.fmod(15, 6))