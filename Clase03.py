numero1 = 10
numero2 = '20'

#Funciones de cast
'''
int(variable) -> convierte a número entero
float(variale) -> convierte a número con decimales
str(variable) -> convierte a cadena
bool(variable) -> convierte a booleano // 1 or ... -> True, 0 -> False
'''
cadena1 = str(numero1)
print(numero1 + int(numero2))

print(type(cadena1))


x = 138413974198
v_bool = bool(x)
print(v_bool)

#numero3 = int(input('Ingrese su un número: '))
#print(numero3, type(numero3))

#if
'''
if condition:
    ejecutar un código
else: 
    ejecutar otro código
'''
edad_juan = 30
edad_ariel = 15
dinero_juan = 50
dinero_ariel = 200

#Solo entran si tienen 100 o más
if edad_juan >= 18:
    if dinero_juan >= 100:
        print('Ingresó a la fiesta')
    else:
        print('No ingresó a la fiesta')
else:
    print('No ingresó a la fiesta')

#Admin, Dev, Gerente, Cliente

menu = '''
========= Menu ========
1. Admin
2. Dev
3. Gerente
4. Cliente
5. Salir
'''

print(menu)

user = int(input('Ingrese su usuario: '))
print(user)

# elif -> if: intrucciones else instrucciones
message = 'Bienvenido '
if user is 1:
    print(f'{message} Admin')
elif user is 2:
    print(f'{message} Dev')
elif user is 3:
    print(f'{message} Gerente')
elif user is 4:
    print(f'{message} Cliente')
elif user is 5:
    print('Programa finalizado')
else:
    print(f'La opción {user} no disponible')

#for
'''
for value in range:
    Código para ejecutar
'''

#Range
rango = range(5)
print(rango)

#for valor in rango:
#   print(valor)

lista_de_numero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if lista_de_numero[5] % 2 == 0:
    print(f'{lista_de_numero[5]}\tEs par')

#for con números
for number in lista_de_numero:
    print(f'{number}\tEs par' if number % 2 == 0 else f'{number}\tno es par')

#for con cadenas
cadenaX = 'Hola a todo el mundo'
for letra in cadenaX:
    if letra is 'a' or letra is 'e' or letra is 'i' or letra is 'o' or letra is 'u':
        print(f'{letra}\tes vocal')

#for anidados
numberY = int(input('Tablas de multiplicar'))
for numberY in range(1, numberY + 1):
    print('-----------')
    for multiplicador in range(1, 11):
        print(f'{numberY} * {multiplicador}\t=\t{numberY*multiplicador}')

#Ingresar un número ej. 1234 y devolver 4321 (Usar un solo for)
#Generar los primero 'n' números primos 2, 3, 5, 7, 9, 11, 13, 17... (for for if)
