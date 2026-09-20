Console.WriteLine("Encapsulamiento");
// Restringir acceso a campos o valores

CtaAhorro cuenta = new CtaAhorro("Raquel",1500.00m );
cuenta.depositar(500);
cuenta.mostrar_saldo();

public class CtaAhorro
{
    public string titular;

    private decimal saldo;
    public CtaAhorro(string Titular, decimal SaldoInicial)
    {
        this. titular = Titular;
        this. saldo = SaldoInicial;
    }
    public void depositar(decimal monto)
    {
        if (monto > 0)
        {
            saldo += monto;
        }
    }
    public void mostrar_saldo()
    {
        Console.WriteLine($"Titular: {titular}");
        Console.WriteLine($"Saldo: {saldo:F2}");
    }
}
