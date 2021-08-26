
#Ejercicio n°1 - Elabore un programa que solicite los datos personales de una persona


#declaro las variables que almacenan los datos a ingresar
nombre= input("Ingrese su nombre : ")
apellido= input("Ingrese su apellido : ")
edad= input("Ingrese su edad : ")
dni= input("Ingrese su dni : ")
telefono= input("Ingrese su teléfono : ")


#se crea un array que contiene  los datos de la tabla

d=[
    ["Nombres   :",nombre],
    ["Apellido  :",apellido],
    ["Edad      :",edad],
    ["N° de Dni :",dni],
    ["Teléfono  :",telefono]
]

#

Tabla = """\


---------------------------------------------------------
{} 
---------------------------------------------------------\
"""
#utilizamos un salto de linea y unimos la tabla al contenido.
#indicamos la alineación hacia l derecha e izquierda 
Tabla = (Tabla.format('\n'.join("| {:>15} {:<37} |".format(*fila) 
#iteramos en los datos e imprimimos el resultado
 for fila in d)))
print(Tabla)







