#!/usr/bin/python3

import sys

script=sys.argv[0]
params=sys.argv[1:]

#Para definir el error
def help():
	print("Uso " + script + "num 1 num2")

if len(params) != 2:
	print("Error: número de parámetros incorrectos")
	help()
	exit(1)

else:
	a=int(params[0])
	b=int(params[1])
	suma = a + b
	print("Resultado ", suma)
