
class TarjetaSube:
  def __init__(self, saldo: int, numero: int):
    self.__saldo = saldo
    self.__numero = numero

  def get_saldo(self):
    return self.__saldo

  def get_numero(self):
    return self.__numero

  def __str__(self):
    cadena = f"Nro.: {self.__numero}\n Saldo:{self.__saldo}"
    return cadena

  def cargar_saldo(self, importe: int):
    if importe > 0:
      self.__saldo += importe
      print(f"Se cargaron ${importe}. Nuevo saldo: ${self.__saldo}")
    else:
      print("Error: El importe a cargar debe ser positivo.")

  def pagar_pasaje(self, importe: int):
    if self.__saldo >= importe:
      self.__saldo -= importe
      print(f"Pago exitoso. Nuevo saldo: ${self.__saldo}")
      return self.__saldo
    else:
      print("Saldo insuficiente.")
      return -1
