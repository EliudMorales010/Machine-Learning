'''
Para eliminar un archivo debe importar el modulo de sistema operativo (os)
y ejecutar la funcion os.remove()

os.remove("leerarchivo.txt")
'''


# Antes de eliminar verifique que el archivo exista 

import os
if os.path.exists("leerarchivo.txt"):
    os.remove("leerarchivo.txt")
else:
    print("El archivo no existe")

# Eliminar una carpeta

import os 
# solo se pueden eliminar carpetas vacias
os.rmdir("micarpeta")