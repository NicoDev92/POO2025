from ManejadorDepartamentos import ManejadorDepartamentos
from Accidente import Accidente

def menu():
  print("\n--- MENÚ DE OPCIONES ---")
  print("1. Total de accidentes por mes")
  print("2. Departamento con más accidentes en un mes")
  print("3. Total anual por nombre de departamento")
  print("4. Mostrar tabla completa")
  print("5. Registrar accidente")
  print("0. Salir")

def opcion_1(accidentes: Accidente, manejador : ManejadorDepartamentos):
  mes = int(input("Ingrese número de mes (1-12): "))
  datos_accidentes = accidentes.get_matriz()
  for i in range(19):
    depto = manejador.get_departamento_por_id(i + 1)
    if depto is not None:
      print(f"{depto.get_nombre()}: {datos_accidentes[mes-1]} accidentes")

def opcion_2(accidentes : Accidente, manejador : ManejadorDepartamentos):
  mes = int(input("Ingrese mes: "))
  resultado = accidentes.mayor_accidentes_en_mes(mes, manejador)
  if resultado is not None:
    print(f"Departamento: {resultado['departamento']}, Accidentes: {resultado['accidentes']}")
  else:
    print("No hubo resultados concluyentes")

def opcion_3(accidentes: Accidente, manejador: ManejadorDepartamentos):
  nombre_depto = input("Ingrese nombre del departamento: ")
  if nombre_depto != "":
    resultado = accidentes.total_anual_por_departamento(nombre_depto, manejador)
    if resultado is not None:
      print(f"Departamento: {resultado['departamento']}, Accidentes: {resultado['accidentes_totales']}")
    else:
      print("Departamento no encontrado.")
  else:
    print("Nombre de departamento vacío.")

def opcion_4(accidentes : Accidente, manejador : ManejadorDepartamentos):
  accidentes.mostrar_total_por_departamento(manejador)

def opcion_5(accidentes : Accidente):
  id_depto = int(input("Ingrese número de departamento (1-19): "))
  mes = int(input("Ingrese número de mes (1-12): "))
  cantidad = int(input("Ingrese cantidad de accidentes: "))
  resultado = accidentes.registrar_accidente(id_depto, mes, cantidad)
  if resultado > 0:
    print("Registrado exitosamente")
  else:
    print("Ocurrio un error, no se pudo cargar el registro")


def main_menu():
  manejador_deptos = ManejadorDepartamentos()
  manejador_deptos.cargar_desde_archivo()
  accidentes = Accidente()
  accidentes.inicializar()

  while True:
    menu()
    op = input("Opción: ")
    if op == "1":
      opcion_1(accidentes, manejador_deptos)
    
    elif op == "2":
      opcion_2(accidentes, manejador_deptos)

    elif op == "3":
      opcion_3(accidentes, manejador_deptos)
    
    elif op == "4":
      opcion_4(accidentes, manejador_deptos)
    
    elif op == "5":
      opcion_5(accidentes)

    elif op == "0":
      return

    else:
      print("Opción inválida")