from ManejadorDepartamentos import ManejadorDepartamentos

class Accidente:
  __matriz : list
  
  def __init__(self):
    self.__matriz =[]
  
  def inicializar(self, filas=12, columnas=19):
    i = 0
    for i in range(columnas):
      fila = []
      j = 0
      for j in range(filas):
        fila.append(0)
      self.__matriz.append(fila)

  def get_matriz(self):
    return self.__matriz

  def registrar_accidente(self, depto : int, mes : int, cantidad : int):
    resultado = -1
    if (depto <= 19) and (depto > 0) and (mes <= 12) and (mes > 0):
      self.__matriz[depto - 1][mes - 1] += cantidad
      resultado = cantidad
    return resultado

  def total_por_mes(self, mes: int):
    if (mes <= 12) and (mes > 0):
        resultados = []
        for i in range(19):
            resultados.append(self.__matriz[i][mes - 1])
    return resultados

  def mayor_accidentes_en_mes(self, mes : int, manejador : ManejadorDepartamentos):
    if (mes <= 12) and (mes > 0):
      max_acc = -1
      id_max = -1
      resultado = None
      for i in range(19):
        if self.__matriz[i][mes - 1] > max_acc:
          max_acc = self.__matriz[i][mes - 1]
          id_max = i + 1
      if id_max > -1:
        departamento = manejador.get_departamento_por_id(id_max)
        resultado = {"departamento": departamento, "accidentes": max_acc}
      return resultado

  def total_anual_por_departamento(self, nombre_departamento : str, manejador : ManejadorDepartamentos):
    departamento = manejador.get_departamento_por_nombre(nombre_departamento)
    resultado = None
    if departamento is not None:
      resultado = {"departamento": departamento, "accidentes_totales": sum(self.__matriz[departamento.get_id()-1])}
    return resultado

  def mostrar_total_por_departamento(self, manejador : ManejadorDepartamentos):
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic" ]
    print("Departamento\t", end="")
    for mes in range(0, 12):
      print(f"\t{meses[mes]}\t", end="")
    print()
      
    for i in range(19):
      departamento = manejador.get_departamento_por_id(i + 1)
      if departamento is not None:
        print(f"{departamento.get_nombre()}\t", end="")
        for j in range(12):
          print(f"{self.__matriz[i][j]}\t", end="")
        print()
