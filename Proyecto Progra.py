from tkinter import *
import os
import random

ganador = 0
contador = 5
letras_usadas = []

# ----MENU INICIAL----
def menuprincipal():
    global menu
    menu = Frame(width=300, height=250)
    menu.pack()

    Label(menu, text='Ahorcado', bg='LightSkyBlue1', width=300, height=2, font=('Calibri', 13)).pack()
    Label(menu, text='').pack()
    Button(menu, text='Iniciar Sesion', width=20, height=1, cursor='hand2', command=menu_iniciarsesion).pack()
    Label(menu, text='').pack()
    Button(menu, text='Registrar', width=20, height=1, cursor='hand2', command=menu_registrar).pack()


# ----MENU DE INICIO DE SESION----
def menu_iniciarsesion():
    menu.destroy()

    global iniciarsesion_frame
    iniciarsesion_frame = Frame(width=300, height=250)
    iniciarsesion_frame.pack()

    global verificar_usuario
    global verificar_contra

    verificar_usuario = StringVar()
    verificar_contra = StringVar()

    global usuario_login_entry
    global contra_login_entry

    Label(iniciarsesion_frame, text='Iniciar Sesion', bg='LightSkyBlue1', width=300, height=2).pack()
    Label(iniciarsesion_frame, text='').pack()
    Label(iniciarsesion_frame, text='Usuario').pack()
    usuario_login_entry = Entry(iniciarsesion_frame, textvariable=verificar_usuario)
    usuario_login_entry.pack()
    Label(iniciarsesion_frame, text='').pack()
    Label(iniciarsesion_frame, text='Contrasenia').pack()
    contra_login_entry = Entry(iniciarsesion_frame, textvariable=verificar_contra, show='*')
    contra_login_entry.pack()
    Label(iniciarsesion_frame, text='').pack()
    Button(iniciarsesion_frame, text='Iniciar Sesion', width=10, height=1, cursor='hand2', command=iniciarsesion).pack()
    Button(iniciarsesion_frame, text='Regresar', width=10, height=1, cursor='hand2', command=regresarmenu_iniciarsesion).pack()


# ----MENU DE REGISTRO----
def menu_registrar():
    menu.destroy()

    global registrar_frame
    registrar_frame = Frame(width=300, height=250)
    registrar_frame.pack()

    global usuario
    global contra
    global usuario_register_entry
    global contra_register_entry

    usuario = StringVar()
    contra = StringVar()

    Label(registrar_frame, text='Intrdduce los datos', bg='LightSkyBlue1', width=300, height=2).pack()
    Label(registrar_frame, text='').pack()
    Label(registrar_frame, text='Usuario').pack()
    usuario_register_entry = Entry(registrar_frame, textvariable=usuario)
    usuario_register_entry.pack()
    Label(registrar_frame, text='').pack()
    Label(registrar_frame, text='Contrasenia').pack()
    contra_register_entry = Entry(registrar_frame, textvariable=contra, show='*')
    contra_register_entry.pack()
    Label(registrar_frame, text="").pack()
    Button(registrar_frame, text='Registrar', width=10, height=1, cursor='hand2', command=registrar).pack()
    Button(registrar_frame, text='Regresar', width=10, height=1, cursor='hand2', command=regresarmenu_registrar).pack()


# ----EVENTO BOTON REGRESAR (INICIAR SESION)----
def regresarmenu_iniciarsesion():
    iniciarsesion_frame.destroy()
    menuprincipal()


# ----EVENTO BOTON REGRESAR (REGISTRAR)----
def regresarmenu_registrar():
    registrar_frame.destroy()
    menuprincipal()


# ----EVENTO BOTON DE INICIO DE SESION----
def iniciarsesion():
    usuario1 = verificar_usuario.get()
    contra1 = verificar_contra.get()

    list_of_files = os.listdir()
    if usuario1 in list_of_files:
        archivo1 = open(usuario1, 'r')
        verificar = archivo1.read().splitlines()
        if contra1 in verificar:
            iniciar()
        else:
            contra_incorrecta()
    else:
        usuario_incorrecto()


# ----BOTON DE REGISTRO----
def registrar():
    usuario_info = usuario.get()
    contra_info = contra.get()

    archivo = open(usuario_info, 'w')
    archivo.write(usuario_info + '\n')
    archivo.write(contra_info)
    archivo.close()

    Label(registrar_frame, text='Registro realizado con exito').pack()

    usuario_register_entry.delete(0, END)
    contra_register_entry.delete(0, END)


# ----CONTRASENIA INCORRECTA----
def contra_incorrecta():
    global contra_ventana
    contra_ventana = Toplevel(main)
    contra_ventana.title('Incorrecta')
    contra_ventana.geometry('150x100')
    contra_ventana.transient(main)

    Label(contra_ventana, text='Contrasenia Incorrecta').pack()
    Label(contra_ventana, text='').pack()
    Button(contra_ventana, text='OK', cursor='hand2', command=eliminarcontra_ventana).pack()

    usuario_login_entry.delete(0, END)
    contra_login_entry.delete(0, END)


