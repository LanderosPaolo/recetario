# Importamos os
import os
# Importamos Path
from pathlib import Path

categoria = []
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
    print(f"\n- Las recetas estan ubicadas en la ruta: {rutas_recetas}")
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
    match respuesta_usuario:

        case "1":
            leer_receta(nombre_carpeta, rutas_recetas)
        case "2":
            crear_receta(nombre_carpeta, rutas_recetas)
        case "3":
            crear_categoria(rutas_recetas)
        case "4":
            eliminar_receta(nombre_carpeta, rutas_recetas)
        case "5":
            eliminar_categoria(nombre_carpeta, rutas_recetas)
        case "6":
            finalizar_programa()

# Función para leer las recetas
def leer_receta(categorias, ruta):
    print("Estas son las categorias:")
    with os.scandir(ruta) as categorias:
        for carpeta in categorias:
            if carpeta.is_dir():
                nombre_carpeta = carpeta.name
                categoria.append(nombre_carpeta)
                print(f" - {nombre_carpeta}")
        respuesta_categoria = input("Que categoria quieres ver?: ").strip().lower()
        while respuesta_categoria not in categoria:
            respuesta_categoria = input("Escribe la categoria: ").strip().lower()
        if respuesta_categoria in categoria:
            carpeta_seleccionada = os.path.join(ruta, respuesta_categoria)
            with os.scandir(carpeta_seleccionada) as recetas:
                for receta in recetas:
                    if receta.is_file():
                        recetas_en_carpeta.append(receta.name)
            print(f"En la carpeta '{respuesta_categoria}', están las siguientes recetas:")
            for nombre_receta in recetas_en_carpeta:
                print(f" - {nombre_receta}")
        respuesta_receta = input('Ingresa el nombre del archivo que contiene la receta que quieres ver: ')
        while respuesta_receta not in recetas_en_carpeta:
            respuesta_receta = input('Por favor ingresa el nombre del archivo que quieres ver: ')
        if respuesta_receta in recetas_en_carpeta:
            direccion = Path(carpeta_seleccionada, respuesta_receta)
            try:
                archivo = open(direccion, 'r')
                print("*****************")
                print("Esta es la receta")
                print(archivo.read())
            except:
                print("No se ha podido cargar el archivo")

# Función para crear recetas
def crear_receta(categorias, ruta):
    print('En que categoria quieres crear una receta?')
    with os.scandir(ruta) as categorias:
        for carpeta in categorias:
            if carpeta.is_dir():
                nombre_carpeta = carpeta.name
                categoria.append(nombre_carpeta)
                print(f" - {nombre_carpeta}")
        respuesta_categoria = input("Que categoria quieres ver?: ").strip().lower()
        while respuesta_categoria not in categoria:
            respuesta_categoria = input("Escribe la categoria: ").strip().lower()
        if respuesta_categoria in categoria:
            nombre_receta = input('Que nombre le pondras a la receta?: ')
            extension = ".txt"
            nombre = f"{nombre_receta}{extension}"
            ruta_completa = os.path.join(ruta, respuesta_categoria, nombre)
            try:
                with open(ruta_completa, "w") as archivo:
                    texto = input("Escribe la receta: ")
                    archivo.write(texto)
                    print("Receta creada con exito")
            except:
                print("El archivo no se pudo crear")

# Función para crear categoria
def crear_categoria(ruta):
    print('Estas son las categorias existentes:')
    with os.scandir(ruta) as categorias:
        for carpeta in categorias:
            if carpeta.is_dir():
                nombre_carpeta = carpeta.name
                categoria.append(nombre_carpeta)
                print(f" - {nombre_carpeta}")
    nombre_nueva_categoria = input("Ingresa el nombre de la categoria a crear: ")
    ruta_completa = os.path.join(ruta, nombre_nueva_categoria)
    try:
        os.mkdir(ruta_completa)
        print("Carpeta creada con exito")
    except:
        print("La carpeta no se pudo crear")

# Función para eliminar receta
def eliminar_receta(categorias, ruta):
    print("Estas son las categorias:")
    with os.scandir(ruta) as categorias:
        for carpeta in categorias:
            if carpeta.is_dir():
                nombre_carpeta = carpeta.name
                categoria.append(nombre_carpeta)
                print(f" - {nombre_carpeta}")
        respuesta_categoria = input("Que categoria quieres ver?: ").strip().lower()
        while respuesta_categoria not in categoria:
            respuesta_categoria = input("Escribe la categoria: ").strip().lower()
        if respuesta_categoria in categoria:
            carpeta_seleccionada = os.path.join(ruta, respuesta_categoria)
            with os.scandir(carpeta_seleccionada) as recetas:
                for receta in recetas:
                    if receta.is_file():
                        recetas_en_carpeta.append(receta.name)
            print(f"En la carpeta '{respuesta_categoria}', están las siguientes recetas:")
            for nombre_receta in recetas_en_carpeta:
                print(f" - {nombre_receta}")
        respuesta_receta = input('Ingresa el nombre de la receta que deseas borrar: ')
        while respuesta_receta not in recetas_en_carpeta:
            respuesta_receta = input('Por favor ingresa el nombre de la receta que quieres borrar: ')
        if respuesta_receta in recetas_en_carpeta:
            direccion = Path(carpeta_seleccionada, respuesta_receta)
            try:
                os.remove(direccion)
                print("*****************")
                print("Archivo eliminado con exito")
            except:
                print("No se ha podido eliminar el archivo")

# Función para eliminar categoria
def eliminar_categoria(categorias, ruta):
    print('Estas son las categorías')
    with os.scandir(ruta) as categorias:
        for carpeta in categorias:
            if carpeta.is_dir():
                nombre_carpeta = carpeta.name
                categoria.append(nombre_carpeta)
                print(f" - {nombre_carpeta}")
    respuesta_categoria = input("Que categoria te gustaria eliminar?: ")
    while respuesta_categoria not in categoria:
        print("El nombre de la categoria no existe")
        respuesta_categoria = input("Que categoria te gustaria eliminar?: ")
    if respuesta_categoria in categoria:
        direccion = Path(ruta, respuesta_categoria)
        try:
            os.rmdir(direccion)
            print("*****************************")
            print("Categoría eliminada con exito")
            print("*****************************")
        except:
            print("No se ha podido eliminar la categoría")
    
# Función para finalizar el programa
def finalizar_programa():
    return print("Muchas gracias por usar el recetario, vuelve luego!")

iniciar_programa()