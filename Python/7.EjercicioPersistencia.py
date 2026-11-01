import pyodbc
import pandas as pd

#pip install pyodbc pandas
servidor = 'localhost'
base_datos = 'Hospital_Caj'
usuario = 'estudiante'
clave = 'Prueba27'

conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={servidor};'
    f'DATABASE={base_datos};'
    f'UID={usuario};'
    f'PWD={clave};'
    'TrustServerCertificate=yes'
)

print("Conexion exitosa")

cursor = conexion.cursor()
#cursor = conexion.cursor("drop table if exists Python 2")

sql = """
CREATE TABLE Python2(
    id_alumno int identity(1,1) primary key,
    Nombre varchar(100) not null,
    Apellido varchar(100),
    Edad int,
    Ciudad Varchar(100)
)
"""

cursor.execute(sql)
conexion.commit()


#insert 
datos = [
        ('Raquel', 'Valdez', 26, 'Cajamarca'),
        ('Susanita', 'Mejia', 37, 'Cuzco'),
        ('Raquel', 'Reyes',42 , 'Trujillo')
]

cursor.executemany(
    """
    INSERT INTO Python (Nombre, Apellido, Edad, Ciudad)
    values (?,?,?,?)
    """, datos
)

conexion.commit()
#Leer datos 
df=pd.read_sql("SELECT * FROM Python", conexion)

print(f'\n Registros de la tabla Python')
print(df)

cursor.close()
conexion.close()
