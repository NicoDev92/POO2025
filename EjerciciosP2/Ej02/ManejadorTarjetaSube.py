from TarjetaSube import TarjetaSube

class ManejadorTarjetaSube:
    def __init__(self):
        self.__tarjetas = []

    def agregar_tarjeta(self, una_tarjeta: TarjetaSube):
        if isinstance(una_tarjeta, TarjetaSube):
            self.__tarjetas.append(una_tarjeta)
        else:
            print("Error: Solo se pueden agregar objetos de tipo TarjetaSube.")

    def mostrar_tarjetas_saldo_negativo(self):
        print("\nTarjetas con saldo negativo:")
        for i in range(len(self.__tarjetas)):
            if self.__tarjetas[i].get_saldo() < 0:
                print(f"→ Número de tarjeta: {self.__tarjetas[i].get_numero()}")

    def test(self):
        for i in range(3):
            print(f"\n=Ingreso de datos para la tarjeta {i+1} ===")
            numero = int(input("Ingrese número de tarjeta: "))
            saldo = int(input("Ingrese saldo inicial: "))
            tarjeta = TarjetaSube(saldo, numero)
            self.agregar_tarjeta(tarjeta)

        for i in range(len(self.__tarjetas)):
            print(f"\n--- Pruebas para la tarjeta {i+1} ---")
            print(f"Número de tarjeta: {self.__tarjetas[i].get_numero()}")
            print(f"Saldo actual: ${self.__tarjetas[i].get_saldo()}")

            carga = int(input("Ingrese un monto a cargar: "))
            self.__tarjetas[i].cargar_saldo(carga)

            pasaje = int(input("Ingrese el costo de un pasaje para pagar: "))
            self.__tarjetas[i].pagar_pasaje(pasaje)

        self.mostrar_tarjetas_saldo_negativo()
