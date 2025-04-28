class Carrera:
  __codigo_carrera: int
  __nombre: str
  __fecha_inicio: str
  __duracion: str
  __titulo_otorgado: str
  __id_facultad: int
    
  def __init__(self, codigo_carrera: int, nombre: str, fecha_inicio: str, duracion: str, titulo_otorgado: str, id_facultad: int):
    self.__codigo_carrera = codigo_carrera
    self.__nombre = nombre
    self.__fecha_inicio = fecha_inicio
    self.__duracion = duracion
    self.__titulo_otorgado = titulo_otorgado
    self.__id_facultad = id_facultad
    
  def get_codigo_carrera(self):
    return self.__codigo_carrera
    
  def get_nombre(self):
    return self.__nombre
    
  def get_fecha_inicio(self):
    return self.__fecha_inicio
    
  def get_duracion(self):
    return self.__duracion
    
  def get_titulo_otorgado(self):
    return self.__titulo_otorgado
    
  def get_id_facultad(self):
    return self.__id_facultad
    
  def __lt__(self, otra):
    return self.__nombre.lower() < otra.__nombre.lower()
    
  def __str__(self):
    return f"{self.__nombre} - Duración: {self.__duracion}"