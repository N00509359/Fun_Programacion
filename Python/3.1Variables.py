## variables locales
def saludar():
    nombre='Raquel'
    print(f"Hola {nombre} Bienvenido")
saludar()
#print(nombre)

## variables globales
edad = 25

def mostraredad():
    global edad
    print (f"tu edad es: {edad}")

mostraredad()
print(type(edad))

## variable no local
def principal():
    subtotal = 0

    def calcularmonto():
        nonlocal subtotal
        subtotal = 100
        print (f"el nuevo valor es: {subtotal}")
    calcularmonto()
    print (f"el nuevo valor en principal es: {subtotal}")

principal()
