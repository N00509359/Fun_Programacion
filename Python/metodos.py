print("Funciones y Módulos")

# Tipos de Funciones
"""
Funciones sin parametros
Funciones con parametros
Funciones sin retorno
Funciones con retorno
"""
def sumar (a,b):
    return a+b

def calcular_promedio(nota1,nota2):
    return (nota1+nota2)/2

# Declarar una funcion
## -------------------------------
# def saludar(a,b,c): --> a,b,c son parametros
def saludar():
    print("Bienvenido al curso de Fundamentos de Programación")

# saludar(1,2,3) --> 1,2,3 son argumentos

## Declarar funcion sin retorno
## -------------------------------
def menu():
    print("1. Registrar")
    print("2. Buscar")
    print("3. Salir")

## Declarar funcion con retorno
## -------------------------------
def producto(a,b):
    return a * b

## Funcion con varios argumentos
## -------------------------------
def promedio(T1, T2, T3, EP, EF):
    return T1*0.10 + T2*0.10 + T3*0.10 + EP*0.20 + EF*0.50

## Declarar Funcion con parametros determinados
## -------------------------------

def saludar_estudiante(nombre, curso='Fundamentos de Programación'):
    print(f'Hola {nombre}, Bienvenido a {curso}')

## Funciones Anidadas
## -------------------------------

def proceso_compra(monto):
    def aplicar_igv(valor):
        return valor*0.18

    igv= aplicar_igv(monto)
    total = monto + igv
    return total

## Funciones Paso Parametros por Valor
## -------------------------------
def incrementar_valor(numero):
    numero = numero + 5
    print(f'Dentro Funcion: {numero}')

## Funciones Paso Parametros por Referencia
## -------------------------------
def añadir_producto(productos):
    productos.append("Laptop")
    print(f'Dentro de la Funcion: {productos}')