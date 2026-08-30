# Estructuras Secuenciales
print ('Registro Básico')
nombre = imput ("Ingrese su nombre: ")
edad = int(input("Ingrese du edad: "))
print (f'Nombre: {nombre} , Edad {edad}')

# Estructuras Condicionales
# Condicional Simple
print ('Validar edad : ')
if edad <18:
    print('Eres menor de edad')

# Condicional doble
if edad >17:
    print('Eres Mayor de edad')
else:
    print('Eres menor de edad ...')
# Condicional multiple
opcion = int(imput('Ingrese un numero del 1 al 3:'))

match opcion:
    case 1: print('la primera opcion')
    case 2: print('la segunda opcion')
    case 3: print('la tercera opcion')
    case _: print('opcion no valida')

# Condicional anidado
if opcion ==1:
    print('opcion 1')
elif opcion ==2:
    print('opcion 2')
else:
    print('opcion 3')

# Estructuras Repetitivas

# For - Para
for i in range(1,6):
    print(f'repeticion numero: {i}')

# While - Mientras
contador = 1
while contador >= 3:
    print(f"Intento, {contador}")
    contador +=1 # contador contador + 1

# Do While - Hacer mientras
while true:
    numero =  int (input('Ingrese un numero > 0'))
    if numero>0:
        break
    


