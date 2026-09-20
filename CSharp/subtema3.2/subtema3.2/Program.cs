using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

namespace subtema3._2
{

    internal class Program
    {
        static string[] ListaAlumnos = new string[4];//variable de clase
        static void Main(string[] args)
        {
            insertar();
            mostrar();
            Console.WriteLine("ingrese alumno a buscar: ");
            string alumno = Console.ReadLine();
            buscar(alumno);
            reemplazar();
            Console.WriteLine("ingrese alumno a ELIMINAR: ");
            String alumnoELIMINAR = Console.ReadLine();
            eliminar(alumnoELIMINAR);
        }
        static void insertar()
        {
            for (int i = 0; i < ListaAlumnos.Length; i++)
            {
                //i=1 , i<4;i++
                Console.Write("ingrese nombres y apellidos: ");
                ListaAlumnos[i] = Console.ReadLine();
            }
        }
        static void mostrar()
        {

            for (int i = 0; i < ListaAlumnos.Length; i++)
            {

                Console.Write("alunmo: " + ListaAlumnos[i]);

            }

        }
        static void buscar(string nombreAbuscar)
        {
            bool encontrado = false;
            for (int i = 0; i < ListaAlumnos.Length; i++)
            {
                if (nombreAbuscar == ListaAlumnos[i])
                {
                    Console.WriteLine("ENCONTRADO!");
                    Console.WriteLine("alumno: " + ListaAlumnos[i]);
                    encontrado = true;
                    return;//retorno a la funcion que lo invoco
                }
                if (encontrado == false)
                {
                    Console.WriteLine("Alumno encontrado: ");
                }
            }

        }
        static void reemplazar() { }
        static void eliminar(string nombreAbuscar)
        {
            bool encontrado = false;
            for (int i = 0; i < ListaAlumnos.Length; i++)
            {
                if (nombreAbuscar == ListaAlumnos[i])
                {
                    for (int j = i; j < ListaAlumnos.Length-1; j++) {
                        ListaAlumnos[j] = ListaAlumnos[j + 1];
                    }
                    ListaAlumnos[ListaAlumnos.Length - 1]=null;
                    Console.Write("Alumno eliminado: " + nombreAbuscar);
                }
                if (encontrado == false)
                {
                    Console.WriteLine("Alumno encontrado: ");
                }
            }
        }
    }
}

