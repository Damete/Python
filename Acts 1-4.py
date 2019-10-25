#### Damià Febrer Rebasa 26/09/2019

from random import randint

carton_1 = []
carton_2 = []
carton_3 = []
carton_4 = []
repetidos = []

def generarCartones():
    for i in range(0,20):
        carton_1.append(randint(0 , 99))
        carton_2.append(randint(0 , 99))
        carton_3.append(randint(0 , 99))
        carton_4.append(randint(0 , 99))

def generarNumero():
    valido = False
    done = False   

    while (done == False):
        numero = randint(0,99)
        if(repetidos.__contains__(numero)):
            valido = False
        else:
            valido = True
            done = True

    if(valido == True):
        repetidos.append(numero)
        print("Ha salido el " + str(numero))

def marcarCartones():
    for i in carton_1:
        posicion = len(repetidos) - 1
        if(i == repetidos[posicion]):
            carton_1.remove(i)
    
    for i in carton_2:
        posicion = len(repetidos) - 1
        if(i == repetidos[posicion]):
            carton_2.remove(i)

    for i in carton_3:
        posicion = len(repetidos) - 1
        if(i == repetidos[posicion]):
            carton_3.remove(i)
    
    for i in carton_4:
        posicion = len(repetidos) - 1
        if(i == repetidos[posicion]):
            carton_4.remove(i)

def jugar():
    ganador = False
    generarCartones()

    while(ganador == False):        

        generarNumero()
        marcarCartones()

        if(len(carton_1) == 0):
            ganador = True
            print("El carton 1 ha echo Bingo")

        if(len(carton_2) == 0):
            ganador = True
            print("El carton 2 ha echo Bingo")

        if(len(carton_3) == 0):
            ganador = True
            print("El carton 3 ha echo Bingo")

        if(len(carton_4) == 0):
            ganador = True
            print("El carton 4 ha echo Bingo")

jugar()