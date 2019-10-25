#### Damià Febrer Rebasa 25/09/2019

redo = True
valido = True

while redo == True:
    print("\nQue moneda tienes ?")
    monedaActual = input()
    
    if(monedaActual == "EUR" or monedaActual == "DOL" or monedaActual == "YEN"):
        valido = True
    else:
        valido = False
        while(valido != True):
            print("\nLa moneda introducida es invalida, por favor vuelva a introducirla")
            monedaActual = input()
            if(monedaActual == "EUR" or monedaActual == "DOL" or monedaActual == "YEN"):
                valido = True
            else:
                valido = False
            

    print("\nA que moneda quieres convertir")
    nuevaMoneda = input()

    if(nuevaMoneda == "EUR" or nuevaMoneda == "DOL" or nuevaMoneda == "YEN"):
        nuevaValida = True
    else:
        nuevaValida = False
        while(nuevaValida != True):
            print("\nLa moneda introducida es invalida, por favor vuelva a introducirla")
            nuevaMoneda = input()
            if(nuevaMoneda == "EUR" or nuevaMoneda == "DOL" or nuevaMoneda == "YEN"):
                nuevaValida = True
            else:
                nuevaValida = False

    if(monedaActual == "EUR"):
        if(nuevaMoneda == "DOL"):
            EUR = 0
            DOL = 1.10
            print("\nCuantos Euros quieres pasar a Dolares ?")
            EUR = input()
            Total = (float(EUR) * DOL)
            print("\nEl total de la conversion es : " + str(Total))
            print("\nQuieres hacer otra conversion ?  S/N")
            respuesta = input()
            if(respuesta == "S"):
                redo = True
            else:
                redo = False
        
        if(nuevaMoneda == "YEN"):
            EUR = 0
            YEN = 118.09
            print("\nCuantos Euros quieres cambiar a Yenes ? ")
            EUR = input()
            Total = (float(EUR) * YEN)
            print("\nEl total de la conversion es : " + str(Total))
            print("\nQuieres hacer otra conversion ?  S/N")
            respuesta = input()
            if(respuesta == "S"):
                redo = True
            else:
                redo = False


    if(monedaActual == "DOL"):
        if(nuevaMoneda == "EUR"):
            DOL = 0
            EUR = 0.91
            print("\nCuantos Dolares quieres cambiar a Euros ?")
            DOL = input()
            Total = (float(DOL) * EUR)
            print("\nEl total de la conversion es : " + str(Total))
            print("\nQuieres hacer otra conversion ?  S/N")
            respuesta = input()
            if(respuesta == "S"):
                redo = True
            else:
                redo = False

        if(nuevaMoneda == "YEN"):
            DOL = 0
            YEN = 107.32
            print("\nCuantos Dolares quieres convertir a Yenes ?")
            DOL = input()
            Total = (float(DOL) * YEN)
            print("\nEl total de la conversion es : " + str(Total))
            print("\nQuieres hacer otra conversion ?  S/N")
            respuesta = input()
            if(respuesta == "S"):
                redo = True
            else:
                redo = False


    if(monedaActual == "YEN"):
        if(nuevaMoneda == "EUR"):
            YEN = 0
            EUR = 0.0085
            print("\nCuantos Yenes quieres convertir a Euros ?")
            YEN = input()
            Total = (float(YEN) * EUR)
            print("\nEl total de la conversion es : " + str(Total))
            print("\nQuieres hacer otra conversion ?  S/N")
            respuesta = input()
            if(respuesta == "S"):
                redo = True
            else:
                redo = False
        
        if(nuevaMoneda == "DOL"):
            YEN = 0
            DOL = 0.0093
            print("\nCuantos Yenes quieres cambiar a Dolares ?")
            YEN = input()
            Total = (float(YEN) * DOL)
            print("\nEl totla de la conversion es : " + str(Total))
            print("\nQuieres hacer otra conversion ?  S/N")
            respuesta = input()
            if(respuesta == "S"):
                redo = True
            else:
                redo = False