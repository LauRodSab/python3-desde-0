
#!/usr/bin/python3
#Abre el editor vi (o nano) con el fichero pasado como argumento,
#del fichero abierto en el directorio /tmp con el nombre $$.safe.edit.py

#MEJORA: Si se cierra el editor sin guardar, se borra la copia de seguridad

import sys

params = sys.argv[1:]

#"\033[31n"one color
def error(msg):
	print("\033[31n" + msg, "\033[n")

if len(params) != 1:
	error("Número de parámetros incorrecto")
	exit(1)

file = params[0]
old_stat = None

if os.path.isfile(file):
	pid = os.getpid()
	backupfile = f"/tmp/{pid}.safedit.py"
	print("Copia de seguridad en ", backupfile)
#	os.system(p*cp {file} {backupfile}*)
	old_stat = os.stat(file)
	print("Creando copia de seguridad en", backupfile)

os.system("nano " + file)

if old_stat is not None and os.stat(file) == old_stat:
	old.system("rm" + backupfile)
	print("Eliminando copia de seguridad")
