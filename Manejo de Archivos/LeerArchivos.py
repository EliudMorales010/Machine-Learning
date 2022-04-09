'''
f = open("LeerArchivo.txt", "r")
print(f.read())


# si el archivo se encuentra en una ruta diferente intenta esto:

y = open("C:/Users/eliud/OneDrive/Documentos/MACHINE LEARNING/MANEJO DE ARCHIVOS EN PYTHON/leerarchivo.txt","r")
print(y.read())

# El metodo read() tambien puede devolver partes del archivo, por ejemplo caracteres

x = open("C:/Users/eliud/OneDrive/Documentos/MACHINE LEARNING/MANEJO DE ARCHIVOS EN PYTHON/leerarchivo.txt","r")
print(x.read(4))
'''
# Metodo readline(): Permite poder devolver solo una linea o un renglón, cada readline es un renglón
j = open("C:/Users/eliud/OneDrive/Documentos/MACHINE LEARNING/MANEJO DE ARCHIVOS EN PYTHON/leerarchivo.txt","r")
print(j.readline())
print(j.readline())

# Tambien se puede recorrer las lineas del archivo, se puede leer el archivo
k = open("C:/Users/eliud/OneDrive/Documentos/MACHINE LEARNING/MANEJO DE ARCHIVOS EN PYTHON/leerarchivo.txt","r")
for x in k:
    print(x)
    
# Siempre es bueno cerrar los archivos despues de ocuparlos
f = open("demofile.txt", "r")
print(f.readline())
f.close()