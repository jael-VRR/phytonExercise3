byte = int(input("ingrese el primer byte:"))
print(byte)
if not (byte & 128):
    print("clase A")
else:
    if not (byte & 64):
        print("clase B")
    else:
        if not (byte & 32):
            print("clase C")
        else:
            if not (byte & 16):
                print("clase D")
            else:
                print("clase E")


#ejercicio 3
#inicio la variable que contiene la dirección ip
ip=input("ingrese dirección ip:")
#reemplazo los puntos
ips = ip.replace(".", "")
#extraigo los 3 primeros números
byte=int(ips[0:3])

if not (byte & 128):
    print("clase A")
else:
    if not (byte & 64):
        print("clase B")
    else:
        if not (byte & 32):
            print("clase C")
        else:
            if not (byte & 16):
                print("clase D")
            else:
                print("clase E")