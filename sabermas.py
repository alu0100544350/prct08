#!/usr/bin/python
#!encoding:UTF-8
print"introduzca el nombre del fichero donde se encuentran los resultados:"
nombre_fichero=raw_input()

try:
  fichero=open(nombre_fichero)
  linea=fichero.readline()
  while(linea!=""):
    aproxima=int(linea.split()[3])
    print("Nº de intervalos: %d" %(aproxima))
    for i in range(5):
	linea=fichero.readline()
	porcentaje=linea.split()[0]
	umbral=float(linea.split()[6])
	print("%s de fallos para el umbral %2.5f" % (porcentaje,umbral))
    linea=fichero.readline()
except:
  print"el nombre del fichero introducido es incorrecto"
      