# ----USUARIO INCORREECTO----
def usuario_incorrecto():
    global usuario_ventana
    usuario_ventana = Toplevel(main)
    usuario_ventana.title('Incorrecta')
    usuario_ventana.geometry('150x100')
    usuario_ventana.transient(main)

    Label(usuario_ventana, text='Usuario Incorrecto').pack()
    Label(usuario_ventana, text='').pack()
    Button(usuario_ventana, text='OK', cursor='hand2', command=eliminarusuario_ventana).pack()

    usuario_login_entry.delete(0, END)
    contra_login_entry.delete(0, END)


# ----BOTON ELIMINAR VENTANA CONTRASENIA INCORRECTA----
def eliminarcontra_ventana():
    contra_ventana.destroy()


# ----BOTON ELIMINAR VENTANA USUARIO INCORRECTO----
def eliminarusuario_ventana():
    usuario_ventana.destroy()


# ----INICIO DE SESION EXITOSO----
def iniciar():
    iniciarsesion_frame.destroy()

    main.geometry('300x300')

    menu_juego()


# ----MENU JUEGO----
def menu_juego():
    global menujuego_frame
    menujuego_frame = Frame(width=300, height=300)
    menujuego_frame.pack()

    Label(menujuego_frame, text='Elige una categoria', bg='LightSkyBlue1', width=33, height=2, font=('Calibri', 13)).place(x=0, y=0)
    Button(menujuego_frame, text='Matematicas',cursor='hand2', width=10, height=1, command=juego).place(x=110, y=75)
    Button(menujuego_frame, text='Efemerides', cursor='hand2', width=10, height=1).place(x=110, y=125)
    Button(menujuego_frame, text='Capitales', cursor='hand2', width=10, height=1).place(x=110, y=175)
    Button(menujuego_frame, text='Como jugar', cursor='hand2', width=10, height=1, command=comojugar).place(x=55, y=225)
    Button(menujuego_frame, text='Cerrar Sesion', cursor='hand2', width=10, height=1, command=cerrarsesion).place(x=165, y=225)


# ----BOTON MATEMATICAS----



# ----BOTON EFEMERIDES----



# ----BOTON CAPITALES----



# ----PALABRA A ADIVNIAR----
'''def palabra_menu():
    menujuego_frame.destroy()
    main.geometry('300x400')

    global palabra_frame
    palabra_frame = Frame(width=300, height=400)
    palabra_frame.pack()

    global palabra

    palabra = StringVar()

    Label(palabra_frame, text='Introduce la palabra a adivinar:', bg='LightSkyBlue1', width=300, height=2, font=('Calibri',13)).pack()
    Label(palabra_frame, text='').pack()
    Entry(palabra_frame, textvariable=palabra, show='*').pack()
    Label(palabra_frame, text='').pack()
    Button(palabra_frame, text='Aceptar', cursor='hand2', width=10, height=1, command=juego).pack()'''

# ----pregunta----
'''def pregunta_menu():
    juego_frame.destroy()
    main.geometry('300x400')

    global pregunta_frame
    pregunta_frame = Frame(width=300, height=400)
    pregunta_frame.pack()

    global palabra

    palabra = StringVar()

    Label(palabra_frame, text='Pregunta:', bg='LightSkyBlue1', width=300, height=2, font=('Calibri',13)).pack()'''


# ----JUEGO----
def juego():
    global contador
    contador = 5
    menujuego_frame.destroy()

    global juego_frame
    global ran
    global lista_palabras
    global lenght

    juego_frame = Frame(width=300, height=400)
    juego_frame.pack()

    global palabra
    global letra
    letra = StringVar()

    global letra_entry
    letra_entry = Entry(juego_frame, textvariable=letra, width=10)
    letra_entry.place(x=110, y=20)

    global ahorcado


# ----SACAR PALABRA RANDOM DE ARCHIVO----
    archivo = open("palabras.txt", "r")
    line = archivo.readline()
    lista_palabras = line.split(";")
    ran = random.randint(2, 9)
    lenght = len(lista_palabras[ran])
    print("Word: " + lista_palabras[ran])
    print("Lenght: " + str(lenght))

    palabra = lista_palabras[ran]

# ----CREACION DE CUADROS CON _ ----
    for i in range(lenght):
        cambia_x = i*20
        c = Label(juego_frame, text='_', bg='LightSkyBlue1', width=1, font= "Calibri 20")
        c.place(x=20+cambia_x, y=60)
    Button(juego_frame, text='Checar', cursor='hand2', width=10, height=1, command=display_text).place(x=20, y=120)

    imagen = PhotoImage(file='ahorcado.gif')
    ahorcado_imagen = Label(juego_frame, image=imagen, width= 150, height=170, bg='white')
    ahorcado_imagen.place(x=120, y=120)


