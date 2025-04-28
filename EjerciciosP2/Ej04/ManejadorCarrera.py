import numpy as np
from Carrera import Carrera
from ManejadorFacultad import ManejadorFacultad

class ManejadorCarrera:
  __carreras: None
  __cantidad_carreras: int
  __espacio_arreglo: int
  
  def __init__(self, cantidad_carreras : int):
    self.__carreras = np.empty(cantidad_carreras, dtype = Carrera)
    self.__cantidad_carreras = cantidad_carreras
    self.__espacio_arreglo = cantidad_carreras
  
  def agregar_carrera(self, nueva_carrera: Carrera):
    if self.__cantidad_carreras == len(self.__carreras):
      self.__espacio_arreglo += 5
      nuevo_arreglo = np.empty(self.__espacio_arreglo, dtype=Carrera)
      
      for i in range(self.__cantidad_carreras):
        nuevo_arreglo[i] = self.__carreras[1]
      self.__carreras = nuevo_arreglo
    self.__carreras[self.__cantidad_carreras] = nueva_carrera
    self.__cantidad_carreras += 1

  
  def buscar_facultad_por_carrera(self, nombre_carrera : str, manejador_facultad : ManejadorFacultad):
    encontrado = False
    i = 0
    facultad = None
    
    while not encontrado and i < len(self.__carreras):
      if self.__carreras[i].get_nombre().lower() == nombre_carrera.lower():
        encontrado = True
        facultad = manejador_facultad.buscar_facultad_por_codigo(self.__carreras[i].get_id_facultad())
      i += 1
    return facultad
  
  def listar_carreras_por_facultad(self, nombre_facultad, manejador_facultad):
    facultad = manejador_facultad.buscar_facultad_por_nombre(nombre_facultad)
    if facultad:
      carreras = facultad.get_carreras()
      carreras_ordenadas = sorted(carreras)
      for carrera in carreras_ordenadas:
        print(carrera)