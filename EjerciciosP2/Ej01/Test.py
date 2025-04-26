from TarjetaSube import TarjetaSube
def Test():
  tarjetas = []
  for i in range(3):
    print(f"{i+1} -Ingrese los datos:")
    numero = int(input("Ingrese el numero de la tarjeta : "))
    saldo = int(input("Ingrese el saldo de la targeta : "))
    tarjeta = TarjetaSube(saldo, numero)
    tarjetas.append(tarjeta)
    
  for i in range(len(tarjetas)):
    print(f"\n =Tarjeta: {tarjetas[i]}=")
    print("\nRealizar carga:")
    carga = int(input("Ingrese un monto a cargar : "))
    if carga > 0:
      tarjetas[i].cargar_saldo(carga)
    else:
      print("No se puede cargar monto negarivo")
  
  for i in range(len(tarjetas)):
    print(f"\n =Tarjeta: {tarjetas[i]}=")
    monto = int(input("Monto a pagar : "))
    if monto <= tarjetas[i].get_saldo():
      tarjetas[i].pagar_pasaje(monto)
      print(tarjetas[i])
    else:
      print("Saldo insuficiente")