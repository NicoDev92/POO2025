import os
import csv
from Beneficiario import Beneficiario
from ManejadorBeca import ManejadorBeca

class ManejadorBeneficiario:
  __beneficiarios : list
  
  def __init__(self):
    self.__beneficiarios = []

  def agregar_beneficiario(self, nuevo_beneficiario : Beneficiario):
    self.__beneficiarios.append(nuevo_beneficiario)

  def get_beneficiarios(self):
    return self.__beneficiarios
  
  def cargar_desde_archivo(self, nombre_archivo : str, separador = ","):
    if nombre_archivo is not "" and separador is not "":
      ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
      archivo = open(ruta, mode="r")
      lector = csv.reader(archivo, delimiter=separador)
      
      next(lector)
      
      for fila in lector:
        beneficiario = Beneficiario(fila[0], fila[1], fila[2], fila[3], fila[4], int(fila[5]),float(fila[6]), int(fila[7]))
        self.agregar_beneficiario(beneficiario)
      archivo.close()
  
  def buscar_beneficiarios_tipo_beca(self, tipo_beca : str):
    resultados = []
    becas = ManejadorBeca.get_lista_becas()
    i = 0
    encontrado = False
    
    while not encontrado and i < len(becas):
      if tipo_beca.lower() == becas[i].get_tipo_beca().lower():
        encontrado = True
      i += 1
    
    for beneficiario in self.__beneficiarios:
      if beneficiario.get_id_beca() == i:
        resultados.append(beneficiario)
    
    return resultados
  
  def buscar_beneficiarios_tipo_beca(self, tipo_beca : str, manejador_becas : ManejadorBeca):
    resultados = []
    id_beca = None
    importe_total = 0.0
    lista_becas = manejador_becas.get_lista_becas()
    encontrado = False
    i = 0
    while not encontrado and i < len(lista_becas):
      if lista_becas[i].get_tipo_beca().lower() == tipo_beca.lower():
        id_beca = lista_becas[i].get_id()
        importe_beca = lista_becas[i].get_importe() 
      i += 1
      
    if id_beca is not None:
      for beneficiario in self.__beneficiarios:
        if beneficiario.get_id_beca() == id_beca:
          resultados.append(beneficiario)
          importe_total += importe_beca

    return {"lista_alumnos":resultados, "importe":importe_total}
  
  def obtener_beneficiario_por_dni(self, dni_buscado : str):
    encontrado = False
    i = 0
    beneficiario = None
    while not encontrado and i < len(self.__beneficiarios):
      if self.__beneficiarios[i].get_dni() == dni_buscado:
        beneficiario = self.__beneficiarios[i]
      i += 1
    return beneficiario
  
  def multiples_becas_por_dni(self, dni_buscado : str):
    encontrado = 0
    beneficiario = None
    for beneficiario in self.__beneficiarios:
      if beneficiario.get_dni() == dni_buscado:
        encontrado += 1
    if encontrado > 1:
      beneficiario = self.obtener_beneficiario_por_dni(dni_buscado)
    return beneficiario
  
  def __listar_promedio_mayor_que(self, promedio : float):
    resultados = []
    for beneficiario in self.__beneficiarios:
      if beneficiario.get_promedio() > promedio:
        resultados.append(beneficiario)
    return resultados

  def obtener_estudiantes_sin_ayuda_economica(self, id_beca : int, promedio = 8.0 ):
    resultados = []
    estudiantes = self.__listar_promedio_mayor_que(promedio)
    for estudiante in estudiantes:
      if estudiante.get_id_beca() != id_beca:
        resultados.append(estudiante)
    return resultados
  
  def test(self):
    self.cargar_desde_archivo("beneficiarios.csv", ";")