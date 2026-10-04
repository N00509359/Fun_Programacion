print ("Procesamiento Arreglos lineales")
print("Ordenamiento Metodo Burbuja")

notas =[20, 4, 17, 12, 5, 11, 0, 16]
for pasar in range (len(notas)-1):
    for i in range (len(notas)-1):
        if notas[i] > notas[i+1]:
            temp = notas[i] 
            notas[i] = notas [i+1]
            notas [i+1] = temp

print (notas) 

print ("Metodo de Seleccion")
notas2 =[10, 4, 19, 12, 0, 11, 20, 16]
for i in range(len(notas2)-1):
    pos_menor= i
    for j in range(i+1, len(notas2)):
        if notas2[j] < notas2[pos_menor]:
            pos_menor=j
    temp = notas2[i]
    notas2[i]= notas2[pos_menor]
    notas2[pos_menor]=  temp
print (notas2)

print("metodo Sort()")
precios =[20.1, 0.67, 14.3, 1.76, 100.34, 30.20, 9.99]
precios.sort()
print (precios)

edades =[20, 5, 35, 16, 99, 12, 0]
print("Usando Sorted()")
ordenado = sorted(edades)
print (edades)
print(ordenado)

print("Usando Reverse")
edades.sort(reverse=True)
print(edades)

