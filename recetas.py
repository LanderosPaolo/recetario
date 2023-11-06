# Importamos os
import os

# Lista donde se guardaran las categorías
lista_categoria = []
# Lista donde se guardaran los archivos
recetas_en_carpeta = []

# Función principal
def iniciar_programa():
    print("-----------------------------------------------")
    print("-----> Bienvenido al baúl de las recetas <-----")
    print("-----------------------------------------------")
    # Obtiene el directorio actual del script
    directorio_actual = os.path.dirname(__file__)
    # Se agrega el directorio de las recetas
    rutas_recetas = os.path.join(directorio_actual, 'recetas')
    print(f"\n- Las recetas están ubicadas en la ruta: {rutas_recetas}")
    # Contamos la cantidad de carpetas que hay en la ruta gracias a contador_categorias
    contador_categorias = 0
    with os.scandir(rutas_recetas) as carpetas:
        for carpeta in carpetas:
            # En caso de ser un directorio, me suma 1 al contador
            if carpeta.is_dir():
                contador_categorias += 1
                nombre_carpeta = carpeta.name
                contador_recetas = 0
                # Para cada carpeta (categoria) se suma la cantidad de archivos dentro gracias a contador_recetas
                with os.scandir(carpeta.path) as recetas:
                    for receta in recetas:
                        if receta.is_file():
                            contador_recetas += 1
            print(f"- En la carpeta '{nombre_carpeta}', hay '{contador_recetas}' recetas")
    # Preguntamos al usuario que desea hacer con el programa
    respuesta_usuario = input("""\n¿Que quieres hacer?, estas son las opciones:
*Ingresa solo el número*
1.- Leer receta
2.- Crear receta
3.- Crear categoria
4.- Eliminar receta
5.- Eliminar categoria
6.- Finalizar programa
tu número: """)
    # En caso de poner algo distinto a los numeros que se le piden, volvera a preguntar
    while respuesta_usuario not in ["1","2","3","4","5","6"]:
        respuesta_usuario = input("""Necesito que ingreses uno de estos números
¿Que te gustaria hacer?
1.- Leer receta
2.- Crear receta
3.- Crear categoria
4.- Eliminar receta
5.- Eliminar categoria
6.- Finalizar programa
tu número: """)
    if respuesta_usuario == "1":
        leer_receta(rutas_recetas)
    elif respuesta_usuario == "2":
        crear_receta(rutas_recetas)
    elif respuesta_usuario == "3":
        crear_categoria(rutas_recetas)
    elif respuesta_usuario == "4":
        eliminar_receta(rutas_recetas)
    elif respuesta_usuario == "5":
        eliminar_categoria(rutas_recetas)
    elif respuesta_usuario == "6":
        finalizar_programa()

# Función que preguntara al usuario si quiere volver al menú principal después de finalizar una acción
def volver_menu():
    volver = input("Quieres volver al menu principal? si/no ")
    while volver not in ["si"]:
        volver = input("Quieres volver al menu principal? si/no ")
    if volver == "si":
        # Para windows, limpia la consola una vez llegado a este punto
        os.system("cls")
    # Se vuelve a iniciar el programa
    iniciar_programa()

# La función se encargara de listar las carpetas
def listado_carpetas(ruta):
    with os.scandir(ruta) as categorias:
        for carpeta in categorias:
            if carpeta.is_dir():
                nombre_carpeta = carpeta.name
                lista_categoria.append(nombre_carpeta)
                print(f" - {nombre_carpeta}")

# La función se encargara de listar los archivos dentro de cada carpeta
def listado_archivo(carpeta_seleccionada):
    with os.scandir(carpeta_seleccionada) as recetas:
        for receta in recetas:
            if receta.is_file():
                recetas_en_carpeta.append(receta.name)

# Función para leer las recetas
def leer_receta(ruta):
    print("Estas son las categorias:")
    listado_carpetas(ruta)
    respuesta_categoria = input("Que categoria quieres ver?: ").strip().lower()
    while respuesta_categoria not in lista_categoria:
        respuesta_categoria = input("Escribe la categoria: ").strip().lower()
    # Si la respuesta del usuario se encuentra en la lista, crea la ruta y llama a la función encargada de mostrar el archivo
    if respuesta_categoria in lista_categoria:
        carpeta_seleccionada = os.path.join(ruta, respuesta_categoria)
        listado_archivo(carpeta_seleccionada)
        print(f"En la carpeta '{respuesta_categoria}', están las siguientes recetas:")
        # Listamos los nombres de las recetas en dicha carpeta
        for nombre_receta in recetas_en_carpeta:
            print(f" - {nombre_receta}")
    respuesta_receta = input('Ingresa el nombre del archivo que contiene la receta que quieres ver: ')
    while respuesta_receta not in recetas_en_carpeta:
        respuesta_receta = input('Por favor ingresa el nombre del archivo que quieres ver: ')
    # Si la respuesta del usuario coincide con un archivo, le muestra la receta
    if respuesta_receta in recetas_en_carpeta:
        direccion = os.path.join(carpeta_seleccionada, respuesta_receta)
        try:
            archivo = open(direccion, 'r')
            print("*****************")
            print("Esta es la receta")
            print(archivo.read())
        except:
            print("No se ha podido cargar el archivo")
    volver_menu()

