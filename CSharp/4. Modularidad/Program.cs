Console.WriteLine("Modularidad");
//modulos --> funcion especifica
//calcular Productos

static string leer_producto()
{
    Console.Write("Ingrese nombre de su producto: ");
    return Console.ReadLine();

}

static double leer_precio()
{
    Console.Write("Ingrese el precio de su producto: ");
    return double.Parse(Console.ReadLine());

}

static double calcular_igv(double precio)
{
    return precio * 0.18;
}

static void mostrar_resultados(string nombre, double precio, double igv)
{
    double total = precio + igv;
    Console.WriteLine($"Producto: {nombre}");
    Console.WriteLine($"Precio: {precio}");
    Console.WriteLine($"IGV: {igv}");
    Console.WriteLine($"Total: {total}");
}

string nombre =leer_producto();
double precio = leer_precio();
double igv = calcular_igv(precio);
mostrar_resultados(nombre, precio, igv);
