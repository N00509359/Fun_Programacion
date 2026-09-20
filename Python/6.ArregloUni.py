# Insertando valor en una posicion
Valores = [0,0,0,0]
print(Valores)

#Insertando valor en una poscion
Valores[1]=25

#Mostrando el Arreglo
print (Valores)

# tipo de dato
print (type(Valores))

#lonfitud de un arreglo
print(f'longitud es: {len(Valores)}')

# EL ultimo elemento
print(f'{Valores[len(Valores)-1]}')

## Arreglo Nombres
Nombres = ['Juan','Maria','Pedro', 'Luis', 'Jose']
print(f'cantidad de Nombres guardados: {len(Nombres)}')
print (f'Ultimo nombre guardado: {Nombres[len(Nombres)-1]}')

Edades = [23, 14, 18, 25, 17]
print (f'Elementos en la posicion 1: {Edades[1]}')
print (f'Elementos en la posicion 4: {Edades[4]}')

## Recorrer un array - arreglo - lista - vector

Notas=[14, 16 , 18, 10, 12, 11]
for i in range(len(Notas)):
    #print("Posicion", i, "Valor: ", Notas[i])
    print(f'Posicion {i} Valor: {Notas[i]}')

print(Nombres)
for k in range(len(Nombres)):
    print(f'Elemento {k+1} Valor {Nombres[k]}')

