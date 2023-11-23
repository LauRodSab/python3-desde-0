#!/usr/bin/python3

secreto = "asdasd"
clave = input("Dime la clave: ")
while clave != secreto:
        print("Clave incorrecta")
	otra = input("¿Quieres introducir otra clave (S/N)?:")
        if otra.upper()=="N":
		break;
	clave = input("Dime la clave: ")
print("Bienvenido!!")
print("Progrma terminado")
