"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
# Definir el diccionario con dos registros de un alumno
alumnos = {
    1: {"nombre": "Juan", "edad": 20, "curso": "Python básico"},
    2: {"nombre": "María", "edad": 22, "curso": "Introducción a la programación"}
}

# Función para imprimir los registros de los alumnos
def imprimir_registros():
    for key, value in alumnos.items():
        print(f"Registro {key}:")
        print(f"Nombre: {value['nombre']}")
        print(f"Edad: {value['edad']}")
        print(f"Curso: {value['curso']}")
        print("------------------")

# Función para editar un campo del registro de un alumno
def editar_registro(num_registro, campo, nuevo_valor):
    if num_registro in alumnos:
        if campo in alumnos[num_registro]:
            alumnos[num_registro][campo] = nuevo_valor
            print("Campo editado exitosamente.")
        else:
            print("El campo especificado no existe.")
    else:
        print("Número de registro no encontrado.")

# Ejemplo de uso de las funciones
print("Registros actuales:")
imprimir_registros()

# Editar el registro 1, cambiando el curso
editar_registro(1, "curso", "Programación avanzada")

# Imprimir los registros actualizados
print("Registros actualizados:")
imprimir_registros() 