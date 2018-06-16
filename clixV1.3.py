#!/usr/bin/python3

#----------------------------------------------------------------------#

# 12/06/2018 COMIENZO DEL PROYECTO "Clix" el asistente personal.
# Nombre: Clix.
# Autor: Luciano Joaquin Alfonso.
# Lenguaje: Python.
# Localizacion: Argentina, Rio Cuarto, Cordoba.

#-----------------------------------------------------------------------#  

def pedirNumeroEntero(): 
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entre 1 y 7')
     
    return num
 
salir = False
opcion = 0

import winsound # Importar reproductor de Windows (Solo archivos .WAV)

winsound.PlaySound("voces/welcome", winsound.SND_FILENAME) # En la carpeta "Voces/" se encuentran todos los archivos de voz.
bienvenido = input("Como es tu nombre.? ")
winsound.PlaySound("voces/encantado", winsound.SND_FILENAME ) # En la carpeta "Voces/" se encuentran todos los archivos de voz.
print ("bienvenido " + bienvenido)
dialogo = input("Que deseas hacer?. ")
print (dialogo)
winsound.PlaySound("voces/opciones", winsound.SND_FILENAME) # En la carpeta "Voces/" se encuentran todos los archivos de voz.

 
while not salir: # Mostramos las opciones disponibles.
    print ("#----Opciones--------------#")
    print ("#1. Opcion 1            -- #")
    print ("#2. Opcion 2            -- #")
    print ("#3. Opcion 3            -- #")
    print ("#4. Opcion 4            -- #")
    print ("#5. Opcion 5            -- #")
    print ("#6. Informacion de Clix -- #")
    print ("#7. Salir.              -- #")
    print ("#--------------------------#")
     
    print ("Selecciona una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1: # Opcion 1 muestra sub opciones.

        while not salir:
            print ("1. Sub_Opcion 1")
            print ("2. Sub_Opcion 2")
            print ("3. Sub_Opcion 3")
            print ("4. Volver atras")
            opcion = pedirNumeroEntero()
            if opcion == 4:
                salir = True
        salir = False

    elif opcion == 2: # Opcion 2 muestra sub opciones.

        while not salir:
            print ("1. Sub_Opcion 1")
            print ("2. Sub_Opcion 2")
            print ("3. Sub_Opcion 3")
            print ("4. Volver atras")
            opcion = pedirNumeroEntero()
            if opcion == 4:
                salir = True
        salir = False

    elif opcion == 3: # Opcion 3 muestra sub opciones.

        while not salir:
            print ("1. Sub_Opcion 1")
            print ("2. Sub_Opcion 2")
            print ("3. Sub_Opcion 3")
            print ("4. Volver atras")
            opcion = pedirNumeroEntero()
            if opcion == 4:
                salir = True
        salir = False

    elif opcion == 4: # Opcion 4 muestra sub opciones.
        while not salir:
            print ("1. Sub_Opcion 1")
            print ("2. Sub_Opcion 2")
            print ("3. Sub_Opcion 3")
            print ("4. Volver atras")
            opcion = pedirNumeroEntero()
            if opcion == 4:
                salir = True
        salir = False

    elif opcion == 5: # Opcion 5 muestra sub opciones.
        while not salir:
            print ("1. Sub_Opcion 1")
            print ("2. Sub_Opcion 2")
            print ("3. Sub_Opcion 3")
            print ("4. Volver atras")
            opcion = pedirNumeroEntero()
            if opcion == 4:
                salir = True
        salir = False

    elif opcion == 6: # info. sobre el proyecto
        while not salir:
            print ("#-----------------------------------------------------------------------#")
            print ("# Fecha: 12/06/2018 COMIENZO DEL PROYECTO 'Clix' el asistente personal.")
            print ("# Nombre: Clix.")
            print ("# Autor: Luciano Joaquin Alfonso.")
            print ("# Lenguaje: Python.")
            print ("# Localizacion: Argentina, Rio Cuarto, Cordoba.")
            print ("#-----------------------------------------------------------------------#")
            print ("1. Volver atras.")
            opcion = pedirNumeroEntero()
            if opcion == 1:
                salir = True
        salir = False

    elif opcion == 7: # Opcion 6 cierra el asistente.
        salir = True
    else:
        print ("Numero entre 1 y 6")

winsound.PlaySound("voces/adios", winsound.SND_FILENAME)