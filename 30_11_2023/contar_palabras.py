#!/usr/bin/python3

cont = 0
posicion = 0

cad = input("Introduce una cadena: ")

#Elimino los espacios
cad =  cad.strip()

#Voy buscando los espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
	cont = cont + 1
#	No tengo en cuenta los espacios entre las palabras
	while cad[posicion + 1] == " ":
		posicion = posicion + 1
	posicion = cad.find(" ", posicion + 1)
print("La frase tiene ",cont + 1, "palabras.")
