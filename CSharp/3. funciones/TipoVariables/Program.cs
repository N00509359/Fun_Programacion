Console.WriteLine("--tipos de variables --");
static void saludar()
{
    string nombre ="Raquel";
    Console.WriteLine($"hola {nombre}, bienvenido");
}
saludar();
//Console.WriteLine(nombre);

Console.WriteLine("variable global - compartida");
int incrementar=0;
static void incrementa(int a)
{
    a++;
    Console.WriteLine($"el valor de incrementar es: {a}");
}
incrementa(incrementar);
incrementa(incrementar);


Console.WriteLine("variable no local");
static void calcularMonto()
{
    double subtotal = 100;
    double calcular_igv(double a)
    {
        return a*0.18;
    }
    double resultado = calcular_igv(subtotal);
    Console.WriteLine($"el resultado subtotal es: {resultado + subtotal}");
}
calcularMonto();