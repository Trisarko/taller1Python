#Taller Número 1 de Python

#Ejercicio 1
base = float(input("La base del triangilo es: "))
altura = float(input("La altura del triangilo es: "))
area = base*altura/2
print ("El area es {}." .format(area))

#Ejercicio 2
dolar = float(input("Ingrese el valor actual del dolar: "))
cDolares = float(input("Ingrese la cantidad de Dolares para su conversión: "))
cPesos = dolar*cDolares
print(cDolares, "dólares, equivalen a ", cPesos, "Pesos")

#Ejercicio 3
C = int(input("Ingrese la cantidad de grados Celcius que desea convertir: "))
F = 9 / 5 * C + 32
print(C, "grados Celcius equivalen a: ", F, "grados Fahrenheit")

#Ejercicio 4
lustro = float(input("Escriba la cantidad de Lustros: "))
seg_lustro = 60 * 60 * 24 * 365 * 5
cant_seg = lustro * seg_lustro
print(lustro, "lustro(s) equivale a: ", cant_seg, "segundos")

#Ejercicio 5
luz = 299792
km_marte = 227943824
segundos = round(km_marte/luz)
print(f"{round(segundos/60)}")


#Ejercicio 6
from math import pi

3.141592653589793
diametro = 50

circunferencia = pi * diametro

print("En cada vuelta la rueda recorre", circunferencia, "cm")

"1 km = 100000 cm"
circunferencia2 = circunferencia/100000 

print("En cada vuelta la rueda recorre", circunferencia2, "km")

vueltas=1/circunferencia2

print("la rueda dará ", vueltas, "vueltas")

#Ejercicio 7
import math

cateto_opuesto= 20
angulo_elevacion= math.radians(22)

"Cateto adyacente: es la longitud de la sombra"

tan = math.tan(angulo_elevacion)

cateto_adyacente = cateto_opuesto/tan

print("la longitud de la sombra", cateto_adyacente, "metros")

#Ejercicio 8
age_User_one = int(input("Enter your age: "))
age_User_two = int(input("Enter your age: "))


same = age_User_one is age_User_two

print(same)

#Ejercicio 9

import datetime

edad = int(input("ingrese la edad: "))
dia = int(input("Día de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
anio = int(input("Año de nacimiento: "))


fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
fecha_de_hoy = datetime.datetime.now()
diferencia = fecha_de_hoy - fecha_de_nacimiento
dias_vividos = diferencia.days
meses_vividos = 12 * edad

mensaje = "Has vivido {} día(s), y {} meses".format(
    dias_vividos , meses_vividos)  
print(mensaje)

#Ejercicio 10

español =  float(input("Ingrese la nota de español: "))
matematicas = float(input("Ingrese la nota de matematicas: "))
economia = float(input("Ingrese la nota de economia: "))
programacion= float(input("Ingrese la nota programacion: "))
ingles = float(input("Ingrese la nota ingles: "))

Promedio = español+matematicas+economia+programacion+ingles 
Promedio = Promedio / 5

print("el promedio del alumno es de:", Promedio)
