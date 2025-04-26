import csv
import os
from Departamento import Departamento

class ManejadorDepartamentos:
  __departamentos = list
  
  def __init__(self):
    self.__departamentos = []

  def agregar_departamento(self, nuevo_dpto : Departamento):
    if isinstance(nuevo_dpto, Departamento):
      self.__departamentos.append(nuevo_dpto)
    else:
      print(f"No se puede agregar un objeto {type(nuevo_dpto)}")


  def cargar_desde_archivo(self):
    ruta = os.path.join(os.path.dirname(__file__), "Departamentos.csv")
    archivo = open(ruta, mode='r')
    lector = csv.reader(archivo, delimiter=';')
    next(lector)
    for fila in lector:
      departamento = Departamento(int(fila[0]), fila[1])
      self.agregar_departamento(departamento)
    archivo.close()

  def get_departamento_por_id(self, id_depto: int):
    encontrado = False
    i = 0
    depto_encontrado = None
    
    while not encontrado and i < len(self.__departamentos):
      if self.__departamentos[i].get_id() == id_depto:
        depto_encontrado = self.__departamentos[i]
        encontrado = True
      i += 1
    return depto_encontrado

  def get_departamento_por_nombre(self, nombre_buscado: str):
    departamento = None
    encontrado = False
    i = 0
    
    while not encontrado and i < len(self.__departamentos):
      if nombre_buscado.lower() == self.__departamentos[i].get_nombre().lower():
        departamento = self.__departamentos[i]
        encontrado = True
      i += 1
    return departamento


  def get_lista(self):
    return self.__departamentos

  def test(self):
    self.cargar_desde_archivo()
