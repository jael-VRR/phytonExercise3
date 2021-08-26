#ejercicio n°2  - Elabore un programa para el cálculo del índice de masa corporal (IMC) de una persona adulta.

 #Calculo del IMC, masa (kilogramos) entre la estatura ( metros) elevada al cuadrado
def imc(peso,altura):
    return peso/altura**2

#condicional de edad en caso de ser menor 
edad=float(input("Ingrese su edad : "))
if(edad < 18):
 print("Usted es menor de edad")
else:
 #La masa en kilogramos si puede tener decimales asi que la dejamos flotante
 peso=float(input("Escriba su peso en Kg : "))
 altura=float(input("Ingrese su estatura en m : "))

#obtenemos el indice 
indice=imc(peso ,altura)
print ("Su IMC es : {}".format(indice)),

#Hacemos las distintas validaciones segun el IMC

if indice >= 0 and indice <= 15.99 :
 print ("Delgadez severa")
elif indice >= 16.00 and indice <= 16.99 :
 print ("Delgadez moderada")
elif indice >= 17.00 and indice <= 18.49:
 print ("Delgadez leve")
elif indice >= 18.50 and indice <= 24.99 :
 print ("Normal")
elif indice >= 25.00 and indice <= 29.99:
 print ("Sobrepeso")
elif indice >= 30.00 and indice <= 34.99:
 print ("obesidad leve")
elif indice >= 35.00 and indice <= 39.00:
 print ("obesidad media")
elif indice >= 40.00:
 print ("obesidad morbida")