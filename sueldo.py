def calcular_comision(ventas):
    if ventas < 3500:
        return 0.07  # 7% de comisión para ventas menores a 3500
    elif ventas >= 3500 and ventas <= 7000:
        return 0.10  # 10% de comisión para ventas entre 3500 y 7000
    else:
        return 0.15  # 15% de comisión para ventas mayores a 7000

def calcular_sueldo(salario_base, ventas):
    tasa_comision = calcular_comision(ventas)
    comision = ventas * tasa_comision
    sueldo_total = salario_base + comision
    return sueldo_total

while True:
    respuesta = input("¿Hay otro vendedor? (si/no): ").lower()
    if respuesta != 'si':
        break
    
    nombre = input("Ingrese el nombre del vendedor: ")
    salario_base = float(input(f"Ingrese el salario base de {nombre}: "))
    ventas = float(input(f"Ingrese el total de ventas de {nombre}: "))
    
    sueldo = calcular_sueldo(salario_base, ventas)
    print(f"El sueldo total de {nombre} es: ${sueldo:.2f}")
