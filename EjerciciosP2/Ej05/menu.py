from ManejadorBeca import ManejadorBeca
from ManejadorBeneficiario import ManejadorBeneficiario

def menu():
  print("\nMenú de opciones:")
  print("1. Beneficiarios por tipo de beca")
  print("2. Verificar si un beneficiario tiene múltiples becas")
  print("3. Listar beneficiarios ordenados por facultad")
  print("4. Listar estudiantes con promedio > 8 sin ayuda económica")
  print("0. Salir")

def opcion_1(manejador_beneficiarios, manejador_becas):
  tipo_beca = input("Ingrese el tipo de beca: ")
  resultado = manejador_beneficiarios.buscar_beneficiarios_tipo_beca(tipo_beca, manejador_becas)
  lista_alumnos = resultado["lista_alumnos"]
  importe = resultado["importe"]

  print(f"\nBeneficiarios de la beca '{tipo_beca}':")
  for beneficiario in lista_alumnos:
    print(f"{beneficiario}")
  print(f"Importe total: ${importe}")

def opcion_2(manejador_beneficiarios):
  dni = input("Ingrese el DNI del beneficiario: ")
  beneficiario = manejador_beneficiarios.multiples_becas_por_dni(dni)
  if beneficiario is not None:
    print(f"\n{beneficiario.get_nombre()} {beneficiario.get_apellido()} tiene más de una beca.")
  else:
    print(f"\nNo se encontró beneficiario con múltiples becas con el DNI {dni}.")

def opcion_3(manejador_beneficiarios):
  beneficiarios = sorted(manejador_beneficiarios.get_beneficiarios(), reverse=True)
  print("\nBeneficiarios ordenados por facultad:")
  for b in beneficiarios:
    print(f"{b.get_facultad()}: {b.get_nombre()} {b.get_apellido()}")

def opcion_4(manejador_beneficiarios):
  id_ayuda_economica = 4
  estudiantes = manejador_beneficiarios.obtener_estudiantes_sin_ayuda_economica(id_ayuda_economica)
  print("\nEstudiantes con promedio > 8 sin ayuda económica:")
  for e in estudiantes:
    print(f"{e.get_nombre()} {e.get_apellido()} - Promedio: {e.get_promedio()}")

def main_menu():
  manejador_becas = ManejadorBeca()
  manejador_becas.test()

  manejador_beneficiarios = ManejadorBeneficiario()
  manejador_beneficiarios.test()

  while True:
    menu()
    opcion = input("Seleccione una opción: ").lower()

    if opcion == "1":
      opcion_1(manejador_beneficiarios, manejador_becas)
    elif opcion == "2":
      opcion_2(manejador_beneficiarios)
    elif opcion == "3":
      opcion_3(manejador_beneficiarios)
    elif opcion == "4":
      opcion_4(manejador_beneficiarios)
    elif opcion == "0":
      return
    else:
      print("Opción no válida.")
