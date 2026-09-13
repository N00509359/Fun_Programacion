def saludar ():
#def saludar (a,b,c):--> a,b,c son parametros
 print ("Bienvenido al curso de Fundamentos de Programacion")

# invocar o Llamar a una funcion
saludar()
#saludar(1,2,3) --> son argumentos

## Declarar funcion sin retorno
def menu():
    print("1.Registrar")
    print("2.Buscar")
    print("3.Salir")

menu()

## Declarar funcioN CON RETORNO
def producto(a,b):
    return a*b

#Llamar a funcion retorno pasando argumentos
resultado = producto (8,7)
print(f'{resultado}, resultado*2 = {resultado*2}')

## funcion con varios argumentos
def promedio(T1,T2,T3,EP,EF):
    return T1*0.10+T2*0.10+T3*0.10+EP*0.20+EF*0.50
resultado1 = promedio(20,20,20,14,12)
print(f'tu promedio final es {resultado1}')

## declarar funcion con paraametros determinados
##-----------------------------------
def saludar_estudiante(nombre, curso= 'Fundamentos de Programacion'):
    print (f'hola {nombre}, Bienvenido a {curso}')
saludar_estudiante('Raquel')
saludar_estudiante('Raquel','base de datos')


## funciones anidadas
##-----------------------------------
def proceso_compra(monto):
    def aplicar_igv(valor):
        return valor*0.18
    igv= aplicar_igv(monto)
    total = monto + igv    
    return total
resultado2 = proceso_compra(550)
print(f'total a pagar con igv es: s/{resultado2}')
