Console.WriteLine(" Arreglos Unidimensionales ");

// Declarando arreglos

int [] numeros = new int[10]; // 10 elementos
numeros[1]=26; // inserta en la posicion 1  el valor 26
numeros[9]=11; // Inserta en la posicion 9 el valor 11

//Mostrar el arreglo
Console.WriteLine(string.Join("," , numeros));

// Declarar un arreglo de nombres

string[] nombres = new string [5];
nombres[0] = "Juan";
nombres[4] = "Susana";
Console.WriteLine(string.Join(", ", nombres));

// Elemento e indice de un arreglo
Console.WriteLine($"Cantidad Elementos: {numeros.Length}");
Console.WriteLine($"Ultimo Elemento: {numeros[numeros.Length - 1]}");

// El valor en un indice especifico

Console.WriteLine($"Nombre en la posicion 4 es: {nombres[4]}");
Console.WriteLine($"Numero en la posicion 9 es: {numeros[9]}");


// Recorrer el arreglo 

for (int i=0; i < numeros.Length; i++)
{
    Console.WriteLine($"Posicion {i}: Valor: {numeros[i]}");
}

for ( int j=0; j< nombres.Length; j++)
{
    Console.WriteLine($"Posicion {j}: Valor: {nombres[j]}");
}


//Declarar arreglo Bidimensional (Matriz)

int [,] notas =
{
    {1,2,3,4}, //Arreglos 
    {5,6,7,8}, //Arreglo 2
    {9,10,11,12}, //Arreglo 3
};

// Mostrar elemento fila 1 columna 3 ( debe mostrar el numero 8)
Console.WriteLine(notas[1,3]);

// Recorre la matriz

for (int filas=0; filas < notas.GetLength(0); filas++)
{
    for (int col=0; col< notas.GetLength(1); col++)
    {
        Console.WriteLine($"Fila: {filas}, Columna: {col} - Valor: {notas[filas, col]}");
    }
}
