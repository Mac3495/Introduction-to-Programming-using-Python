#while
'''
while condicion -> True:
    condicion -> False
'''

sw = True
'''numero = 0
while sw:
    #numero = numero + 1
    numero += 1
    print(numero)
    if numero >= 5:
        sw = False'''
'''
while sw:
    menu = 
    ========= Menu ========
    1. Admin
    2. Dev
    3. Gerente
    4. Cliente
    5. Salir
    

    print(menu)

    user = int(input('Ingrese su usuario: '))
    print(user)

    # elif -> if: intrucciones else instrucciones
    message = 'Bienvenido '
    if user is 1:
        print(f'{message} Admin')
        sw = False
    elif user is 2:
        print(f'{message} Dev')
        sw = False
    elif user is 3:
        print(f'{message} Gerente')
        sw = False
    elif user is 4:
        print(f'{message} Cliente')
        sw = False
    elif user is 5:
        print('Programa finalizado')
        sw = False
    else:
        print(f'La opción {user} no disponible')
'''
#Tuplas no son mutables
tupla = ('Marcelo', 123, True)
print(tupla)

variable1, variable2, variable3 = tupla
print(f'v1 = {variable1} v2 = {variable2}, v3 = {variable3}')

nombre = tupla[0]
print(nombre)

#Listas si son mutables
lista= ['Cadenas', 21, True]
print(lista)

lista_de_frutas = ['Manzana', 'Uva', 'Frutilla']
print(lista_de_frutas)

lista_de_frutas.append('Banana')
print(lista_de_frutas)

lista_de_frutas += ['Sandia', 'Naranja']
print(lista_de_frutas)

lista_de_frutas += ['Durazno']
print(lista_de_frutas)

print(lista_de_frutas[2])

lista_de_frutas[2] = 'Piña'
print(lista_de_frutas)

print(lista_de_frutas[0], lista_de_frutas[6])

#For importante
for value in range(len(lista_de_frutas)):
    print(f'{value}\t->\t{lista_de_frutas[value]}')

for fruta in lista_de_frutas:
    print(fruta)

lista_de_frutas.insert(2, 'Frutilla')
print(lista_de_frutas)

lista_de_frutas.pop()
print(lista_de_frutas)

lista_de_frutas.reverse()
print(lista_de_frutas)

lista_de_frutas.remove('Manzana')
print(lista_de_frutas)

lista_de_frutas.remove('Banana')
print(lista_de_frutas)

#Diccionarios
'''
diccionario{'key':'valor', 'key2':'valor2'}
'''
tupla2 = ()
lista2 = []
diccionario = {'nombre': 'Marcelo', 'numero': 321, 'estudiante': True, 'notas': [51, 51, 51]}
print(diccionario)

print(diccionario.keys())
print(diccionario.values())

#Tarea 2
#Crear un pequeño sistemita de ventas de fruta
#Lista de frutas
#menu
#Agregar una fruta
#Ver si la fruta esta disponible
#Eliminar frutar

