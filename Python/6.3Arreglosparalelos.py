print("Arreglos Paralelos")
# Sintaxis
nombres = ["Susana", "Diana", "Luis"]
edades = [37,42,18]
for i in range(len(nombres)):
    print(f'Nombre: {nombres[i]} - Edad: {edades[i]}')

# Correspondencia por indice
indice = 1
print(f'Nombre: {nombres[indice]}')
print(f'Edad: {edades[indice]}')

# Validar coherencia longitud cadenas
if len(nombres) == len(edades):
    print("Las Estructuras Son Coherentes.")
else:
    print("Las Estructuras NO Son Coherentes.")

# Estructura Combinada
persona = [44444444, "Juan Perez", 35]
print(f'DNI: {persona[0]}')
print(f'Nombre: {persona[1]}')
print(f'Edad: {persona[2]}')

# Usando Diccionarios
persona2 = {
    "DNI": 45454545,
    "Nombre": "Maria Gonzalez",
    "Edad": 37,
    "Estado Civil": "Soltera"
}
print(f'DNI: {persona2["DNI"]}')
print(f'Nombre: {persona2["Nombre"]}')
print(f'Edad: {persona2["Edad"]}')
print(f'Estado Civil: {persona2["Estado Civil"]}')

# Usando Clases
class Estudiante:
    def __init__(self, dni, nombre, edad, estado):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.estado = estado

est = Estudiante(78787878, "Juan Perez", 54, "Viudo")
print(f'{est.dni}, {est.nombre}, {est.edad}, {est.estado}')