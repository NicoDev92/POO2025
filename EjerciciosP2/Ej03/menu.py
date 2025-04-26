def menu():
  print("\n--- MENÚ DE OPCIONES ---")
  print("1. Total de accidentes por mes")
  print("2. Departamento con más accidentes en un mes")
  print("3. Total anual por nombre de departamento")
  print("4. Mostrar tabla completa")
  print("5. Registrar accidente")
  print("0. Salir")

def main():
  manejador = ManejadorDepartamentos()
  manejador.cargar_desde_archivo()
  accidentes = Accidente()

  while True:
    menu()
    op = input("Opción: ")
    if op == "1":
      mes = int(input("Ingrese número de mes (1-12): "))
      datos = accidentes.total_por_mes(mes)
      for i in range(19):
        d = manejador.get_departamento_por_id(i + 1)
        if d:
          print(f"{d.get_nombre()}: {datos[i]} accidentes")

    elif op == "2":
      mes = int(input("Ingrese mes: "))
      id_dep, cant = accidentes.mayor_accidentes_en_mes(mes)
      nombre = manejador.get_departamento_por_id(id_dep).get_nombre()
      print(f"{nombre} tuvo la mayor cantidad: {cant} accidentes")

    elif op == "3":
      nombre = input("Ingrese nombre del departamento: ")
      d = manejador.get_departamento_por_nombre(nombre)
      if d:
        total = accidentes.total_anual_por_departamento(d.get_id())
        print(f"{nombre}: {total} accidentes totales")
      else:
        print("Departamento no encontrado")

    elif op == "4":
          accidentes.mostrar_tabla(manejador)

    elif op == "5":
      id_dep = int(input("Ingrese número de departamento (1-19): "))
      mes = int(input("Ingrese número de mes (1-12): "))
      cantidad = int(input("Ingrese cantidad de accidentes: "))
      accidentes.registrar_accidente(id_dep, mes, cantidad)

    elif op == "0":
      return

    else:
      print("Opción inválida")