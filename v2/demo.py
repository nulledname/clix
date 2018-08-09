def pedirNumeroEntero():

	correcto=False
	num=0
	while(not correcto):
		try:
			num = int(input('Introduce un numero: '))
		except ValueError:
			print('Error!')
	return num

salir = False
opcion = 0

import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

while not salir:
	b = input("Como es tu nombre? ")
	r = ("encantado, " + b ) + (",Mi nombre es clix tu asistente personal ")
	speaker.Speak(r)
	speaker.Speak(a)
	a = int(input( "Presiona 1 para opciones "))	

	if a == 1:
		print('Opciones')
		print('opcion 1')
		print('opcion 2')
		print('opcion 3')

		print('Seleciona una opcion: ')

		opcion = pedirNumeroEntero()

		if opcion == 1:

			while not salir:
				print('opcion 1')