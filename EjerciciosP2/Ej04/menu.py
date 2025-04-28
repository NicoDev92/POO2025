from ManejadorFacultad import ManejadorFacultad
from ManejadorCarrera import ManejadorCarrera

def menu():
  print("\n--- MENÚ DE OPCIONES ---")
  print("1. Mostrar facultad de una carrera")
  print("2. Mostrar cantidad de carreras por facultad")
  print("3. Listar carreras de una facultad (ordenadas alfabéticamente)")
  print("4. Listar carreras")
  print("5. Listar facultades")
  print("0. Salir")

def opcion_1(manejador_carreras : ManejadorCarrera, manejador_facultades : ManejadorFacultad):
  nombre_carrera = input("Ingrese el nombre de la carrera: ")
  facultad = manejador_carreras.buscar_facultad_por_carrera(nombre_carrera, manejador_facultades)
  if facultad:
      print(f"La carrera se dicta en la facultad: {facultad.get_nombre()}")
  else:
    print("Carrera no encontrada.")

def opcion_2(manejador_facultades : ManejadorFacultad):
  resultados = manejador_facultades.calcular_cantidad_carreras()
  for detalle in resultados:
      print(f"Facultad: {detalle['facultad']} - Cantidad de carreras: {detalle['cantidad_carreras']}")

def opcion_3(manejador_carreras : ManejadorCarrera, manejador_facultades : ManejadorFacultad):
  nombre_facultad = input("Ingrese el nombre de la facultad: ")
  carreras = manejador_facultades.listar_carreras_alfabeticamente(nombre_facultad)
  if carreras:
      print(f"Carreras dictadas en {nombre_facultad}:")
      for carrera in carreras:
          print(f"{carrera.get_nombre()} - Duración: {carrera.get_duracion()}")
  else:
      print("Facultad no encontrada o sin carreras.")

def opcion_4(manejador_carreras : ManejadorCarrera):
  carreras = manejador_carreras.get_carreras()
  for carrera in carreras:
      if carrera is not None:
          print(carrera)

def opcion_5(manejador_facultades : ManejadorFacultad):
  facultades = manejador_facultades.get_facultades()
  for facultad in facultades:
      if facultad is not None:
          print(facultad)

def main_menu():
    manejador_facultades = ManejadorFacultad(5)
    manejador_facultades.cargar_desde_archivo()
    manejador_carreras = ManejadorCarrera(5)
    manejador_carreras.cargar_desde_archivo()

    while True:
        menu()
        op = input("Opción: ")
        if op == "1":
            opcion_1(manejador_carreras, manejador_facultades)
        elif op == "2":
            opcion_2(manejador_facultades)
        elif op == "3":
            opcion_3(manejador_carreras, manejador_facultades)
        elif op == "4":
            opcion_4(manejador_carreras) 
        elif op == "5":
            opcion_5(manejador_facultades) 
        elif op == "0":
            return
        else:
            print("Opción inválida")
