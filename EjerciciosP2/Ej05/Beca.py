
class Beca:
  __id_beca : int
  __tipo_beca : str
  __importe : float

  def __init__(self, id_beca, tipo_beca, importe):
    self.__id_beca = id_beca
    self.__tipo_beca = tipo_beca
    self.__importe = importe

  def get_id(self):
    return self.__id_beca
  
  def get_tipo_beca(self):
    return self.__tipo_beca
  
  def get_importe(self):
    return self.__importe
  
  def __str__(self):
    cadena = f"Beca de: {self.__tipo_beca}, importe mensual: {self.get_importe}"
