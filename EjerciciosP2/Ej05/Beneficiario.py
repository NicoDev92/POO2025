

class Beneficiario:
  __dni : str
  __nombre : str
  __apellido : str
  __carrera : str
  __facultad : str
  __anio_cursa : int
  __promedio : float
  __id_beca : int
  
  def __init__(self, dni, nombre, apellido, carrera, facultad, anio_cursa, promedio, id_beca):
    self.__dni = dni
    self.__nombre = nombre
    self.__apellido = apellido
    self.__carrera = carrera
    self.__facultad = facultad
    self.__anio_cursa = anio_cursa
    self.__promedio = promedio
    self.__id_beca = id_beca
  
  def get_dni(self):
    return self.__dni

  def get_nombre(self):
      return self.__nombre

  def get_apellido(self):
      return self.__apellido

  def get_carrera(self):
      return self.__carrera

  def get_facultad(self):
      return self.__facultad

  def get_anio_cursa(self):
      return self.__anio_cursa

  def get_promedio(self):
      return self.__promedio

  def get_id_beca(self):
      return self.__id_beca

# SETTERS
  def set_dni(self, dni : str):
      self.__dni = dni

  def set_nombre(self, nombre : str):
      self.__nombre = nombre

  def set_apellido(self, apellido : str):
      self.__apellido = apellido

  def set_carrera(self, carrera : str):
      self.__carrera = carrera

  def set_facultad(self, facultad : str):
    self.__facultad = facultad

  def set_anio_cursa(self, anio_cursa : int):
    self.__anio_cursa = anio_cursa

  def set_promedio(self, promedio :float):
    self.__promedio = promedio

  def set_id_beca(self, id_beca : int):
    self.__id_beca = id_beca

  def __str__(self):
    cadena = f"Nombre completo: {self.__apellido}, {self.__nombre} Carrera: {self.__carrera}"
    return cadena
  
  def __gt__(self, otro):
    return self.__facultad > otro.get_facultad()