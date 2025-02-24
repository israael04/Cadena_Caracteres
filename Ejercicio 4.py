#Autor: Israel
#Version: 1.0

#Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

cadena1 = input("Dime una cadena: ")
cadena2 = input("Dime una subcadena: ")

if cadena1.count(cadena2) > 0:
    print(f"La subcadena {cadena2} si esta.")
else:
    print(f"La subcadena {cadena2} no esta.")