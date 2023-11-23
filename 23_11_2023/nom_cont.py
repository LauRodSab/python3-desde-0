#!/usr/bin/python3
#Escribe un programa que pida un nombre de usuario y una contraseña y si se
#ha introducido "pepe" y asdasd" se indica "Has entrado si no se da error

usuario = input("Introduce el usuario: ")
password = input("Introduce el password: ")

if usuario == "pepe" and password == "asdasd":
	print("Has entrado al sistema")

if usuario != "pepe" or password != "asdasd":
		print("Usuario/Password incorrectos")

