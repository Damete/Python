## Damià Febrer Rebasa 30/09/2019

from random import randint

def generarNumero(generadoMaquina):
    generadoMaquina = randint(0, 99)
    return generadoMaquina

def comprobarNumero(intentos, generadoMaquina):    
    while(intentos > 0):
        print("\nIntroduce un número")
        userInput = input()

        if(generadoMaquina == int(userInput)):
            print("\nHas acertado el número, tienes un premio de 5€")
            ganador = True
            return ganador
        else:
            intentos = intentos - 1
            ganador = False
            if(generadoMaquina > int(userInput)):
                print("\nEl número generado por la máquina es mayor que el que has intoducido")
            if(generadoMaquina < int(userInput)):
                print("\nEl número generado por la máquina es menor al número que has introducido")

    return ganador

def comprobarIntentos(euros, intentos):
    intentos = 0
    if(euros > 0):
        intentos += 5
        return intentos



def Ej5():

    generadoMaquina = 0 
    euros = 0
    intentos = 0
    intentosExtra = 0
    eurosIntroducidos = 0
    ganador = False

    fichero = open("Registro.txt", "a")

    generadoMaquina = generarNumero(generadoMaquina)

    print("Introducir 1€ ?  S/N")
    respuesta = input()

    if(respuesta == "S" or respuesta == "s"):
        euros += 1
        eurosIntroducidos += 1
        intentos = comprobarIntentos(euros, intentos)
    else:
        exit
        
    ganador = comprobarNumero(intentos, generadoMaquina)
    
    while(ganador == False):
        euros = 0
        intentos = 0
        print("\nTe has quedado sin intentos, quieres introducir otro euro para tener 5 intentos más ??    S/N")
        respuesta = input()

        if(respuesta == "Si" or respuesta == "SI" or respuesta == "S" or respuesta == "s"):
            euros += 1
            eurosIntroducidos += 1
            intentosExtra += 1
            intentos = comprobarIntentos(euros, intentos)
            ganador = comprobarNumero(intentos, generadoMaquina)
        
        else:
            print("Espero que te lo hayas pasado bien")            
            fichero.write("\n===============Partida===============\n" + 
                        "Dinero introducido por el usuario: " + str(eurosIntroducidos) + "\n" +
                        "Números que ha intentado el usuario:" + str() + "\n" +
                        "Número generado por la máquina: " + str(generadoMaquina) + "\n" +
                        "El usuario ha sido premiado : " + str(ganador) + "\n" +
                        "Intentos extra que ha realizado el usuario: " + str(intentosExtra) + "\n" +
                        "======================================" )
            fichero.close()
            ganador = True
            

Ej5()