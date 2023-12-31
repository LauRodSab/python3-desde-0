#!/usr/bin/python3
#Vamos a realizar la clase 'DNI' donde vamos a guardar el número DNI
#(lo vamos a guardar en una cadena de longitud de 8) y la letra
# correspondiente.
#Vamos a crear el constructor, que recibe el número de DNI y calcula
#automáticamente
#Crearemos también los métodos seters y getters
#Se debe definir el método 'mostrar()' para imprimir el DNI

class Dni():

	def __init__(self,numero):
		self.numero=numero

	def __calcular_letra(self):
		letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
		return letras[int(self.numero)%23]

	@property
	def numero(self):
		return self._numero

	@property
	def letra(self):
		return self._letra
	@numero.setter
	def numero(self,numero):
		if len(numero)==8 and numero.isdigit():
			self.numero = numero
			self.letra = self._calcular_letra()
		else:
			self._numero=0
			self._letra = ""
			print("DNI Incorrecto")

	def mostrar(self):
		return self.numero+self.letra
