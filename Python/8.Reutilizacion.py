
print("Reutilizar Codigo")
print("-----------------")
def calcular_total(precio, cantidad):
    return precio* cantidad

total_lapices = calcular_total(1.50, 7)
total_cuadernos = calcular_total(5.20, 7)

print(f'Total Lapices: s/.{total_lapices}')
print(f'Total Cuadernos: s/.{total_cuadernos}')

print("Reutilizar Funciones")
print("-----------------")
def  es_nota_valida(nota):
    return nota >= 0 and nota <= 20

nota1 = 18
nota2 = 25

print(f"Nota 1 Válida: {es_nota_valida(nota1)}")
print(f"Nota 2 Válida: {es_nota_valida(nota2)}")

print("Abstraccion de Funcionalidad Comun")
print("----------------------------------")
def calcular_promedio(n1, n2, n3):
    return (n1+n2+n3)/3

promedio = calcular_promedio(14,10,17)
print(f'Promedio: {promedio}')

print("Biblioteca Estandar")
print("-----------------")
import math
import datetime
import os

numero = 25
raiz = math.sqrt(numero)

fecha_actual = datetime.datetime.now()
carpeta_actual = os.getcwd()

print(f'Raiz Cuadrada: {raiz}')
print(f'Fecha Actual: {fecha_actual}')
print(f'Carpeta Actual: {carpeta_actual}')

print("Bibliotecas Externas")
print("-----------------")
import requests
url="https://httpbin.org/get"
respuesta = requests.get(url)
codigo = respuesta.status_code
print(f"Codigo de Respuesta: {codigo}")

import pandas as pd
ventas = pd.DataFrame({
    "Productos":["Mouse", "Teclado", "Monitor"],
    "Precio":[36.89, 76.78, 760.00],
    "Cantidad":[3,5,7]
})

ventas["Subtotal"] = ventas["Precio"]*ventas["Cantidad"]
total_general = ventas["Subtotal"].sum()
print("Reporte de Ventas:")
print(ventas)
print(f'Total General: {total_general}')

import numpy as np
notas = np.array([14, 16,19,10])
promedio = np.mean(notas)
nota_maxima = np.max(notas)
nota_minima = np.min(notas)
aprobados = notas[notas>=12]
cantidad_aprobados = len(aprobados)
print(f'Notas Registradas: {notas}')
print(f'Promedio: {promedio}')
print(f'Nota Maxima: {nota_maxima}')
print(f'Nota Minima: {nota_minima}')
print(f'Notas Aprobadas: {aprobados}')
print(f'Cantidad Aprobados: {cantidad_aprobados}')

print("Principio DRY")
print("-----------------")
# Evitar duplicidad de código
def mostrar_estado(tarea, completada):
    if completada:
        print(f'{tarea}, - Completada')
    else:
        print(f'{tarea}, - Pendiente')

mostrar_estado("Revisar Codigo", True)
mostrar_estado("Probar Programa", False)

print("Reutilizacion a gran Escala")
print("---------------------------")
def normalizar_texto(texto):
    return texto.strip().lower()

nombre1 = "   ADMIN   "
nombre2 = "  Usuario   "

print(f"Texto 1: {normalizar_texto(nombre1)}")
print(f"Texto 2: {normalizar_texto(nombre2)}")

print("Reutilizacion en el Enfoque")
print("---------------------------")

def calcular_descuento(monto, porcentaje):
    return monto*porcentaje/100

monto_total = 200
descuento = calcular_descuento(monto_total, 10)
monto_final= monto_total - descuento

print(f"Descuento: s/.{descuento}")
print(f'Monto Final: s/.{monto_final}')