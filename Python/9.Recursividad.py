# Funcio saludar
# def indica funcion
# saludar nombre funcion
#nombre es el parametro de la funcion
#return lo que devuelve la funcion

def saludar(nombre):
    print (f'Hola, Buen día {nombre}')
# Llamar a la funcion
# nombre(argumentos)
saludar('Raquel')

def sumar(a,b):
    return a+b
resultado = sumar(7,8)
print(resultado)

# print("funcion recursiva")



"""
def funcion_recursiva(parametro):
        if condicion_de_parada:
        return valor_conocido
    else:
        return operacion(parametro, funcion_recursiva(parametro_reducido))
"""



def cuenta_regresiva(n):
    #caso base
    if n==0:
        print ("¡fin!")
        return
    
    print(n)
    #caso recursivo(llamado asi mismo)
    cuenta_regresiva(n-1)

cuenta_regresiva(7)

##Errores comunes en recursividad
#sin caso base
"""
def f(n):
    returnf(n-1) ##recursividad inifinita
f()
3
2
1
-1
-2
...
- infinito
"""
#caso base inalcanzable

"""
def f1(n):
    if n==0:
    n=5
    f1(n-2)
5
3
1
-1
-3
-5

def f2(n):
    return n+f(n)#1
    1+ 1+1+1+1+1+1+1+1+1+1+1+1+1+1 --infinito


Desbordamiento
    f(100000)
"""

print("Funciones Recursivas Simples")
#Factorial
""" 
factorial 5! = 5 x 4 x 3 x 2 x 1 = 120
n! = 1 --> n=0-------> caso base
n! = n* (n-1)! --> n > 0 ---> caso recursivo
"""
def factorial (n):
    #caso base 
    if n ==0:
        return 1
    else:
        # CASO RECURSIVO
        return n*factorial(n-1)
print (factorial(5))
print(factorial(0))


#Potencia
"""
base^exp=1 ----> exp=0
base^exp= base x base^(exp-1)   ----> exp > 0
"""
def potencia(base, exp):
    #caso base
    if exp==0:
        return 1
    else:
        #caso recursivo
        return base * potencia(base, exp-1)

print(potencia(2,10))
print(potencia(5,0))
#Sumatoria
"""
suma(n)=0 --> n=0
suma(n)= n+suma(n-1) ---> n>0
"""
def suma_hasta(n): #SUMANDO DE 1 A n
    if n==0:
        return 0
    else:
        return n+ suma_hasta(n-1)
print(suma_hasta(10))


#suma de elementos de una lista

"""
suma_lista([a, ...restoelementos]) = a+ suma_lista(resto)
suma_lista([]) = 0
"""
def suma_lista(lista):
    if len(lista)==0:
        return 0
    else:
        return lista[0]+suma_lista(lista[1:])

print (suma_lista([10,20,30,40,50]))

#Conteo
