#!/usr/bin/python3
cad=input("Dime un número: ")
try:
	print (10/int(cad))
except ValueError:
	print ("No se puede convertir a entero")
except ZeroDivisionError:
	print("No se puede dividir por cero")
else:
	print("Se ha introducido otro error")
finally:
	print("Se ejecuta siempre al final")

