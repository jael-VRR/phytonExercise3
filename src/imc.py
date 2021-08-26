#ejercicio n°2  - Elabore un programa para el cálculo del índice de masa corporal (IMC) de una persona adulta.

 #Calculo del IMC, masa (kilogramos) entre la estatura ( metros) elevada al cuadrado
def imc(peso,altura):
    return round(peso/altura**2,2)

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

if indice >= 0 and indice <= 18.5 :
 print ("BAJO PESO")
elif indice >= 18.5 and indice <= 24.90 :
 print ("PESO NORMAL")
elif indice >= 25.00 and indice <= 29.90:
 print ("SOBREPESO")
elif indice >= 30.00 and indice <= 34.90 :
 print ("OBESIDAD TIPO 1")
elif indice >= 35.00 and indice <= 39.9:
 print ("OBESIDAD TIPO 2")
elif indice >= 40.00:
 print ("OBESIDAD TIPO 3")

 
