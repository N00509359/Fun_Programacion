"""
Leer un codigo de estudiante y su carrera
Forma una etiqueta
Mostrar la longitud codigo, carrera, etiqueta
Mostrar primer y ultimo caracter del codigo
Recorrer cada letra de la carrera
Crear una etiquetra nueva agregando el semestre sin alterar la original
"""

codigo= input("Ingrese su codigo: ")
carrera= input("Ingrese su carrera: ")
etiqueta = codigo +"  |" + carrera
etiqueta_periodo = etiqueta + "|2026-2"


print (etiqueta)
print(f'Longitud del codigo: {len(codigo)}')
print(f'Longitud de la carrera: {len(carrera)}')
print(f'Longitud de la etiqueta: {len(etiqueta)}')

if len(codigo)>0:
    print(f'Primer caracter: {codigo[0]}')
    print(f'Ultimo craracter: {codigo[len(codigo)-1]}')

print("Recorriendo la carrera")
for i in range(len(carrera)):
    print(f'{i}-> {carrera[i]}')