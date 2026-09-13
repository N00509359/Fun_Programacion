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
            Console.WriteLine("Ingrese su edad: ");
            int edad = int.Parse(Console.ReadLine());
            Console.WriteLine($"Nombre: {nombre}, Edad: {edad}");

            // Condicionales
            // Simple
            if (edad < 18) {
                Console.WriteLine("Eres menor de edad");
            }

            // Doble
            if (edad >= 18){
                Console.WriteLine("Eres mayor de edad");
            }
            else {
                Console.WriteLine("Eres menor de edad");
            }

            // Condicional Multiple
            Console.WriteLine("Ingrese un numero del 1 al 3: ");
            int opcion = int.Parse(Console.ReadLine());
            switch (opcion) {
                case 1: Console.WriteLine("Opcion 1"); break;
                case 2: Console.WriteLine("Opcion 2"); break;
                case 3: Console.WriteLine("Opcion 3"); break;
                default: Console.WriteLine("Opcion Invalida"); break;
            }

            // Condicional Anidado
            if (opcion == 1) {
                Console.WriteLine("Eligio Opcion 1");
            }
            else if (opcion == 2) {
                Console.WriteLine("Eligio Opcion 2");
            }
            else {
                Console.WriteLine("Eligio Opcion 3");
            }

            // Repetitivos
            // For
            for (int i = 0; i < 10; i++) {
                Console.Write($"Numero: {i}");
            }
            // While
            int contador = 1;
            while (contador <= 3) { 
                Console.WriteLine($"Intento:{contador}");
                contador ++;
            }


            // Do While
            int contador2 = 1;
            do {
                Console.WriteLine($"Intento: {contador2}");
                contador2 ++;
            } while (contador2<=3);

        }
    }
}