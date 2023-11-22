#!/usr/bin/python3
#Pedir el nombre y apellidos de una persona y mostar
#sus iniciales
nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]

#Voy a utilizar el método upper para convertir a mayúsculas
inicial = inicial.upper()
print("Las iniciales son:",inicial)
