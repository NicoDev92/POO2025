import numpy as np
from Carrera import Carrera

class Facultad:
  __id: int
  __nombre: str
  __direccion: str
  __localidad: str
  __telefono: str
  __cantidad_carreras: int
  __espacio_arreglo_carreras: int  
  __carreras: None
    
  def __init__(self, id: int, nombre: str, direccion: str, localidad: str, telefono: str, espacio_arreglo: int):
    self.__id = id
    self.__nombre = nombre
    self.__direccion = direccion
    self.__localidad = localidad
    self.__telefono = telefono
    self.__carreras = np.empty(espacio_arreglo, dtype=Carrera)
    self.__espacio_arreglo_carreras = espacio_arreglo
    self.__cantidad_carreras = 0
    
  #agregar carrera
  def agregar_carrera(self, nueva_carrera: Carrera):
    if self.__cantidad_carreras == self.__espacio_arreglo_carreras:
      self.__espacio_arreglo_carreras += 5
      nuevo_arreglo = np.empty(self.__espacio_arreglo_carreras, dtype=Carrera)
      for i in range(self.__cantidad_carreras):
        nuevo_arreglo[i] = self.__carreras[i]
      self.__carreras = nuevo_arreglo

    self.__carreras[self.__cantidad_carreras] = nueva_carrera
    self.__cantidad_carreras += 1

        
  #obtener cantidad de carreras
  def get_cantidad_carreras(self):
    return self.__cantidad_carreras
    
  def __str__(self):
    return f"{self.__nombre} - {self.__localidad}"
      
  # Getters
  def get_id(self):
    return self.__id
    
  def get_nombre(self):
    return self.__nombre
    
  def get_direccion(self):
    return self.__direccion
    
  def get_localidad(self):
    return self.__localidad
    
  def get_telefono(self):
    return self.__telefono
    
  def get_carreras(self):
    return self.__carreras