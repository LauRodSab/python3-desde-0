#!/usr/bin/python3

import os
import subprocess

#Lee la variable de entorno USER
user=os.getenv("USER")

#Compruebo si el figlet está instalado
def verify():
	return subprocess.call("which figlet > /dev/null", shell=True) == 0
#print(codigo)

#Ejecutamos figlet
if verify():
	os.system("figlet " + user)
else:
	print("no tengo figlet :_(...", user)
