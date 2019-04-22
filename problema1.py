"""
	Archivo: problema2.py
	Ejemplo de lenguaje Python
	autor: @fjsaca2001
"""
# Pidiendo valores para las variables
horas = input("Ingrese las horas laboradas: ")
c_horas = input("Ingrese el costo por hora: ")

#calculo de M

sueldo = float(horas) * float(c_horas)
seguro = float(sueldo) * 0.10
sueldo = sueldo - seguro

# Presentacion de datos
print("Su descuento del seguro es: %.1f \nSu sueldo total es: %.1f"% (seguro,sueldo))