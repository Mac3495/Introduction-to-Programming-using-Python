#tkinter
import tkinter as tk
# Declarando los recursos que se van a utilizar en el programa

lista_de_frutas = []
root = tk.Tk()

fruta_agregada = tk.StringVar()
fruta_buscada = tk.StringVar()
fruta_comprada = tk.StringVar()
mensaje = tk.StringVar()

sw = False


def listar_frutas():
    if len(lista_de_frutas) == 0:
        print('Lista vacia')
        mensaje.set('Lista vacia')
    else:
        print(lista_de_frutas)
        mensaje.set(str(lista_de_frutas))


def agregar_fruta():
    fruta = fruta_agregada.get()
    lista_de_frutas.append(fruta)
    mensaje.set('Fruta agregada!')
    fruta_agregada.set('')
    print('Fruta agregada!')


def fruta_existente(fruta):
    if fruta in lista_de_frutas:
        return True
    else:
        return False


def buscar_fruta():
    fruta_buscar = fruta_buscada.get()
    if fruta_existente(fruta_buscar):
        mensaje.set('La fruta esta disponible')
        fruta_buscada.set('')
        print('La fruta esta disponible')
    else:
        mensaje.set('La fruta no esta disponible')
        fruta_buscada.set('')
        print('La fruta no esta disponible')


def eliminar_fruta():
    fruta_eliminar = fruta_comprada.get()
    if fruta_existente(fruta_eliminar):
        mensaje.set('Fruta comprada')
        print('Fruta comprada')
        lista_de_frutas.remove(fruta_eliminar)
        fruta_comprada.set('')
    else:
        mensaje.set('La fruta no esta disponible')
        print('La fruta no esta disponible')
        fruta_comprada.set('')



root.geometry('800x500')
root.title('Tiendita de frutas')

root.configure(bg="#009688")

tk.Label(root, text='TIENDITA DE FRUTAS', bg="#009688", fg='white', font=('', 32)).place(x=250, y=30)

#Listar
tk.Label(root, text='LISTAR FRUTAS', bg="#009688", fg='white', font=('', 24)).place(x=30, y=120)
tk.Button(root, text='Listar', bd=0, command=listar_frutas).place(x=220, y=120)

#Agregar
tk.Label(root, text='AGREGAR FRUTA', bg="#009688", fg='white', font=('', 24)).place(x=30, y=170)
tk.Entry(root, justify='center', textvariable=fruta_agregada).place(x=250, y=170)
tk.Button(root, text='Agregar', bd=0, command=agregar_fruta).place(x=500, y=170)

#Buscar
tk.Label(root, text='BUSCAR FRUTA', bg="#009688", fg='white', font=('', 24)).place(x=30, y=230)
tk.Entry(root, justify='center', textvariable=fruta_buscada).place(x=250, y=230)
tk.Button(root, text='Buscar', bd=0, command=buscar_fruta).place(x=500, y=230)

#Comprar
tk.Label(root, text='COMPRAR FRUTA', bg="#009688", fg='white', font=('', 24)).place(x=30, y=290)
tk.Entry(root, justify='center', textvariable=fruta_comprada).place(x=250, y=290)
tk.Button(root, text='Comprar', bd=0, command=eliminar_fruta).place(x=500, y=290)

tk.Label(root, textvariable=mensaje, bg="#009688", fg='white', font=('', 24)).place(x=300, y=410)
tk.Button(root, text='Salir', bd=0, command=root.destroy).place(x=400, y=450)

root.mainloop()

# Lógica del programa


# PEP8 ->






def terminar_programa():
    print('Fin del programa')
    global sw
    sw = False


def opcion_no_disponible():
    print('Opcion no disponible')


# La interfaz del usuario
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

# Funciones y metodós o procedimientos
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

