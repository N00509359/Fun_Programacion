print ("Arreglo de cadena")
mensaje ="Fundamentos de Programacion"
print(mensaje)
print(mensaje[3])
print(mensaje[10])
print(mensaje[11])

#Inmutabilidad
notas= [14,20,8,15]
notas[2]=12
print(notas)

palabra = "UPN."
#palabra [3]="♠"
print(palabra)

texto=palabra[0]+palabra[1]+palabra[2]+"♠"
print(texto)

#-----------
print ("concatenacion")
nombre = "RAQUEL"
apellido= "VALDEZ"
completo = nombre+ " "+ apellido
print (completo)

#longitud de la cadena
cantidad = len(mensaje)
print (f'El texto{mensaje} tiene una longitud de {cantidad} letras')

#Ultimo caracter

print (f'El ultimo caracter del texto{mensaje} es {mensaje[len(mensaje)-1]} ')

print ("Recorriendo una cadena")
for i in range(len(mensaje)):
    print(f'{i}->{mensaje[i]}')


print ("Metodos para trabajar en cadenas")
# Find
# Slicing
# Split

nombre = "Raquel,Valdez"
posicion_coma=nombre.find(",")

print(f'La coma esta en la posicion: {posicion_coma}')

#Slicing (extraer subcadena)

email = "N0000000@sistemas.PE"
posicion_arroba=email.find("@")
usuario = email [:posicion_arroba]
dominio = email[posicion_arroba +1:]

print (f'Usuario: {usuario}')
print(f'Dominio: {dominio}')


#split 
nombre_curso ="BigData y Base de Datos Avanzada"
partes = nombre_curso.split(" ")
print(partes)
print(partes[0])
print(partes[1])
print(partes[2])
print(partes[3])
print(partes[4])
print(partes[5])


#Replace 
telefono = "+51--987-654-321"
telefono_clean = telefono.replace("-", "")
print(f' Telefono limpio: {telefono_clean}')

# Uper poner a mayusculas
nombre_mayuscula = nombre.upper()
print(nombre_mayuscula)

#Lower poner a minusculas 
nombre_minuscula = nombre.lower()
print(nombre_minuscula)

# Strip (Espacios en blanco)
palabra = "    Aprendiendo Python    "
palabra_limpia = palabra.strip()

print(f'{palabra_limpia}')