print ("Persistencia de Datos")
#capacidad de conservar informacion despues de terminar una ejecucion
#Crear un archivo y escribir un mensaje
with open ("Python\datos.txt" , "w", encoding="utf-8") as archivo:
    archivo.write("Hola extudiantes\n")

print ("Archivo creado correctamente.")

#Abrir el archivo leer el contenido 
with open ("Python\datos.txt" , "r", encoding="utf-8") as archivo:
        contenido = archivo.read();

print(f'contenido: {contenido}')


print ("puntero de archivo")
#Crear un archivo --apuntar a un indice
with open ("Python\estudiantes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Susana\nDiana\nMaria\n")

with open("python\estudiantes.txt", "r", encoding= "utf-8") as archivo:
    posicion_inicial = archivo.tell()
    primera_linea= archivo.readline()
    posicion_final = archivo.tell()

print (f'Posicion Inicial: {posicion_inicial}')
print(f'Primera Linea:{primera_linea}')
print(f'Posicion Final: {posicion_final}')


