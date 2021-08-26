#declaro variable que contiene el dato del ingreso anual
ingreso = float(input("Ingrese el ingreso anual:"))
#primera condición a cumplir si el ingreso es menor que 85528 la retención es de 18% - otro descuento fijo
if ingreso < 85528:
    impuesto = (ingreso * .18) - 556.02
#si la cantidad es mayor de 85528 se retiene una cantidad fija más el 32% de la diferencia del ingreso menos 85528
else:
    impuesto = 14839.02 + ((ingreso - 85528) * .32)
#En caso que el ingreso sea negativo no habrá retención
if impuesto < 0:
    impuesto = 0
#el método round tiene 2 parámetros el número y la cantidad de cifras a las que se redondea
impuesto = round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")