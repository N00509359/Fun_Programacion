using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace estructuras_control
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("estructuras de control");

            // Secuencial
           
            Console.WriteLine("Ingrese su nombre: ");
            string nombre = Console.ReadLine();
            Console.WriteLine("ingrese su edad:  ");
            int edad = int.Parse(Console.ReadLine());
            Console.WriteLine($"Nombre: {nombre}, edad: {edad}");
            // Condicionales
            //simple
            if (edad < 18)
            { 
                Console.WriteLine("ERES MAYOR DE EDAD"); 
            }
             // doble
             if (edad >=18)
            { 
                Console.WriteLine("Eres menor de edad");
             else 
                { 
                  Console.WriteLine("eres menor de edad");
                }
                // condicional multiple
                Console.WriteLine("Ingrese un numero del 1 al 3");
                switch (opcion)
                {
                    case 1: Console.WriteLine("opc 1");
                    case 2: Console.WriteLine("opc 2");
                    case 2: Console.WriteLine("opc 3");
                    default: Console.WriteLine("Opcion Invalida");
                        break;

                }
                // condicional anidado
                if (opcion == 1)
                {
                    Console.WriteLine("eligio opc 1");

                }
                else if (opcion == 2) { Console.WriteLine("eligio opc 2");
                }
                else
                {
                    Console.WriteLine("eligio la opc 3");

                }
                // Repetitivas
                // for
                for (int i = 0; i < edad; i++) {
                    Console.WriteLine($"numero: {i}");
                }
                // while
                int contador = 1;
                while (contador <=3)
                {
                    Console.WriteLine($"intento: {contador}");
                    contador++;

                }
                // do while
                int contador2 = 1;
        }
    }
}
