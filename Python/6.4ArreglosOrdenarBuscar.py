print("ORDENAMIENTO DE CADENAS")
print("-----------------------")
print("Ordenamiento Alfabetico")
# Sintaxis
# Crear Lista
nombres = ["Zendaya", "Americo", "Luis", "Tania", "Carlos", "Ernesto"]

# Ordenar alfabeticamente
ordenado_alfa = sorted(nombres)

# Mostrar lista ordenada
print(f'A-Z: {ordenado_alfa}')

print("Ordenamiento Longitud Palabra")
# Ordenar por la cantidad de letras de menor a mayor
# Usando la lista de nombres
ordenado_len = sorted(nombres, key=len)
# Mostrar lista ordenada
print(ordenado_len)

print("Ordenamiento Personalizado")
articulos = ["Laptop", "Impresora", "Gamer", "Teclado", "Mouse"]
# Ordenar segun la ultima letra de la cadena
ordenado_personalizado = sorted(articulos, key=lambda texto: texto[-1])
# Mostrar lista ordenada
print(ordenado_personalizado)

print("Ordenamiento Burbuja para Cadenas")
nombres2 = ["Zendaya", "Americo", "Luis", "Tania", "Carlos", "Ernesto"]
for i in range(len(nombres2)):
    for j in range(0, len(nombres2) -1):
        if nombres2[j] > nombres2[j+1]:
            nombres2[j], nombres2[j+1] = nombres2[j+1], nombres2[j]

# Mostrar lista ordenada
print(nombres2)

print("Ordenamiento Seleccion Cadenas")
nombres3 = ["Zendaya", "Americo", "Luis", "Tania", "Carlos", "Ernesto"]
for i in range(len(nombres3)):
    menor=i
    for j in range(i+1, len(nombres3)):
        if nombres3[j] < nombres3[menor]:
            menor=j
    nombres3[i], nombres3[menor]=nombres3[menor], nombres3[i]

print(nombres3)

print("Ordenamiento por Insercion de Cadenas")
nombres4 = ["Yesenia", "Americo", "Maria", "Tania", "Daniel", "Ernesto"]
for i in range(1,len(nombres4)):
    actual = nombres4[i]
    j=i-1
    while (j>=0 and nombres4[j] > actual):
        nombres4[j+1]=nombres4[j]
        j -=1
    nombres4[j+1]=actual

print(nombres4)


#PDF 4.4 Busqueda
""" 
Crear un arreglo Y desarrollar todos los metodos
"""
#Busqueda Exacta - Equals
#Busqueda Sensible a Mayusculas y Minusculas
#Busqueda de subcadenas
#Busqueda de Expresion Regular
#Busqueda Ultima posicion - LastIndexof
#Busqueda Ultima posicion - Indexof
#Busqueda empieza tecxto especifico - startswitch
#Busqueda termina tecxto especifico - endtswitch