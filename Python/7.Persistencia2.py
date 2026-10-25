print ("Operaciones Abrir, Leer, Escribir y Cerrar archivos")

#utilizar import os

import os
nombre_archivo="Python\\escribir.txt"
# obtener la ruta
ruta_completa = os.path.abspath(nombre_archivo)
print(f'Nombre Archivo: {nombre_archivo}')
print(f'Ruta Completa: {ruta_completa}')

# Escribir 
archivo = open(nombre_archivo, "w", encoding="utf-8")
archivo.write("Archivo abierto en modo escritura. \n")
archivo.close()

print("Archivo creado y escrito correctamente.")

# Escribir varias lineas
with open (nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("Maria \n")
    archivo.write("Esperanza \n")
    archivo.write("Sofia \n")

print("Datos escritos correctamente")

#escribir eliminar

with open (nombre_archivo, "a", encoding="utf-8") as archivo:
    archivo.write("Maria Fernanda \n")
    archivo.write("Perla \n")


#leer contenido
with open (nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)

#leer linea por linea

with open (nombre_archivo, "r", encoding="utf-8") as archivo:
    lineal = archivo.readline()
    linea2 = archivo.readline()
    linea3 = archivo.readline()
    linea4 = archivo.readline()
    linea5 = archivo.readline()

print(f"linea 1: {lineal}")
print(f"linea 2: {lineal}")
print(f"linea 3: {lineal}")
print(f"linea 4: {lineal}")
print(f"linea 5: {lineal}")


#leer como coleccion 
with open (nombre_archivo, "r", encoding="utf-8") as archivo:
    contenido = archivo.readlines()

for i in range (len(contenido)):
    print(f'linea{i+1}: {contenido[i].strip()}')
    
