import csv
#API formato JSON --Pares--> Clave:Valor --> "Nombre": "Raquel"
import json
import sqlite3


#Persistencia de datos con archivos

print ('Datos Organizados con estructura definida')
estudiantes = [
    ["E001", "Jaime", "17"],
    ["E002", "Diana", "16"],
    ["E003", "Susana", "14"]
]
archivo_csv = open("Python\\estudiante_csv.txt", "w", encoding="utf-8")
for estudiante in estudiantes:
    linea =",".join(estudiante)
    archivo_csv.write(linea+"\n")
archivo_csv.close()

archivo_tsv = open("Python\\estudiante_tsv.txt", "w", encoding="utf-8")
for estudiante in estudiantes:
    linea ="\t".join(estudiante)
    archivo_tsv.write(linea+"\n")
archivo_csv.close()

archivo_pipe = open("Python\\estudiante_csv.pipe", "w", encoding="utf-8")
for estudiante in estudiantes:
    linea ="|".join(estudiante)
    archivo_pipe.write(linea+"\n")
archivo_csv.close()

print ("Archivos CSV, TSV Y PIPE CREADOS CORRECTAMENTE")



#Archivos CSV EN PYTHON
with open("Python\\estudiantes.csv","w", newline="", encoding="utf-8") as archivo:
    escritor=csv.writer(archivo)
    escritor.writerow(["Codigo", "Nombre", "Nota"])
    escritor.writerow(["E001", "Jaime", "17"])
    escritor.writerow(["E002", "Diana", "16"])
    escritor.writerow(["E003", "Susana", "14"])

print ("Archivo estudiantes.csv creado correctamente!!")
with open ("python\\estudiantes.csv", "r", newline="", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)
    print(f'Encabezado:{encabezado}')
    for fila in lector:
        Codigo = fila[0]
        nombre = fila[1]
        nota = fila[2]
        print(f'Codigo: {Codigo}- Nombre:{nombre}- Nota:{nota}')



#Crear lista productos en formato JSON
productos =[
    {
        "Codigo":"P001",
        "NOMBRE": "Laptop",
        "Categoria": "Tecnologia",
        "Precio": 2500.00,
        "Stock":20
    },
    {
        "Codigo":"P002",
        "NOMBRE": "Mouse",
        "Categoria": "Tecnologia",
        "Precio": 75.00,
        "Stock":40
    },
    {
         "Codigo":"P003",
        "NOMBRE": "Router",
        "Categoria": "Comunicaciones",
        "Precio": 200.00,
        "Stock":10
    }
]
with open("python\\productos.json","w", encoding="utf-8") as archivo:
    #guardar los productos en JSON
    json.dump(productos, archivo, indent=4, ensure_ascii=False)
    print("archivo productos.json creado correctamente")

#leer el contenido del archivo json

with open("python\\productos.json", "r", encoding="utf-8") as archivo:
    productos = json.load(archivo)
    print("Lista de productos")
    print("********************")
    for producto in productos:
        print(f'Codigo: {producto["Codigo"]}')
        print(f'Nombre{producto["NOMBRE"]}')
        print(f'Categoria: {producto["Categoria"]}')
        print(f'Precio: {producto["Precio"]}')
        print(f'Stock:{producto["Stock"]}')
        valor_inventario = producto["Precio"] * producto["Stock"]
        print(f'Valor del inventario: s/ {valor_inventario}')
        print("----------------------------")

#Limitaciones csv, TSV, PIPE, ETC. CAPACIDAD almacenamiento
# --> Migrar wn Base de datos
# usar SQLite --> sqlite3
conexion = sqlite3.connect("python\\estudiante.db")
cursor= conexion.cursor()
cursor.execute("drop table if exists estudiante ")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS estudiante(
        id integer primary key autoincrement,
        nombre text not null,
        edad integer not null
    )
    """
)
cursor.execute("DELETE FROM estudiante")
cursor.execute("INSERT INTO estudiante(nombre, edad) values (?,?)", ("Susana",25))
cursor.execute("INSERT INTO estudiante(nombre, edad) values (?,?)", ("Maria", 35))
cursor.execute("INSERT INTO estudiante(nombre, edad) values (?,?)", ("Jaime", 40))
cursor.execute("INSERT INTO estudiante(nombre, edad) values (?,?)", ("Diana", 34 ))

conexion.commit()
#Consultae
cursor.execute("SELECT id, nombre, edad from estudiante")
registros = cursor.fetchall()

for fila in registros:
    print(f'ID: {fila[0]}, Nombre: {fila[1]}, edad {fila[2]}')
conexion.close()



