#!/usr/bin/python3

import sys

script=sys.argv[0]
params=sys.argv[1:]

if len(params) < 1:
        print("El número de parámetros no es correcto")
        exit(1)

for i in range(0, len(params)):
        params[i]=int(params[i])

#Busco el mayor
mayor=params[0]
for i in range(1, len(params)):
	if params[i] >  mayor:
		mayor = params[1]

#Muestro el mayor
print(mayor, "es el mayor")

