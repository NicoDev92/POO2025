import csv
import os
from Departamento import Departamento

class ManejadorDepartamentos:
  __departamentos = list
  
  def __init__(self):
    self.__departamentos = []

  def agregar_departamento(self, nuevo_dpto):
    self.__departamentos.append(nuevo_dpto)

  def cargar_desde_archivo(self):
    ruta = os.path.join(os.path.dirname(__file__), "Departamentos.csv")
    archivo = open(ruta, mode='r')
    lector = csv.reader(archivo, delimiter=';')
    next(lector)
    for fila in lector:
      departamento = Departamento(int(fila[0]), fila[1])
      self.agregar_departamento(departamento)
    archivo.close()

  def get_departamento_por_id(self, id_dep: int):
    for departamento in self.__departamentos:
      if departamento.get_id() == id_dep:
        return departamento

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
