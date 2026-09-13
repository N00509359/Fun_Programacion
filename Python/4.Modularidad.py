# modulos --> funcion especifica

## calcular Productos

def leer_productos():
    return input("ingrese un producto: ")

def leer_precio():
    return float (input("ingrese un Precio: "))

def calcular_igv(precio):
    return precio*0.18

def resultados(nombre, precio, igv):
    total=precio + igv
    print(f"producto: {nombre}")
    print(f"precio: {precio}")
    print(f"IGV: {igv}")
    print(f"total a pagar: {total}")
    
nombre = leer_productos()
precio = leer_precio()
igv = calcular_igv(precio)
resultados(nombre,precio,igv)
