


using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Actividad_N2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            for (int i = 0; i < 3; i++)
            {
                Console.Beep(1000,900);
                Console.Clear();//Limpiar consola
                RegistrarDatos();
                Console.ReadKey();
            }
           

            }//Funcion 1
            static void RegistrarDatos()
            {
                Console.WriteLine("Ingresa tu nombre por favor");
                string nombre = Console.ReadLine();

                Console.WriteLine("Ahora ingrese su edad por favor");
                int edad = int.Parse(Console.ReadLine());
                DeterminarDatos(edad);
            }
            //Funcion 2
            static void DeterminarDatos(int edad)
            {
                if (edad >= 18)
                {
                    Console.WriteLine("Eres mayor de edad");
                }
                else
                {
                    Console.WriteLine("No eres mayor de edad");
                }
            Console.ReadKey();
            }


        }
 }