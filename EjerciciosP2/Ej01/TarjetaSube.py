
class TarjetaSube:
  __saldo: int
  __numero: int
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
    self.__saldo += importe
    return self.__saldo

  def pagar_pasaje(self, importe: int):
    self.__saldo -= importe
    return self.__saldo
