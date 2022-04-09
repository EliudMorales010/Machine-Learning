'''
Para escribir en un archivo existente, debe agregar un parámetro a la función open():

"a"- Agregar: se agregará al final del archivo

"w"- Escribir: sobrescribirá cualquier contenido existente

'''
# Ejemplo: Abriel el archivo leerarchivo.txt y agregar contenido al archivo


f = open("C:/Users/eliud/OneDrive/Documentos/MACHINE LEARNING/MANEJO DE ARCHIVOS EN PYTHON/leerarchivo.txt", "a")
f.write("\nAqui se agrego mas informacion al archivo")
f.close()

# Abro el documento despues de agregar contenido
f = open("C:/Users/eliud/OneDrive/Documentos/MACHINE LEARNING/MANEJO DE ARCHIVOS EN PYTHON/leerarchivo.txt", "r")
print(f.read())