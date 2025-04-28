from Facultad import Facultad
from Carrera import Carrera
import numpy as np
import os
import csv

class ManejadorFacultad:
  __facultades : None
  __cantidad_facultades : int
  __espacio_arreglo : int
  
  def __init__(self, cantidad_facultades):
    self.__facultades = np.empty(cantidad_facultades, dtype=Facultad)
    self.__espacio_arreglo = cantidad_facultades
    self.__cantidad_facultades = 0
  
  def agregar_facultad(self, nueva_facultad: Facultad):
    if self.__cantidad_facultades == len(self.__facultades):
        self.__espacio_arreglo += 5
        nuevo_arreglo = np.empty(self.__espacio_arreglo, dtype=Facultad)
        
        for i in range(self.__cantidad_facultades):
          nuevo_arreglo[i] = self.__facultades[i]
        
        self.__facultades = nuevo_arreglo
      
    self.__facultades[self.__cantidad_facultades] = nueva_facultad
    self.__cantidad_facultades += 1
  
  def get_facultades(self):
    return self.__facultades

  def buscar_facultad_por_codigo(self, codigo : int):
    encontrado = False
    i = 0
    facultad = None
    
    while not encontrado and i < self.__cantidad_facultades:
      if self.__facultades[i].get_id() == codigo:
        facultad = self.__facultades[i]
        encontrado = True
      i += 1
    return facultad
  
  def buscar_facultad_por_nombre(self, nombre : str):
    encontrado = False
    i = 0
    facultad = None
    
    while not encontrado and i < self.__cantidad_facultades:
      if self.__facultades[i].get_nombre().lower() == nombre.lower():
        facultad = self.__facultades[i]
        encontrado = True
      i += 1
    return facultad
  
  def __lector_archivos(self, nombre_archivo : str, separador=","):
    lector = None
    archivo = None
    if nombre_archivo != "" and separador != "":
      ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)
      archivo = open(ruta_archivo, mode="r", encoding="latin-1")
      lector = csv.reader(archivo, delimiter=separador)
    respuesta = {"lector": lector, "archivo":archivo}
    return respuesta

  def cargar_desde_archivo(self):
    datos_facultades = self.__lector_archivos("Facultades.csv", ";")
    datos_carreras = self.__lector_archivos("Carreras.csv", ";")
    
    archivo_facultades = datos_facultades["archivo"]
    archivo_carreras = datos_carreras["archivo"]
    
    lector_facultades = datos_facultades["lector"]
    lector_carreras = datos_carreras["lector"]
    
    next(lector_facultades)
    next(lector_carreras)
    
    carreras = []

    for fila_carrera in lector_carreras:
      carreras.append(fila_carrera)
    print(f"Largo de lector {(lector_facultades)}")
    for fila_facultad in lector_facultades:
      nueva_facultad = Facultad(int(fila_facultad[0]), fila_facultad[1], fila_facultad[2], fila_facultad[3], fila_facultad[4], 1)
      for fila_carrera in carreras:
        if fila_carrera[5] == fila_facultad[0]:
          nueva_carrera = Carrera(int(fila_carrera[0]), fila_carrera[1], "",fila_carrera[3],fila_carrera[2],int(fila_carrera[5]))
          nueva_facultad.agregar_carrera(nueva_carrera)
      self.agregar_facultad(nueva_facultad)

    archivo_facultades.close()
    archivo_carreras.close()

  def calcular_cantidad_carreras(self):
    detalle_facultad = {"facultad": "", "cantidad_carreras" : 0}
    resultados = []
    for i in range(self.__cantidad_facultades):
      detalle_facultad = {"facultad": self.__facultades[i].get_nombre(),
                          "cantidad_carreras": self.__facultades[i].get_cantidad_carreras()}
      resultados.append(detalle_facultad)
    return resultados
  
  def listar_carreras_alfabeticamente(self, nombre_facultad: str):
    facultad = self.buscar_facultad_por_nombre(nombre_facultad)
    carreras = []
    if facultad is not None:
      aux_carreras = facultad.get_carreras()
      for carrera in aux_carreras:
        if carrera is not None:
          carreras.append(carrera)
      carreras.sort()
    return carreras
