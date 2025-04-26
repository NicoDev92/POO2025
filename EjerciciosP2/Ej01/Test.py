from TarjetaSube import TarjetaSube

def Test():
	tarjetas = []
	for i in range(3):
		print(f"\n=Ingreso de datos para la tarjeta {i+1}:")
		numero = int(input("Ingrese número de tarjeta: "))
		saldo = int(input("Ingrese saldo inicial: "))
		tarjeta = TarjetaSube(saldo, numero)
		tarjetas.append(tarjeta)

	for i in range(len(tarjetas)):
		print(f"\n--- Pruebas para la tarjeta {i+1} ---")
		print(f"Número de tarjeta: {tarjetas[i].get_numero()}")
		print(f"Saldo actual: ${tarjetas[i].get_saldo()}")

		carga = int(input("Ingrese un monto a cargar: "))
		tarjetas[i].cargar_saldo(carga)

		pasaje = int(input("Ingrese el costo de un pasaje para pagar: "))
		tarjetas[i].pagar_pasaje(pasaje)