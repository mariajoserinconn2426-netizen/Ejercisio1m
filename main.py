# Programa para evaluar el rendimiento académico de estudiantes

continuar = "si"

while continuar == "si":

    nombre = input("Ingrese el nombre del estudiante: ")

    suma = 0
        # Bucle for para pedir las 5 notas
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        suma = suma + nota
            # Cálculo del promedio
    promedio = suma / 5

    # Mostrar resultados
    print("\n--- Resultado ---")
    print("Estudiante:", nombre)
    print("Promedio:", round(promedio, 2))
        # Condicionales
    if promedio >= 4.5:
        print("Estado: Excelente")
    elif promedio >= 3.0:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")

    continuar = input("\n¿Desea evaluar otro estudiante? (si/no): ")

print("Programa finaliza muchas garcias por usar nuestro programa siempre estaremos a tus servicios.")