# Función para crear recetas
def crear_receta(ruta):
    print('En que categoria quieres crear una receta?')
    listado_carpetas(ruta)
    respuesta_categoria = input("Que categoria quieres ver?: ").strip().lower()
    # En caso de que la categoria seleccionada exista, podremos crear una receta dentro de esa carpeta
    while respuesta_categoria not in lista_categoria:
        respuesta_categoria = input("Escribe la categoria: ").strip().lower()
    if respuesta_categoria in lista_categoria:
        nombre_receta = input('Que nombre le pondras a la receta?: ')
        extension = ".txt"
        # Solo sera necesario escribir el nombre, se le agrega automaticamente el .txt
        nombre = f"{nombre_receta}{extension}"
        ruta_completa = os.path.join(ruta, respuesta_categoria, nombre)
        try:
            # Abrimos el archivo en modo escritura
            with open(ruta_completa, "w") as archivo:
                texto = input("Escribe la receta: ")
                archivo.write(texto)
                print("***********************")
                print("Receta creada con exito")
                print("***********************")
        except:
            print("El archivo no se pudo crear")
    volver_menu()

# Función para crear categoria
def crear_categoria(ruta):
    print('Estas son las categorias existentes:')
    listado_carpetas(ruta)
    # En caso de no existir la categoria podemos crearla
    nombre_nueva_categoria = input("Ingresa el nombre de la categoria a crear: ").strip().lower()
    # Si el nombre ya esta registrado en la lista, se nos da un aviso
    while nombre_nueva_categoria in lista_categoria:
        nombre_nueva_categoria = input("La categoria ya existe, ingresa otro nombre: ").strip().lower()
    if nombre_nueva_categoria not in lista_categoria:
        ruta_completa = os.path.join(ruta, nombre_nueva_categoria)
    try:
        os.mkdir(ruta_completa)
        print("************************")
        print("Carpeta creada con exito")
        print("************************")
    except:
        print("La carpeta no se pudo crear")
    volver_menu()

# Función para eliminar receta
def eliminar_receta(ruta):
    print("Estas son las categorias:")
    listado_carpetas(ruta)
    # Preguntamos al usuario que categoria desea ver
    respuesta_categoria = input("Que categoria quieres ver?: ").strip().lower()
    while respuesta_categoria not in lista_categoria:
        respuesta_categoria = input("Escribe la categoria: ").strip().lower()
    if respuesta_categoria in lista_categoria:
        carpeta_seleccionada = os.path.join(ruta, respuesta_categoria)
        listado_archivo(carpeta_seleccionada)
        # Mostramos las categorias
        print(f"En la carpeta '{respuesta_categoria}', están las siguientes recetas:")
        for nombre_receta in recetas_en_carpeta:
            print(f" - {nombre_receta}")
    respuesta_receta = input('Ingresa el nombre de la receta que deseas borrar: ')
    # En caso de no existir la categoria en el listado entramos al bucle
    while respuesta_receta not in recetas_en_carpeta:
        respuesta_receta = input('Por favor ingresa el nombre de la receta que quieres borrar: ')
    # Si el archivo existe comienza el proceso de borrado
    if respuesta_receta in recetas_en_carpeta:
        direccion = os.path.join(carpeta_seleccionada, respuesta_receta)
        try:
            os.remove(direccion)
            print("***************************")
            print("Archivo eliminado con exito")
            print("***************************")
        except:
            print("No se ha podido eliminar el archivo")
    volver_menu()

# Función para eliminar categoria
def eliminar_categoria(ruta):
    print('Estas son las categorías')
    listado_carpetas(ruta)
    respuesta_categoria = input("Que categoria te gustaria eliminar?: ")
    # Si no existe la categoria, volvemos a preguntar por el nombre
    while respuesta_categoria not in lista_categoria:
        print("El nombre de la categoria no existe")
        respuesta_categoria = input("Que categoria te gustaria eliminar?: ")
    # En caso de existir se elimina la categoria
    if respuesta_categoria in lista_categoria:
        direccion = os.path.join(ruta, respuesta_categoria)
        try:
            os.rmdir(direccion)
            print("*****************************")
            print("Categoría eliminada con exito")
            print("*****************************")
        except:
            print("No se ha podido eliminar la categoría")
    volver_menu()

# Función para finalizar el programa
def finalizar_programa():
    # Se le da un aviso al usuario y el programa finaliza
    return print("Muchas gracias por usar el recetario, vuelve luego!")

iniciar_programa()