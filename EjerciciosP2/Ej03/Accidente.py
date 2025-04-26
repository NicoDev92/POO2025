from ManejadorDepartamentos import ManejadorDepartamentos

class Accidente:
  __matriz : list
  
  def __init__(self):
    self.__matriz =[]
  
  def inicializar(self, filas = 12, columnas = 19):
    self.__matriz = []
    for i in range(columnas):
        fila = [0] * filas
        self.__matriz.append(fila)

  def get_matriz(self):
    return self.__matriz

  def registrar_accidente(self, dep, mes, cantidad):
    if (dep <= 19) and (dep > 0) and (mes <= 12) and (mes > 0):
      self.__matriz[dep - 1][mes - 1] += cantidad
    else:
      print("departamento o mes incorrecto")

  def total_por_mes(self, mes: int):
    if (mes <= 12) and (mes > 0):
        resultados = []
        for i in range(19):
            resultados.append(self.__matriz[i][mes - 1])
    return resultados

  def mayor_accidentes_en_mes(self, mes):
    if (mes <= 12) and (mes > 0):
      max_acc = -1
      id_max = -1
      result = "No hay resultados para la consulta"
      for i in range(19):
        if self.__matriz[i][mes - 1] > max_acc:
          max_acc = self.__matriz[i][mes - 1]
          id_max = i + 1
      if id_max > -1:
        md = ManejadorDepartamentos()
        md.cargar_desde_archivo()
        departamento = md.get_departamento_por_id(id_max)
        result = (f"Dpto.: {departamento}, cant. Accidentes: {max_acc}")
      return result

  def total_anual_por_departamento(self, nombre_departamento : str):
    md = ManejadorDepartamentos()
    md.cargar_desde_archivo()
    departamento = md.get_departamento_por_nombre(nombre_departamento)
    result = "No se encontro el departamento"
    if departamento is not None:
        result = (f"{departamento.get_nombre()}, cant. accidentes.:{sum(self.__matriz[departamento.get_id()-1])}")
    return result
