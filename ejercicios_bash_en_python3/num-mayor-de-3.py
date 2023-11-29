#!/usr/bin/python3

import sys

script=sys.argv[0]
params=sys.argv[1:]

if len(params) != 3:
	print("El número de parámetros no es correcto")
	exit(1)

for i in range(0, len(params)):
	params[i]=int(params[i])

a=params[0]
b=params[1]
c=params[2]

if a > b and a > c:
	print(a, "es el mayor")
elif b > c:
	print(b, "es el mayor")
else:
	print(c, "es el mayor")

