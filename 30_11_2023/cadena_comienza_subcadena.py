#!/usr/bin/python3
#Escribir por pantalla cada carácter de una cadena introducida por teclado.

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")

if cad.startswith(subcad):
	print("La cadena comienza por la subcadena")
else:
	print("La candena NO comienza por la subcadena")

