def obtener_rango_edad(edad):
    if edad < 2:
        return "Menor a 2 años"
    elif edad >= 2 and edad < 5:
        return "Entre 2 y menor a 5 años"
    elif edad >= 5 and edad < 10:
        return "Entre 5 y menor a 10 años"
    else:
        return "Mayor o igual a 10 años"

# Variables para almacenar la cantidad de animales en cada rango de edades
menor_2 = 0
entre_2_5 = 0
entre_5_10 = 0
mayor_10 = 0
total_animales = 0

while True:
    respuesta = input("¿Hay otro animal a registrar? (si/no): ").lower()
    if respuesta != 'si':
        break
    
    edad = int(input("Ingrese la edad del animal (en años): "))
    rango_edad = obtener_rango_edad(edad)
    
    if rango_edad == "Menor a 2 años":
        menor_2 += 1
    elif rango_edad == "Entre 2 y menor a 5 años":
        entre_2_5 += 1
    elif rango_edad == "Entre 5 y menor a 10 años":
        entre_5_10 += 1
    else:
        mayor_10 += 1
    
    total_animales += 1

# Cálculo de porcentajes
porcentaje_menor_2 = (menor_2 / total_animales) * 100 if total_animales > 0 else 0
porcentaje_entre_2_5 = (entre_2_5 / total_animales) * 100 if total_animales > 0 else 0
porcentaje_entre_5_10 = (entre_5_10 / total_animales) * 100 if total_animales > 0 else 0
porcentaje_mayor_10 = (mayor_10 / total_animales) * 100 if total_animales > 0 else 0

# Mostrar resultados
print("\nEstadísticas de edades de los animales en el zoológico:")
print(f"Total de animales registrados: {total_animales}")
print(f"Animales Menor a 2 años: {menor_2} ({porcentaje_menor_2:.2f}%)")
print(f"Animales Entre 2 y menor a 5 años: {entre_2_5} ({porcentaje_entre_2_5:.2f}%)")
print(f"Animales Entre 5 y menor a 10 años: {entre_5_10} ({porcentaje_entre_5_10:.2f}%)")
print(f"Animales Mayor o igual a 10 años: {mayor_10} ({porcentaje_mayor_10:.2f}%)")