# ----SACAR PALABRA RANDOM DE ARCHIVO----
def display_text():
    global check

    archivo = open("palabras.txt", "r")
    line = archivo.readline()
    lista_palabras = line.split(";")
    check = lista_palabras[ran]

    verificar_juego()


# ----VERIFICAR SI LAS LETRAS EXISTEN O NO----
def verificar_juego():
    Label(juego_frame, text='', width=30, height=1).place(x=0, y=150)
    global contador
    global letras_usadas
    global palabra
    global ganador

    suma = 0

    for i in range(lenght):
        cambia_x = i*20
        if check[i] == letra.get():
            palabra = palabra.replace(palabra[i], ' ')
            ganador = ganador + 1
            suma = suma + 1
            if letra.get() in letras_usadas:
                Label(juego_frame, text='Letra ya utilizada', width=20, height=1).place(x=0, y=150)
                ganador = ganador - 1
            Label(juego_frame, text=check[i], bg='LightSkyBlue1', width=1, font= "Calibri 20").place(x=20+cambia_x, y=60)
        elif letra.get() == '':
            suma = suma + 1
            Label(juego_frame, text='Introduce una letra', width=19, height=1).place(x=0, y=150)
    if suma == 0:
        contador = contador - 1
        Label(juego_frame, text='Letra incorrecta', width=15, height=1).place(x=8, y=150)

    letras_usadas.append(letra.get())
    letra_entry.delete(0, END)


# ----EVENTOS AL PERDER O GANAR----
    if contador < 0:
        juego_frame.destroy()
        global perdiste_frame
        perdiste_frame = Frame(width=300, height=400)
        perdiste_frame.pack()

        Label(perdiste_frame, text='PERDISTE', bg='LightSkyBlue1', width=50, height=2, font=('Calibri', 32)).pack()
        Label(perdiste_frame, text='').pack()
        Button(perdiste_frame, text='Volver a jugar', cursor='hand2', width=10, height=2, command=volverajugar_perdiste).pack()
        Label(perdiste_frame, text='').pack()
        Button(perdiste_frame, text='Menu', cursor='hand2', width=10, height=2, command=menu_perdiste).pack()

    elif ganador == lenght:
        juego_frame.destroy()
        global ganaste_frame
        ganaste_frame = Frame(width=300, height=400)
        ganaste_frame.pack()

        Label(ganaste_frame, text='GANASTE', bg='LightSkyBlue1', width=50, height=2, font=('Calibri', 32)).pack()
        Label(ganaste_frame, text='').pack()
        Button(ganaste_frame, text='Volver a jugar', cursor='hand2', width=10, height=2, command=volverajugar_ganaste).pack()
        Label(ganaste_frame, text='').pack()
        Button(ganaste_frame, text='Menu', cursor='hand2', width=10, height=2, command=menu_ganaste).pack()


# ----BOTON VOLVER A JUGAR (PERDISTE)
def volverajugar_perdiste():
    perdiste_frame.destroy()
    juego()

# ----BOTON MENU(PERDISTE)
def menu_perdiste():
    perdiste_frame.destroy()
    menu_juego()


# ----BOTON VOLVER A JUGAR (PERDISTE)
def volverajugar_ganaste():
    ganaste_frame.destroy()
    juego()

# ----BOTON MENU(PERDISTE)
def menu_ganaste():
    ganaste_frame.destroy()
    menu_juego()


# ----COMO JUGAR BOTON----
def comojugar():
    global comojugar_ventana
    comojugar_ventana = Toplevel(main)
    comojugar_ventana.title('Como Jugar')
    comojugar_ventana.transient(main)
    comojugar_ventana.geometry('350x400')

    comojugar_frame = Frame(comojugar_ventana, width=320, height=400)
    comojugar_frame.pack()

    Label(comojugar_frame, text='¿Cómo jugar?', bg='LightSkyBlue1', width=350, height=2, font=('Calibri', 13)).pack()
    Label(comojugar_frame, text='').pack()
    Label(comojugar_frame, text='1.-Escoge una categoría para las preguntas dentro\ndel juego (Matemáticas, Efemérides, Estados y capitales)\n\n2.-Al iniciar el juego se seleccionara una palabra al asar.\n\n3.-Para poder adivinar una letra, deberás contestar una pregunta\ndel tema que elegiste, de ser contestada correctamente, podrás\nintroducir la letra que quieras.\n\n4.-El objetivo final del juego será completar la palabra oculta\n\n5.-Por cada letra incorrecta, se ira completando el dibujo del\nahorcado, cuando este completo, se termina el juego.').pack()

# ----CERRAR SESION BOTON----
def cerrarsesion():
    menujuego_frame.destroy()
    main.geometry('300x250')
    menuprincipal()


# ----VENTANA PRINCIPAL----
main = Tk()
main.title('Ahorcado')
main.geometry('300x250')
main.resizable(0, 0)


# ----INICIAR MENU INICIAL----
menuprincipal()

main.mainloop()
