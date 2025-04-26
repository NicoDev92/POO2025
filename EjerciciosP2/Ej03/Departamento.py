
class Departamento:
  __id : int
  __nombre : str
  def __init__(self, id_dep: int, nombre: str):
    self.__id = id_dep 
    self.__nombre = nombre

  def get_id(self):
    return self.__id

  def get_nombre(self):
    return self.__nombre

  def __str__(self):
    cadena = f"ID:{self.__id} Nombre: {self.__nombre}"
    return cadena