using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Fundamentos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Fundamentos de C#");
            Console.WriteLine("Tipos de datos");

            //1. Numero Entero
            int edad = 25;

            //2. Cadena de Texto
            string nombre = "Raquel";

            //3. Numero Decimal
            double precio = 19.99;

            //4. Valor Logico
            bool estado = false;

            //5. Valor Caracter
            char genero = 'M';

            Console.WriteLine("Entrada Salida Comentario");
            
            //Entrada 
            Console.Write("Ingrese su nombre");
            nombre = Console.ReadLine();

            //Salida
            Console.WriteLine($"Hola, {nombre}");

            //Comentario de 1 linea

            /*
             Comentario en Bloque
             */

            //Ejecutar un Programa vs Code
            dotnet run 
            
           
        }
    }
}
