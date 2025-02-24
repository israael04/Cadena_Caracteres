#Autor: Israel
#Version: 1.0

#Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

cadena1 = input("Dime una cadena de caracteres: ")
cadena2 = ""

for caracter in cadena1:
    if caracter == caracter.upper():
        cadena2 += caracter.lower()
    elif caracter == caracter.lower():
        cadena2 += caracter.upper()
print(f"Cadena es: {cadena2}")