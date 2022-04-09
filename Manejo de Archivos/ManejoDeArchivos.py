# Funcion open():

'''
Toma 2 parámetros, nombre del archivo y el modo(metodo)
Hay 4 modos(metodos):

"r" = Leer: el valor por defecto , Abre un archivo para lectura, y da error si el archivo no existe
"a" = Agregar: Abre un archivo para agregar, crea un archivo si no existe
"w" = Escribir: Abre un archivo  para escribir, puede crear el archivo si no existe
"x" = Crear: crea un archivo especificado. devuelve un error si el archivo existe

Además, puede especificar si el archivo debe manejarse como modo binario o de texto
"b" = Binario: Modo binario(por ejemplo, imagenes)
"t" = Texto: Valor por defecto, modo de texto
'''
# sintaxis
f = open("hola.txt")