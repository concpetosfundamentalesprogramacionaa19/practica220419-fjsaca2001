""""
	Archivo: problema1.py
	Ejemplo de lenguaje Python
	autor: @fjsaca2001
"""
# Pidiendo valores para las variables
x = input("Ingrese el valor para X: ")
y = input("Ingrese el valor para Y: ")
z = input("Ingrese el valor para Z: ")
#calculo de M
m = (float(x)+(float(y)/float(z)))/(float(x)-(float(y)/float(z)))

# Presentacion de datos
print("x = %.1f \n\t y = %.1f \n\t\tz = %.1f \nda como resultado:\n\tm = %.1f"% (float(x), float(y), float(z), float(m)))