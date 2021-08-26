#ejercicio n°4
#Probando la potencia de menos 1 
x = pow(-1, 4)
print(x)
#Cuando el resultado es 1 indica que el número es par
x = pow(-1, 5)
print(x)
#Cuando el resultado es -1 indica que el número es impar

#declaro la variable que contiene el número a indicar si es par o impar
number=int(input("Ingrese un número: "))
# función con una sentencia de retorno
def espar (number):
#La función pow() recibe dos (02) argumentos, eleva el primero argumento a la potencia del segundo argumento y luego lo compara con 1 retornando un valor booleano.
    return pow(-1,number) == 1 
print (espar(number))