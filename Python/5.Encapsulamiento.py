# restringir accesos a campos o valores
class CtaAhorro:
    def __init__(self, Titular, SaldoInicial):
        self.Titular = Titular #publico
        self.__saldo = SaldoInicial # restringido

    def depositar(self, monto):
        if (monto > 0):
            self.__saldo += monto # nuevo saldo restringido

    def mostrar_saldo(self):
        print(f'Titular: {self.Titular}')
        print(F'Saldo: {self.__saldo:.2f}') #restringido


cuenta = CtaAhorro("Raquel",1500)
cuenta.depositar(500)
cuenta.mostrar_saldo()