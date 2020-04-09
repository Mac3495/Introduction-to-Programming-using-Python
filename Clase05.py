#Declarando los recursos que se van a utilizar en el programa

lista_de_frutas = []

sw = True

#Lógica del programa


#PEP8 ->

def listar_frutas():
    if len(lista_de_frutas) == 0:
        print('Lista vacia')
    else:
        print(lista_de_frutas)


def agregar_fruta():
    fruta = input('Ingrese la fruta: ')
    lista_de_frutas.append(fruta)
    print('Fruta agregada!')


def fruta_existente(fruta):
    if fruta in lista_de_frutas:
        return True
    else:
        return False


def buscar_fruta():
    fruta_buscar = input('Ingrese la fruta a buscar: ')
    if fruta_existente(fruta_buscar):
        print('La fruta esta disponible')
    else:
        print('La fruta no esta disponible')


def eliminar_fruta():
    fruta_eliminar = input('Ingrese la fruta a comprar: ')
    if fruta_existente(fruta_eliminar):
        print('Fruta comprada')
        lista_de_frutas.remove(fruta_eliminar)
    else:
        print('La fruta no esta disponible')


def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False


def opcion_no_disponible():
    print('Opcion no disponible')




#La interfaz del usuario
menu = '''
======= Tiendita ======
1. Listar Frutas
2. Agregar Fruta
3. Buscar Fruta
4. Borrar Fruta
5. Salir
'''

# is == ; not is !=

while sw:
    print(menu)
    opcion = int(input('Ingrese la opcion: '))
    if opcion == 1:
        listar_frutas()
    elif opcion == 2:
        agregar_fruta()
    elif opcion == 3:
        buscar_fruta()
    elif opcion is 4:
        eliminar_fruta()
    elif opcion is 5:
        terminar_programa()
    else:
        opcion_no_disponible()


#Funciones y metodós o procedimientos
'''
==== Funciones ====
def nombre_funcion():
    código a ejecutar
    return algo -> Valor que devuelve la función
    
==== Métodos o Procedimiento ====
def nombre_metodo():
    código a ejecutar -> No devuelve ningun valor
    
==== Parametros ====
def funcion_X(parametro1, parametro2, ...):
    variable = parametro1 + parametro2
'''


def funcion():
    return 'Hola mundo'


def funcion_promedio(numeroA, numeroB):
    return (numeroA + numeroB) / 2


def metodo_promedio(numeroA, numeroB):
    print((numeroA + numeroB) / 2)


saludo = funcion()
print(saludo)

numero1, numero2 = 5, 10
promedio = (20 + 50) / 2
print(promedio)

prom1 = funcion_promedio(numero1, numero2)
print(prom1)

metodo_promedio(numero1, numero2)
print('Argumento')

cadena = 'HOLA MUNDO'

print(cadena.lower())

