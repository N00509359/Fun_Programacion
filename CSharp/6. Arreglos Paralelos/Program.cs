Console.WriteLine("Arreglos Paralelos");
// Estructuras separadas que almacenan datos de distintos tipos pero relacionados

//Sintaxis
string[] nombres = {"Maria", "Diana", "José", "Luis"};
int[] edades = {37, 42, 25, 18};
//Combinar mostrar nombre y edad recorrer ambos arreglos
for (int i=0; i<nombres.Length; i++){
    Console.WriteLine($"Nombre: {nombres[i]} - Edad: {edades[i]}");
}

//Correspondencia por indice
int indice=1;
Console.WriteLine($"Nombre: {nombres[indice]}");
Console.WriteLine($"Edad: {edades[indice]}");

//Coherencia
if (nombres.Length == edades.Length){
    Console.WriteLine("Las Estructuras son Conherentes");
}
else {
    Console.WriteLine("Las Estructuras NO son Coherentes");
}

Console.WriteLine("Estructuras Combinadas");
// Utilizar Objetos almacenar distintos tipos de datos en un mismo arreglo
object[] personas = {44444444, "Esperanza", 37};
Console.WriteLine($"DNI: {personas[0]}");
Console.WriteLine($"Nombre: {personas[1]}");
Console.WriteLine($"Edad: {personas[2]}");

Console.WriteLine("Uso de Diccionarios");
//Almacenar datos asociados mediante claves, recuperar por nombre y no solo posicion
Dictionary<string, object> estudiantes = new Dictionary<string, object>();
estudiantes["Codigo"] = "N0001";
estudiantes["Nombre"] = "Juan Perez";
estudiantes["Nota"] = 18.5;

Console.WriteLine($"Codigo: {estudiantes["Codigo"]}");
Console.WriteLine($"Nombre: {estudiantes["Nombre"]}");
Console.WriteLine($"Nota: {estudiantes["Nota"]}");

Console.WriteLine("Usando Clases");
Estudiante est = new Estudiante();
est.codigo= "N007";
est.nombre="Juan P.";
est.nota= 14.55;

Console.WriteLine($"{est.codigo} {est.nombre} {est.nota}");
public class Estudiante{
    public string nombre;
    public string codigo;
    public double nota;
}