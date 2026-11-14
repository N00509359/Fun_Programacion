print("Organizacion Clases simples")
print("***************************")
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        return f"Producto: {self.nombre} | Precio: {self.precio}"

producto = Producto("Cuaderno", 12.50)
print(producto.mostrar())

print("Modulo o Clase")
print("**************")
def convertir_a_dolares(soles):
    tipo_cambio=3.49
    return soles / tipo_cambio

monto=150
dolares = convertir_a_dolares(monto)
print(f'Monto en dolares: {round(dolares, 2)}')

# Buenas practicas Codificación
print("Buenas Practicas de Codificacion")
print("********************************")
nombre_producto = "Cuaderno"
precio_unitario = 4.70
cantidad = 8
total = precio_unitario * cantidad
print(f'Producto: {nombre_producto}')
print(f'Total a Pagar: s/.{total}')

print("Buenas Practicas de Legibilidad del Codigo")
print("******************************************")
nota_practica = 16
nota_examen=18
promedio= (nota_practica + nota_examen) / 2
if promedio >=13:
    print("El estudiante aprobó")
else: 
    print("El estudiante NO aprobó")

print(f'Promedio final: {promedio}')

print("Buenas Practicas Comentarios utiles")
print("******************************************")
monto_servicio = 120 # se define monto inicial que el usuario debe pagar por el servicio
porcentaje_descuento = 10 # se define el porcentaje de descuento aplicado
descuento = monto_servicio * porcentaje_descuento / 100 # calcula el descuenti convirtiendo a decimal
monto_final = monto_servicio - descuento # se calcula el monto final restando monto inicial - descuento
print(f'Descuento aplicado: {descuento}')
print(f'Monto Final: s/. {monto_final}')

print("Buenas Practicas Convenciones en Codificacion")
print("******************************************")
# usar snake_case para nombre de variables
nombre_estudiante = 'Susana'

# usar snake_case para nombres compuestos
cantidad_cursos = 5

# MAYUSCULAS para constantes
NOTA_MINIMA_APROBATORIOA = 13

# Asignar valor a una variable
nota_final = 15

if nota_final > NOTA_MINIMA_APROBATORIOA:
    print(f'{nombre_estudiante}, Aprobó el Curso')

else:  # se ejecuta cuando no se cumple la condicion
    print(f'{nombre_estudiante}, No Aprobó el Curso')

print(f'Cursos registrados: {cantidad_cursos}')

print("Buenas Practicas Nombres significativos")
print("******************************************")
# indica la horas que trabajo la persona
horas_trabajadas = 8

# indica cuanto se paga por hora trabajada
pago_por_hora = 12

# almacena el calculo de horas trabajadas por pago por hora
salario = horas_trabajadas*pago_por_hora

# devuele el total salario
print(f'Salario: s/. {salario}')

print("Buenas Practicas Identacion")
print("******************************************")

edad = 18

if edad >= 18:
    print("Puede Registrarse") # pertenece al bloque if
    print("Registro Permitido") # pertenece al bloque if

else:
    print("NO Puede Registrarse") # pertenece al bloque else
    print("Registro NO Permitido") # pertenece al bloque else

print("Mensaje Final") # no tiene identacion, pertenece al bloque principal main