
from funcion import calcular_total, calcular_promedio, clasificar_gasto

# Definición de los valores
primero = 5000
segundo = 1000
tercero = 2000


total_gastos = calcular_total(primero, segundo, tercero)

promedio = calcular_promedio(total_gastos, 3)


clasificacion = clasificar_gasto(total_gastos)

# Mostramos los resultados
print(f"Total de gastos: ${total_gastos}")
print(f"Promedio de gastos: ${promedio}")
print(f"Clasificación: {clasificacion}")