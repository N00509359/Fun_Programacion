using System;
using System.Collections.Generic;
//  Clase generica que implementa una lista circuloare
//Ningun puntero apunta a null
//el ultimo apunta al primero y el primero al ultimo
public class ListaCircular<T> //la clase es un molde ,y su objeto es una instancia
{
    //puntero que apunte a la cabeza
    private NodoCircular<T> cabeza;
    //Contar la cantidad de nodos
    private int count;
    //Propiedades publicas
    public int Count => count;
    public bool EstaVacia => count == 0;
    //Constructor
    public ListaCircular()
    {
        cabeza = null;
        count = 0;
    }
    //,ETODOS DE INSERCION  
    //Agregamos un nodo al final de la lista
    public void AgregarFinal(T dato)
    {
        NodoCircular<T> nuevo = new NodoCircular<T>(dato);
        if (cabeza == null) 
        {
            nuevo.Siguiente = nuevo;
            nuevo.Anterior = nuevo;
            cabeza = nuevo;
        }
        else
        {
            //Insertar antes de la cabeza
            NodoCircular<T> ultimo = cabeza.Anterior;
            nuevo.Siguiente = cabeza;
            nuevo.Anterior= ultimo;
            ultimo.Siguiente= nuevo;
            cabeza.Anterior = ultimo;
        }
        count++;
    }
}