#Autor: Israel
#Version: 1.0

#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.

cadena1 = input("Dime una palabra palindroma: ")

if cadena1 == cadena1[::-1]:
    print(f"La palabra {cadena1} es palindroma.")
else:
    print(f"La palabra {cadena1} no es palindroma.")