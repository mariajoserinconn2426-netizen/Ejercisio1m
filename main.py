# Programa para evaluar el rendimiento académico de estudiantes

continuar = "si"

while continuar == "si":

    nombre = input("Ingrese el nombre del estudiante: ")

    suma = 0
        # Bucle for para pedir las 5 notas
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        suma = suma + nota

