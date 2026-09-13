using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

Console.WriteLine("-- Funciones");
static void saludar()
{
    Console.WriteLine("hola, bienvenidos a fundamentos");
}

saludar();

Console.WriteLine("--funciones sin retorno--");
Console.WriteLine("---------------------");
menu();
static void menu()
{
    Console.WriteLine("1. Registrar");
    Console.WriteLine("2. Buscar");
    Console.WriteLine("3. Salir");
}


Console.WriteLine("--funciones con retorno--");
Console.WriteLine("---------------------");
int resultado=producto(8,7);
Console.WriteLine($"resultado, resultado*2={resultado*2}");
static int producto(int a, int b)
{
    return a * b;
}

Console.WriteLine("--funciones con varios argumentos--");
Console.WriteLine("---------------------");

static double promedio(double t1, double t2, double t3, double ep, double ef)
{
    return t1*0.10+ t2*0.10+ t3*0.10 + ep*0.2+ ef*0.50;
}
double prom = promedio(20,20,20,14,12);
Console.WriteLine($"promedio obtenido es:{prom}");


Console.WriteLine("--funciones con parametros predeterminados--");
Console.WriteLine("        ---------------------");

static void saludar_estudiante(string nombre, string curso="fundamentos de programacion")
{
    Console.WriteLine($"hola {nombre}, bienvenido a {curso}");
}
saludar_estudiante("Raquel");
saludar_estudiante("Raquel", "base de datos");


Console.WriteLine("--funciones anidadas--");
Console.WriteLine(" ---------------------");
static double proceso_compra(double monto)
{
    double aplicar_igv(double valor)
    {
        return valor*0.18;

    }
    double igv = aplicar_igv(monto);
    double total = monto + igv;
    return total;

}
double venta = proceso_compra(550);
Console.WriteLine($"total a pagar s/ {venta}");

Console.WriteLine("--funciones con parametros por valor--");
Console.WriteLine(" ---------------------");
static void incrementar(int numero)
{
    numero = numero + 5;
    Console.WriteLine($"dentro de la funcion; {numero}");
}
int z=25;
incrementar(z);
Console.WriteLine($" fuera de la funcion; {z}");

Console.WriteLine("--funciones con parametros por por referencia--");
Console.WriteLine(" ---------------------");
static void incrementar_referencia(ref int numero)
{
    numero = numero +10;
    Console.WriteLine($"dentro de la funcion:{numero}");
}
int y=30;
incrementar_referencia(ref y);
Console.WriteLine($"fuera de la funcion: {y}");