#Autor: Israel
#Version: 1.0

#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.

cadena1 = input("Dime una cadena de caracteres: ")
caracter1 = input("Dime un caracter: ")
caracter2 = input("Dime un segundo caracter: ")

if len(caracter1)==1 and len(caracter2)==1:
    cadena_invertida = cadena1.replace(caracter1,caracter2)
    print(f"La cadena invertida es: {cadena_invertida}")
else:
    print("No has introducido caracteres.")
