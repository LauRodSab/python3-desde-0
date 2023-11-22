#!/usr/bin/python3
#Dadas dos variables numéricas A y B. que el usuario debe
#teclear, se pide realizar un algoritmo que intercambie 
#los valores de ambas y muestre cuanto valen las dos variables

a = int(input("Introduce el valor de la variable A: "))
b = int(input("Introduce el valor de la variable B: "))
aux = a
a = b
b = aux
print("Nuevo valor de A: ", a)
print("Nuevo valor de B: ", b)

