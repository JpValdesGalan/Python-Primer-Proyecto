from tkinter import *
import os

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

    #global usuario_login_entry
    #global contra_login_entry

    Label(iniciarsesion_frame, text='Iniciar Sesion', bg='LightSkyBlue1', width=300, height=2).pack()
    Label(iniciarsesion_frame, text='').pack()
    Label(iniciarsesion_frame, text='Usuario').pack()
    Entry(iniciarsesion_frame, textvariable=verificar_usuario).pack()
    Label(iniciarsesion_frame, text='').pack()
    Label(iniciarsesion_frame, text='Contrasenia').pack()
    Entry(iniciarsesion_frame, textvariable=verificar_contra, show='*').pack()
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
    #global usuario_register_entry
    #global contra_register_entry

    usuario = StringVar()
    contra = StringVar()

    Label(registrar_frame, text='Intrdduce los datos', bg='LightSkyBlue1', width=300, height=2).pack()
    Label(registrar_frame, text='').pack()
    Label(registrar_frame, text='Usuario').pack()
    Entry(registrar_frame, textvariable=usuario).pack()
    Label(registrar_frame, text='').pack()
    Label(registrar_frame, text='Contrasenia').pack()
    Entry(registrar_frame, textvariable=contra, show='*').pack()
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

    menujuego()


# ----MENU JUEGO----
def menujuego():
    global menujuego_frame
    menujuego_frame = Frame(width=300, height=300)
    menujuego_frame.pack()

    Label(menujuego_frame, text='Elige una categoria', bg='LightSkyBlue1', width=33, height=2, font=('Calibri', 13)).place(x=0, y=0)
    Button(menujuego_frame, text='Matematicas',cursor='hand2', width=10, height=1, command=palabra_menu).place(x=110, y=75)
    Button(menujuego_frame, text='Efemerides', cursor='hand2', width=10, height=1).place(x=110, y=125)
    Button(menujuego_frame, text='Capitales', cursor='hand2', width=10, height=1).place(x=110, y=175)
    Button(menujuego_frame, text='Como jugar', cursor='hand2', width=10, height=1, command=comojugar).place(x=55, y=225)
    Button(menujuego_frame, text='Cerrar Sesion', cursor='hand2', width=10, height=1, command=cerrarsesion).place(x=165, y=225)


# ----BOTON MATEMATICAS----



# ----BOTON EFEMERIDES----



# ----BOTON CAPITALES----



# ----PALABRA A ADIVNIAR----
def palabra_menu():
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
    Button(palabra_frame, text='Aceptar', cursor='hand2', width=10, height=1, command=juego).pack()


# ----JUEGO----
def juego():
    palabra_frame.destroy()

    global juego_frame
    juego_frame = Frame(width=300, height=400)
    juego_frame.pack()




# ----COMO JUGAR BOTON----
def comojugar():
    global comojugar_ventana
    comojugar_ventana = Toplevel(main)
    comojugar_ventana.title('Como Jugar')
    comojugar_ventana.transient(main)
    comojugar_ventana.geometry('200x400')


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
