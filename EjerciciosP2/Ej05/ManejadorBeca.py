from Beca import Beca
import csv
import os

class ManejadorBeca:
  __becas : list
  
  def __init__(self):
    self.__becas = []
  
  def agregar_beca(self, nueva_beca : Beca):
    self.__becas.append(nueva_beca)
    
  def get_lista_becas(self):
    return self.__becas
  
  def cargar_desde_archivo(self, nombre_archivo : str, separador = ","):
    if nombre_archivo is not "" and separador is not "":
      ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
      archivo = open(ruta, mode="r")
      lector = csv.reader(archivo, delimiter=separador)
      
      next(lector)
      
      for fila in lector:
        beca = Beca(int(fila[0]), fila[1], float(fila[2]))
        self.agregar_beca(beca)
      archivo.close()
    
  def test(self):
    self.cargar_desde_archivo("becas.csv", ";")
    