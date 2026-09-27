//Clase que representa un nodo de una lista circular doble
//cada nodo guarde un dato, y dos punteros:siguiente y anterior
//el ultimo nodo. siguiente es la cabeza y viceverza
public class NodoCircular<T>
{
    //Dato almacenado en el nodo (Canciones)
    public T Dato { get; set; }
    //Referencia al nodo anterior
    public NodoCircular<T>Anterior { get; set; }
    //Referencia al nodo siguiente
    public NodoCircular<T>Siguiente { get; set; }
    //constructor
    public NodoCircular(T dato)
    {
        Dato = dato;
        Anterior = null;
        Siguiente = null;
    }
}
