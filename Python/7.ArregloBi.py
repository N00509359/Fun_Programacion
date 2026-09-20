# Arreglos Bidimensionales - Matrices - Tablas
# Declarar matriz

matriz = [
    [1, 2, 3], #Filas 1
    [4, 5, 6]
]
print (matriz)
print (type(matriz))

matriz2 =[
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

print(matriz2)
print(matriz2[1][2])

# Recorrer la matriz
for fila in range(len(matriz2)):
    for columna in range(len(matriz2[fila])):
        print(f'Fila: {fila}, columna: {columna}, Valor: {matriz2[fila][columna]}')