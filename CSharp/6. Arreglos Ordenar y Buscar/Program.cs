using System.Security;
using System.Text.RegularExpressions;
Console.WriteLine("Ordenamiento y Busqueda en Cadenas");
Console.WriteLine("Ordenamiento Alfabetico");

List<string> nombres = new List<string>{"Susana", "Diana", "Ana", "Zendaya", "Maria"};
//Ordenar usando metodo sort
nombres.Sort();
//Mostrar la lista ordenada
foreach (string nombre in nombres)
{
    Console.WriteLine(nombre);
}

Console.WriteLine("                ");

Console.WriteLine("Ordenamiento por longitud");
string[] paises ={"Uruguay","Peru","Chile", "Argentina", "USA", "Mexico", "Colombia" };
//Usando OrderBy
string[] ordenados = paises.OrderBy(p=>p.Length).ToArray();
//mostrarlo 
Console.WriteLine(string.Join(", ",ordenados));

Console.WriteLine("                ");

Console.WriteLine("Ordenamiento personalizado");
//Usando OrderBy
string[] ordenados_per=paises.OrderBy(p=>p[p.Length -1]).ToArray();
//mostrarlo
Console.WriteLine(string.Join(",", ordenados_per));

Console.WriteLine("                ");

Console.WriteLine("...Ordenamiento por el metodo de la burbuja...");
string[] nombres2 = {"Susana", "Diana", "Ana", "Zendaya", "Maria"};
for (int i=0;i<nombres2.Length; i++)
{
    for (int j=0; j< nombres2.Length -1; j++)
    {
        if(string.Compare(nombres2[j], nombres2[j + 1]) > 0)
        {
            string temporal = nombres2[j];
            nombres2[j]= nombres2[j+1];
            nombres2[j+1] = temporal;
        }
    }
}
//mostrar ordenamiento 
Console.WriteLine(string.Join(",", nombres2));

Console.WriteLine("                ");

Console.WriteLine("...Ordenamiento por el metodo de seleccion...");
string[] nombres3 = {"Susana", "Diana", "Ana", "Zendaya", "Yesenia"};
for (int i=0; i < nombres3.Length; i++)
{
    int menor= i;
    for (int j = i+1;j<nombres3.Length; j++)
    {
        if (string.Compare(nombres3[j], nombres3[menor]) < 0)
        {
            menor = j;
        }
    }
    string temporal = nombres3[i];
    nombres3[i]= nombres3[menor];
    nombres3[menor]= temporal;
    
}

//MOSTRAR ORDENAMIENTO
Console.WriteLine(string.Join(",", nombres3));

Console.WriteLine("                ");

Console.WriteLine("...Ordenamiento por el metodo de Insercion...");
string[] nombres4 = {"Susana", "Diana", "Ana", "Zendaya", "Yesenia"};
for (int i=0; i<nombres4.Length; i++)
{
    string actual = nombres4[i];
    int j = i-1;
    while(j>=0 && string.Compare(nombres4[j], actual) > 0)
    {
        nombres4[j+1] = nombres4[j];
        j--;
    }
    nombres4[j+1] = actual;
}//MOSTRAR ORDENAMIENTO
Console.WriteLine(string.Join(",", nombres4));

Console.WriteLine("             ");

Console.WriteLine(" ......Busqueda en cadenas.....");
Console.WriteLine(" Busqueda textual -Contains ");
string mensaje = "Aprendiendo Fundamentos de Programacion";
// verificar si la subcadena esta dentro del texto
bool existe = mensaje.Contains("Fundamentos");
Console.WriteLine($"La palabra 'Fundamentos' esta dentro del texto: {existe}");

Console.WriteLine("             ");
Console.WriteLine(" ....Busqueda exacta- Equals.... ");
string clave = "N00123";
string codigo = "N00123";

bool coincide = clave.Equals(codigo);
Console.WriteLine($"La clave {clave} es igual a {codigo}: {coincide}");

Console.WriteLine("             ");

Console.WriteLine(" ....Busqueda Sensible a Mayusculas y Minusculas.... ");
string curso = "PROGRAMACIÓN";
string buscar = "programación";
bool coinciden = curso.Equals(buscar, StringComparison.OrdinalIgnoreCase);
Console.WriteLine($" {curso} es igual a {buscar}: {coinciden}");

Console.WriteLine("             ");

Console.WriteLine(" ....Busqueda de subcadenas.... ");
string fragmento = "Aprendiendo";
bool existe_texto = mensaje.Contains(fragmento);
Console.WriteLine(mensaje);
Console.WriteLine($" {fragmento} está dentro del texto: {existe_texto}");

Console.WriteLine("             ");

Console.WriteLine(" ....Busqueda de Expresion Regular.... ");
String placa ="ABC-123";
//usar Regex. IsMacth
bool  existe_digitos = Regex.IsMatch(placa, @"\d{3}");
Console.WriteLine($"Existe 3 digitos en la placa {placa}:{existe_digitos}");

Console.WriteLine("             ");

Console.WriteLine(" ....Busqueda Primera posicion - Indexof.... ");
int posicion = curso.IndexOf("O");
Console.WriteLine(curso);
Console.WriteLine(posicion);

Console.WriteLine("             ");

Console.WriteLine(" ....Busqueda Ultima posicion - LastIndexof.... ");
int ultima_posicion = curso.LastIndexOf("A");
Console.WriteLine(curso);
Console.WriteLine(ultima_posicion);

Console.WriteLine("             ");

Console.WriteLine(" ....Busqueda empieza tecxto especifico - startswitch.... ");
bool inicia = placa.StartsWith("123");
Console.WriteLine(inicia);

Console.WriteLine("             ");
Console.WriteLine(" ....Busqueda termina tecxto especifico - endtswitch.... ");
bool termina = placa.EndsWith("123");
Console.WriteLine(termina);