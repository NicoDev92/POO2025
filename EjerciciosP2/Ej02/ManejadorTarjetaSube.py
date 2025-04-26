from TarjetaSube import TarjetaSube

class ManejadorTarjetaSube:
  __tarjetas : list

  def __init__(self):
    self.__tarjetas = []
  
  def agregar_tarjeta(self, nueva_tarjeta : TarjetaSube):
    if isinstance(nueva_tarjeta, TarjetaSube):
      self.__tarjetas.append(nueva_tarjeta)
    else:
      print("El elemento a agregar no es del tipo Tarjeta SUBE")

  def mostrar_saldo_negativo(self):
    print("= Tarjetas SUBE con saldo negativo =")
    for i in range(len(self.__tarjetas)):
      if self.__tarjetas[i].get_saldo() < 0:
        print(self.__tarjetas[i])
  
  def buscar_por_nro_tarjeta(self, nro_buscado : int):
    encontrado = False
    i = 0
    saldo = None
    while not encontrado and i < len(self.__tarjetas):
      if self.__tarjetas[i].get_numero() == nro_buscado:
        saldo = self.__tarjetas[i].get_saldo()
        encontrado = True
      i += 1
    return saldo

  def test(self):
    for i in range(3):
      print(f"{i+1} -Ingrese los datos:")
      numero = int(input("Ingrese el numero de la tarjeta : "))
      saldo = int(input("Ingrese el saldo de la targeta : "))
      tarjeta = TarjetaSube(saldo, numero)
      self.__tarjetas.append(tarjeta)

