#!/usr/bin/python3

import os

#Lee la variable de entorno USER
user=os.getenv("USER")
print(user)

#Ejecutamos figlet
os.system("figlet " + user)
