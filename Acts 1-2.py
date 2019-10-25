#Damià Febrer Rebasa 24/09/2019    Cambiar cabecera :(

# Creación del fichero
def crearFichero():
    try:
        file = open("filmoteca.txt", "x")

        #Modificación del fichero
        file = open("filmoteca.txt", "a")
        file.write("Titulo;Director;Actores;Año;Genero;Duracion;Pais")
        file.close()
    except:
        print("Nada")
    
#Añadir peliculas
def añadirPeliculas():
    print("Cuantas peliculas quieres añadir ?\n")
    pelis = input()

    y = 1

    # Inserción de las pelis en el fichero
    while y <= int(pelis):
        print("Pelicula " + str(y) + " de " + str(pelis) + "\n")

        print("\nTitulo de la peli")
        Titol = input()

        print("\nDirector")
        Director = input()

        print("\nActores")
        Actor = input()

        print("\nAño")
        Any = input()

        print("\nGenero")
        Genero = input()

        print("\nDuración")
        Duracion = input()

        print("\nPaís")
        Pais = input()

        file = open("filmoteca.txt", "a")
        file.write("\n" + Titol + "; " + Director + "; " + Actor + "; " + Any + "; " + Genero + "; " + Duracion + "; " + Pais + "; \n")
        file.close

        y += 1

def leerFichero(busqueda):
    #Creamos array
    leido = []
    #Abrimos el fichero y vamos metiendolo en la array linea a linea
    with open ('filmoteca.txt', 'rt') as filmoteca:
        for linea in filmoteca:
            leido.append(linea)
    filmoteca.close()

    #Printeamos la lineas guardadas que coincidan con el String que nos pasa el user
    print("Resultado de la busqueda\n")
    for i in leido:
        if(i.__contains__(busqueda)):
            print(i + "\n")
    


salir = False
crearFichero()

while(salir == False):
    print("\nBienvenido a la filmoteca que operacion quieres realizar? \n 1- Introducir pelicula/s \n 2- Buscar pelicula \n 3- Salir \n")
    respuesta = input()

    if(respuesta == str(1)):
        añadirPeliculas()
    elif(respuesta == str(2)):
        print("Que pelicula quieres buscar ?\n")
        busqueda = input()
        leerFichero(busqueda)
    elif(respuesta == str(3)):
        salir = True