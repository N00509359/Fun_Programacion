//clase modelo que representa una cancion de la playlist
public class Cancion
{
    //Propiedades de la cancion
    public string Titulo { get; set; }
    public string Artista { get; set; }
    public int DuracionSegundos { get; set; }

    //constructor : inicializar una cancion con sus datos // el constructor es el mismo de la clase en este caso cancion
    public Cancion(string titulo, string artista, int duracionSegundos)
    {
        Titulo = titulo;
        Artista = artista;
        DuracionSegundos= duracionSegundos;
    }
    // sobreescribir ToString para mostrar la cancion
    //cuando se agrege una cancion a listbox
    public override string ToString()
    {
        int minutos = DuracionSegundos/60;
        int segundos = DuracionSegundos%60;
        return $"{Titulo}-{Artista}({minutos}:{segundos:D2})";
    }

  
}