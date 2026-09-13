using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace semana_4
{
    internal class Program
    {
        static int numeropedidos = 0;
        static void Main(string[] args)
        {
            Console.WriteLine("----Mesa 1----");
            MesaActiva();
            Console.WriteLine("----Mesa 2----");
            MesaActiva();
            Console.WriteLine("Total de pedidos hoy:" + numeropedidos);
        }
    static void MesaActiva()
        {
            int subtotalmesa = 0;//variable local
            string producto = " ";//variable local jugo, pan,cafe...
            Console.WriteLine("ingrese los pedidos (´fin´para cerrar mesa): ");
            producto = Console.ReadLine().ToLower();
            //fin == fin (true)
            while (producto!="fin")
            {
                Console.WriteLine("producto: ");
                producto = Console.ReadLine().ToLower();
                RegistrarPerido(producto);
                numeropedidos++; 
            }

            void RegistrarPerido(string productoP)
            {
                string mensaje = "pedido registrado: " + productoP;
                subtotalmesa++;
            }

        }

    }
}
