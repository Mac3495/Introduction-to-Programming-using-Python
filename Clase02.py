print('Pan')
print('Salsas')
print('Tomate')
#Comentario 1
#Comentario 2
print('Carne')
print('Lechuga')
print('Pan')

#Variable
nombre_variable = 5
nombre_variable2 = 'Hola'
nombre_variable3 = False

#Numeros Enteros Negativos, Positivos...
numero1 = 10
numero2 = 2

#Numeros con decimal (float)
decimal1 = 2.5
decimal2 = 5.75

#Numeros complejos
complejo = 10j

#La funcion type() sirve para indicarnos el tipo de dato
print(type(decimal1))

numero3 = numero1 + numero2
print('La suma es: ')
print(numero3)

numero4 = numero1 - numero2
print('La resta es: ')
print(numero4)

numero5 = numero1 * numero2
print('El producto es: ', numero5)

numero6 = numero1 / numero2
print('La division es: ', numero6, type(numero6))

numero7 = numero1 // numero2
print('La division entera es: ', numero7, type(numero7))

numero8 = numero1 % numero2
print('El residuo es: ', numero8)

numero9 = numero1 ** numero2
print('El numero: ', numero1, ' elevado a la potencia: ', numero2, ' es igual a: ', numero9)

print(type(complejo))

#Strings

cadena1 = 'Hola '
cadena2 = 'Mundo'

cadena3 = cadena1 + cadena2 #'Hola Mundo'

cadena4 = cadena1 * 4

print('La longitud es: ', len(cadena3))

#sub Strings
cadena5 = cadena3[0:4] + '\n' + cadena3[5:10]
print('La sub cadena es: ', cadena5)

#Encontrar cadenas (si devuelve  -1 la sub cadena no se encontró en la cadena)
print(cadena3.find('Mundo'))

print(cadena3.upper())

cadena_mayusculas = "CORONAVIRUS"
print(cadena_mayusculas.lower())

print('La \n sub cadena\' es: ', cadena5)

print('''Aqui voy a escribir un parrafo
en python para no escribir una linea 
confusa y larga''')

print('Hola\tmundo')

#booleanos
Juan = 30 #30 años
Ariel = 18 #15 años

#Saber si son iguales
print(numero1 == numero2)
print(numero1 != numero2)
print(numero1 <= numero2)
print(numero1 >= numero2) # (> or =) -> True

print('======FIESTA=====')
print('Juan es mayor de edad? ', Juan >= 18)
print('Ariel es mayor de edad? ', Ariel >= 18)

if Ariel >= 18:
    print('Entra a la fiesta')
else:
    print('No entra a la fiesta')

cad1, cad2, cad3 = 'Hola', 10, True
print(type(cad1), type(cad2), type(cad3))

