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
  
  def agregar_carrera(self, carrera: Carrera):
    if self.__cantidad_carreras == len(self.__carreras):
      self.__espacio_arreglo += 5
      nuevo_arreglo = np.empty(self.__espacio_arreglo, dtype=Carrera)
      
  
  def cargar_desde_archivo(self, archivo, manejador_facultad: ManejadorFacultad):
    try:
      f = open(archivo, 'r', encoding='utf-8')
      for linea in f:
        datos = linea.strip().split(';')
        if len(datos) >= 6:
          codigo = int(datos[0])
          nombre = datos[1]
          fecha_inicio = datos[2]
          duracion = datos[3]
          titulo = datos[4]
          id_facultad = int(datos[5])
          
          carrera = Carrera(codigo, nombre, fecha_inicio, duracion, titulo, id_facultad)
          self.agregar_carrera(carrera)
          
          facultad = manejador_facultad.buscar_facultad_por_codigo(id_facultad)
          if facultad:
            facultad.agregar_carrera(carrera)
      f.close()
    except IOError:
      print(f"Error al abrir el archivo {archivo}")
  
  def buscar_facultad_por_carrera(self, nombre_carrera, manejador_facultad):
    for i in range(self.__cantidad):
      if self.__carreras[i].get_nombre().lower() == nombre_carrera.lower():
        id_facultad = self.__carreras[i].get_id_facultad()
        facultad = manejador_facultad.buscar_facultad_por_codigo(id_facultad)
        return facultad
    return None
  
  def listar_carreras_por_facultad(self, nombre_facultad, manejador_facultad):
    facultad = manejador_facultad.buscar_facultad_por_nombre(nombre_facultad)
    if facultad:
      carreras = facultad.get_carreras()
      carreras_ordenadas = sorted(carreras)
      for carrera in carreras_ordenadas:
        print(carrera)