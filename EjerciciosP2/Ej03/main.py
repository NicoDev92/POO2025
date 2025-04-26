from ManejadorDepartamentos import ManejadorDepartamentos
from Accidente import Accidente



def main():
  manejador_dptos = ManejadorDepartamentos()
  manejador_dptos.test()
  accidente = Accidente()
  accidente.inicializar()
  matriz = accidente.get_matriz()
  for i in range(19):  # departamentos
      for j in range(12):  # meses
          print(f"{matriz[i][j]} | ", end="")
      print("\n")

  dptos = manejador_dptos.get_lista()
  print(manejador_dptos.get_departamento_por_nombre("zOnDa"))
  print(accidente.total_anual_por_departamento("zOnDa"))


if __name__ == "__main__":
    main()
