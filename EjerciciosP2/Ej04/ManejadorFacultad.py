import numpy as np
from Facultad import Facultad

class ManejadorFacultad:
  __facultades : None
  __cantidad_facultades : int
  __espacio_arreglo : int
  
  def __init__(self, cantidad_facultades):
    self.__facultades = np.empty(cantidad_facultades, dtype=Facultad)
    self.__cantidad_facultades = cantidad_facultades
    self.__espacio_arreglo = cantidad_facultades
  
  def agregar_facultad(self, nueva_facultad: Facultad):
    if self.__cantidad_facultades == len(self.__facultades):
        self.__espacio_arreglo += 5
        nuevo_arreglo = np.empty(self.__espacio_arreglo, dtype=Facultad)
        
        for i in range(self.__cantidad_facultades):
            nuevo_arreglo[i] = self.__facultades[i]
        
        self.__facultades = nuevo_arreglo
      
    self.__facultades[self.__cantidad_facultades] = nueva_facultad
    self.__cantidad_facultades += 1
  
  def mostrar_cantidad_carreras(self):
    for i in range(self.__cantidad_facultades):
      print(f"{self.__facultades[i].get_nombre()} tiene {self.__facultades[i].get_cantidad_carreras()}")
  
  def mostrar_carreras_alf(self, nombre_facultad: str):
    encontrado = False
    i = 0
    while not encontrado and i < self.__cantidad_facultades:
      if self.__facultades[i].get_nombre().lower() == nombre_facultad.lower():
        encontrado = True
        carreras = self.__facultades[i].get_carreras()
        carreras_ordenadas = sorted(carreras)
        print(f"\nCarreras de la facultad {nombre_facultad} (orden alfabético):")
        for carrera in carreras_ordenadas:
          print(carrera)  # Esto usa el método __str__ de la clase Carrera
      i += 1
    
    if not encontrado:
        print(f"No se encontró la facultad: {nombre_facultad}")