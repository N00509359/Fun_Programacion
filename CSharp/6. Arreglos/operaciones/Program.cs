Console.WriteLine("---Operaciones con arreglos");
Console.WriteLine("------Operaciones Insercion");

// Insercion en posicion especifica
List<String> productos = new List<string> {"teclado" , "mouse" , " laptop"};
productos.Insert(1, "parlantes");
Console.WriteLine(string.Join("," , productos));



//Insercion al Final de la lista
productos.Add("Refrigeradora");
Console.WriteLine(string.Join(" ," , productos));

//Insercion Multiple 
productos.AddRange(new List<string>{"HP" , "Dell" , "Asus" , "Lenovo" , "HP"});
Console.WriteLine(string.Join(" , ", productos));



Console.WriteLine("-------Operaciones de Busqueda");
//Busqueda

if (productos.Contains("HP"))
{
    int posicion = productos.IndexOf("HP");
    Console.WriteLine($"Encontrado en la posicion:{posicion}");
}
else
{
    Console.WriteLine("Producto no encontrado");
}

// Equivalente in
Console.WriteLine($"Contiene el producto HP: {productos.Contains("HP")}");

//Primera posicion
Console.WriteLine($"HP se encuentra en la posicion: {productos.IndexOf("HP")}");

// Cantidad de repeticiones
Console.WriteLine($"Producto HP se repite: {productos.Count(X => X =="HP")} veces");

Console.WriteLine("-------Operaciones de Modificacion");
//Modificacion
productos[5] = " NVidia";
Console.WriteLine(string.Join(" ," , productos));

//Modificacion masiva
List<double> notas = new List<double>{12.9, 14.3, 19.1, 11.49};
for (int i=0; i<notas.Count; i++)
{
    notas[i] = notas[i] + 0.9;
}
Console.WriteLine(String.Join("," , notas));

// Modificacion por segmento
for(int j=0; j<=3; j++)
{
    productos[j]= productos[j].ToUpper();
}
Console.WriteLine(String.Join("," , productos));

// Modificacion Transformacion Masiva
List<double> salarios = new List<double> {2000, 1560, 2700, 4000};
salarios = salarios.Select(salario => salario > 1900? salario * 1.1: salario).ToList();
Console.WriteLine(String.Join("," , salarios));



Console.WriteLine("------Operaciones de Eliminacion");
//Eliminacion de un valor
productos.Remove("Refrigeradora");
Console.WriteLine(String.Join("," , productos));

//Eliminacion por un indice
productos.RemoveAt(1);
Console.WriteLine(String.Join("," , productos));

//Eliminacion por rango
productos.RemoveRange(1,2);
Console.WriteLine(String.Join("," , productos));

//Eliminacion por criterio
List<int> datos = new List<int>{11, 20, 18, 11, 20, 17, 16};
datos.RemoveAll(x=> x == 11);

Console.WriteLine(String.Join("," , datos));

//Vacias Lista
salarios.Clear();

Console.WriteLine(String.Join("," , salarios));

