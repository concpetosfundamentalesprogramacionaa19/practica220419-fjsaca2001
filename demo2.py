"""
	Archivo: demo2.py
	Ejemplo de lenguaje Python
	autor: @fjsaca2001
"""
# Importacion del sys
import sys
# Asignacion de valores
nombre_archivo = sys.argv[0]
valor1 = sys.argv[1] 
valor2 = sys.argv[2]

# Aqui realizo la suma de variables
suma = int(valor1) + int(valor2)

# Aqui realizo la multiplicacion de variables
multi = int(valor2) * int(valor1)

# Presentacion de datos
print ("la sumas es:   %d" % suma)
print ("\nLa multiplicacion es:   %d" % multi)