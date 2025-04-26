from ManejadorTarjetaSube import ManejadorTarjetaSube
from TarjetaSube import TarjetaSube
def main():
  un_manejador = ManejadorTarjetaSube()
  un_manejador.test()
  
  nro_nueva_tarjeta = int(input("Escriba el numero de la nueva tarjeta: "))
  saldo_nueva_tarjeta = int(input("Escriba el saldo de la nueva tarjeta: "))
  nueva_tarjeta = TarjetaSube(saldo_nueva_tarjeta, nro_nueva_tarjeta)
  un_manejador.agregar_tarjeta(nueva_tarjeta)
  
  result = un_manejador.buscar_por_nro_tarjeta(int(input("ingrese la tarjeta a buscar")))
  if result is not None:
    print(f"= El saldo de la tarjeta es {result}")
  else:
    print("Numero no encontrado")
  
  un_manejador.mostrar_saldo_negativo()
  
if __name__ == "__main__":
  main()
