def calcular_total(primero,segundo,tercero):
    total=primero+segundo+tercero
    return total
def calcular_promedio(total_promedio,cantidad):
    promedio=total_promedio/cantidad
    return promedio

def clasificar_gasto(total_gastos):
    if total_gastos<=5000:
        return print("gastos bajos")
    elif 5001 <= total_gastos <= 10000:
        return print("gastos modertados")
    else:
        return "Gasto elevado"

