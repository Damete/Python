#Damià Febrer Rebasa 24/09/2019

from random import randint

x = 0
Lista = []

while x < 10:

    print("Quieres introducir un numero en la posición " + str(x) + " de la lisa")
    respuesta = input()

    if(respuesta == "S" or respuesta == "s"):
        usuario = randint(0,9)
        Lista.append(usuario)
        x += 1
    else:
        usuario = "#"
        Lista.append(usuario)
        x += 1

i = 0
for i in Lista:
    print(i)
    