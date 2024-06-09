#Bautista Santos Tapia
from data_stark_03 import lista_personajes
import re
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

#Recibe: un string con el nombre de un personaje.
#Hace: verifica que la lista no este vacia, cambia el guion por un espacio en blanco y separa las primeras etra de cada palabra.
#Retorna: las iniciales de ese nombre, seguidos por un punto, sin el the o "N\A" en caso de que algo haya salido mal.
def extraer_iniciales(nombre_heroe:str):
    if len(nombre_heroe) > 0:
        nombre = nombre_heroe.replace("-"," ")
        palabras = nombre.split()
        primeras_letras = ""
        for palabra in palabras:
            if palabra != "The" and palabra != "the":
                primeras_letras = primeras_letras + palabra[0] + "."
        return primeras_letras
    else:
        return "N/A"

print(f"1.1 = {extraer_iniciales(lista_personajes[1]['nombre'])}")


#Recibe: un dato en formato string.
#Hace: valida que sea un string, lo pasa a minuscula y remplaza signos para lograr un formato snake_case.
#Retorna: el dato en formato snake_case o False en caso de que algo haya salido mal.
def obtener_dato_formato(dato:str):
    if type(dato) == str:
        dato = dato.lower()
        dato = dato.replace("-"," ")
        dato = dato.replace(" ","_")
        return dato
    else:
        return False

print(f"1.2 = {obtener_dato_formato(lista_personajes[5]['nombre'])}")


#Recibe: un string con el nombre del personaje.
#Hace: valida que sea un diccionario, que tenga la clave ‘nombre’ y junta el formato snake_case con las iniciales.
#Retorna: False si no se cumplen las validaciones o el nombre formateado/True en caso de que las haya pasado.
def stark_imprimir_nombre_con_iniciales(diccionario:dict):
    if type(diccionario) != dict or len(diccionario["nombre"]) < 1 or diccionario["nombre"] == " ":
        return False
    else:
        nombre = diccionario["nombre"]
        iniciales = f" ({extraer_iniciales(nombre)})"
        nombre_snake = f"* {obtener_dato_formato(nombre)}"
        nombre_formateado = nombre_snake + iniciales
        #return True
        return nombre_formateado

print(f"1.3 = {stark_imprimir_nombre_con_iniciales(lista_personajes[0])}")


#Recibe: una lista de heroes.
#Hace: valida que sea una lista y que no este vacia e imprime los nombres formateados de todos los heroes de la lista.
#Retorna: un True si salio bien o False si salio mal.
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    if type(lista_heroes) == list and len(lista_heroes) > 0:
        for personaje in lista_heroes:
            print(stark_imprimir_nombre_con_iniciales(personaje))
        return True
    else:
        return False

print(f"1.4 = {stark_imprimir_nombres_con_iniciales(lista_personajes)}")




#Recibe: un diccionario y un id de tipo int.
#Hace: valida que los datos no esten vacios y esten dentro de lo correcto, pone el guion y el numero segun corresponda y rellena los espacios faltantes con ceros.
#Retorna: un "N\A" en caso de que no cumpla las validaciones o el codigo de un personaje con un formato especifico.
def generar_codigo_heroe(diccionario:dict, id_heroe:int):
    genero = diccionario["genero"]
    id = str(id_heroe)
    if (len(genero) == 2 and len(id) > 6) or (len(genero) == 1 and len(id) > 7) or len(genero) == 0 or (genero != "M" and genero != "F" and genero != "NB"):
        return "N/A"
    else:
        genero_guion = genero + "-"

        if genero == "M":
            genero_codigo = genero_guion + "1"
        elif genero == "F":
            genero_codigo = genero_guion + "2"
        elif genero == "NB":
            genero_codigo = genero_guion + "0"

        if len(genero_codigo) == 4:
            id_ceros = id.zfill(6)

        if len(genero_codigo) == 3:
            id_ceros = id.zfill(7)

        codigo = genero_codigo + id_ceros
        #print(len(codigo))
        return codigo

print(f"2.1 = {generar_codigo_heroe(lista_personajes[1], 332337)}")


#Recibe: una lista de heroes.
#Hace: valida que la lista no este vacia y que sus elementos sean diccionarios, le asigna un id diferente a cada personaje y genera un codigo (reutilizando funciones pasadas) en base a eso.
#Retorna: un mensaje con el nombre, el codigo y el total de codigos o un False en caso de que algo haya salido mal.
def stark_generar_codigos_heroes(lista:list):
    if len(lista) > 0:
        cadena = ""
        id = 1
        for peronaje in lista:
            if type(peronaje) == dict:
                peronaje["id"] = id
                codigo = generar_codigo_heroe(peronaje,id)
                nombre = stark_imprimir_nombre_con_iniciales(peronaje)
                cadena = cadena + f"{nombre} | {codigo}\n"
                id += 1
            else:
                return False

        mensaje = cadena + f"Se asignaron {id - 1} codigos"
        return mensaje
    else:
        return False

print(f"2.2 = {stark_generar_codigos_heroes(lista_personajes)}")




#Recibe: un string que puede ser un número entero.
#Hace: pasa el numero a string, le saca los espacios y depende de que condicion cumpla retorna una cosa u otra.
#Retorna: si el numero es positivo se retorna el string convertido a numero, si no es un numero entero se retorna un -1, si el numero es negativo se retorna un -2 y si ocurren otros errores se retorna un -3.
def sanitizar_entero(numero:str):
    try:
        numero_str = str(numero)
        numero_str = numero_str.strip()
        if (numero_str.isdigit() == True) or (numero_str[0] == "+" and numero_str[1:].isdigit() == True):
            numero_int = int(numero_str)
            return numero_int
        elif numero_str[0] == "-" and numero_str[1:].isdigit() == True:
            return -2
        elif numero_str.isdigit() == False:
            return -1
    except:
        return -3

print(f"3.1 = {sanitizar_entero('-4')}")


#Recibe: un string que pude ser un número decimal.
#Hace: pasa el numero a string, le saca los espacios y depende de que condicion cumpla retorna una cosa u otra.
#Retorna: si el numero es positivo se retorna el string convertido a flotante, si tiene caracteres no numericos retorna un -1, si el numero es negativo se retorna un -2 y si ocurren otros errores se retorna un -3.
def sanitizar_flotante(numero:str):
    try:
        numero_str = str(numero)
        numero_str = numero_str.strip()
        menos = numero_str.count('-')

        mas = numero_str.count('+')

        puntos = numero_str.count('.')
        localizacion = numero_str.find(".")
        after_punto = localizacion + 1
        antes_punto = localizacion - 1


        if puntos != 1 or mas > 1 or menos > 1:
            return -3
        
        elif (numero_str[0] == "+" or numero_str[0].isdigit() == True) and puntos == 1 and numero_str[after_punto].isdigit() == True and numero_str[antes_punto].isdigit() == True:
            numero_flo = float(numero_str)
            return numero_flo
        
        elif numero_str[0] == "-" and numero_str[1].isdigit() == True and puntos == 1 and numero_str[after_punto].isdigit() == True:
            return -2
        
        elif numero_str.isdigit() == False:
            return -1
        
        
    except:
        return -3

print(f"3.2 = {sanitizar_flotante('6.1')}")


#Recibe: un string y un valor opcional que tambien es un string.
#Hace: le saca los espacios de los costados, reemplaza la / con un espacio y segun el string que le hayas pasado te retorna cosas distintas.
#Retorna: N/A en caso de que tenga numeros, el string por defecto en minuscula en caso de que no haya string principal o el string principal en minuscula si no se cumplen las anteriores.
def sanitizar_string(valor_str:str,valor_por_defecto:str="-"):#

    valor_str = valor_str.strip()
    if valor_por_defecto:
        valor_por_defecto = valor_por_defecto.strip()

    if valor_str.__contains__("/"):
        valor_str = valor_str.replace("/"," ")

    lista = re.split("[0-9]+", valor_str)
    if len(lista)>1:
        return "N/A"

    if (len(valor_str) == 0 or valor_str == " "):
        return valor_por_defecto.lower()
    else:
        return valor_str.lower()

print(f"3.3 = {sanitizar_string('f/df e gA8SR SRSR d','sdsdAFSFDF')}")


#Recibe: un diccionario de un heroe, un string que representa el dato a sanitizar y un string que representa el tipo de dato a sanitizar.
#Hace: se fija que la clave sea parte del heroe y en caso de serlo compara el tipo de dato para saber que funcion usar.
#Retorna: False si no se sanitizo ningun dato o True si se sanitizo algun dato.
def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):
    tipo_dato = tipo_dato.upper()

    for dato in heroe:

        if clave == dato:

            if tipo_dato == "STRING":
                #print(sanitizar_string(heroe[clave]))
                return True
            
            elif tipo_dato == "ENTERO":
                #print(sanitizar_entero(heroe[clave]))
                return True
            
            elif tipo_dato == "FLOTANTE":
                #print(sanitizar_flotante(heroe[clave]))
                return True
            
            else:
                #print("Tipo de dato no reconocido")
                return False

    print("La clave especificada no existe en el héroe")
    return False

print(f"3.4 = {sanitizar_dato(lista_personajes[4],'altura','fLoTanTe')}")


#Recibe: una lista de heroes.
#Hace: verifica que la lista no este vacia, ve si el dato cumple las condiciones para ser normalizado y lo normaliza usando la funcion anterior.
#Retorna: si logra normalizar datos retorna True y si no retorna False.
def stark_normalizar_datos(lista:list):
    if len(lista) > 0:
        for personaje in lista:
            for dato in personaje:

                if dato == "altura":
                    tipo = "flotante"
                    sanitizar_dato(personaje,dato,tipo)

                if dato == "peso":
                    tipo = "flotante"
                    sanitizar_dato(personaje,dato,tipo)

                if dato == "color_ojos":
                    if len(personaje[dato])<1 or personaje[dato] == " ":
                        personaje[dato] = "No tiene"
                    tipo = "string"
                    sanitizar_dato(personaje,dato,tipo)

                if dato == "color_pelo":
                    if len(personaje[dato])<1 or personaje[dato] == " ":
                        personaje[dato] = "No tiene"
                    tipo = "string"
                    sanitizar_dato(personaje,dato,tipo)

                if dato == "fuerza":
                    tipo = "entero"
                    sanitizar_dato(personaje,dato,tipo)

                if dato == "inteligencia":
                    if len(personaje[dato])<1 or personaje[dato] == " ":
                        personaje[dato] = "No tiene"
                    tipo = "string"
                    sanitizar_dato(personaje,dato,tipo)

        return True
    else:
        print("Error: Lista de héroes vacía")
        return False

print(f"3.5 = {stark_normalizar_datos(lista_personajes)}")




#Recibe: una lista de personajes.
#Hace: agarra cada nombre de los personajes de la lista (sin el "the") los pasa a minuscula y los une en una sola cadena separada por guiones.
#Retorna: la cadena con los nombres.
def stark_imprimir_indice_nombre(lista:list):
    palabras = ""
    for personaje in lista:
        cadena = []
        nombre = personaje["nombre"]
        nombre_min = nombre.lower()
        nombre_separado = nombre_min.split()
        cadena += nombre_separado
        for palabra in cadena:
            if palabra != "The" and palabra != "the":
                palabras = palabras + palabra + "-"
                
    return palabras

print(f"4.1 = {stark_imprimir_indice_nombre(lista_personajes)}")




#Recibe: un string que se va a usar para el patron, un int que especifica el largo y un parametro opcional booleano.
#Hace: valida que patrón tenga entre un carácter o dos, que el largo sea un entero entre 1 y 235 inclusive y lo junta en una cadena las veces que se indique para retornarlo despues.
#Retorna: si imprimir es True imprime y retorna el separador, si es false solo lo retorna y en caso de que no se valide bien retorna un "N/A".
def generar_separador(patron:str, largo:int,imprimir:bool=True):
    if largo > 0 and largo < 236 and len(patron)<3 and len(patron)>0:
        separador = ""
        for caracter in range(largo):
            separador = separador + patron

        if imprimir == True:
            alert("Separador",f"El separador quedo asi: {separador}")
            print(separador)
            return separador
        else:
            return separador
    else:
        return "N/A"

print(f"5.1 = {generar_separador('*',10,False)}")


#Recibe: un string que representa un título.
#Hace: lo pasa a mayuscula, reusa la funcion anterior y lo junta en el formato pedido.
#Retorna: un string con un formato de titulo.
def generar_encabezado(titulo:str):
    titulo_mayus = titulo.upper()
    separador = generar_separador('*',100,False)
    titulo_separado = f"{separador}\n{titulo_mayus}\n{separador}"
    return titulo_separado

print(f"5.2 =\n{generar_encabezado('Buenas')}")


#Recibe: un diccionario con los datos de un héroe.
#Hace: reutiliza la funcion anterior para crear los encabezados, le da el formato pedido a los datos del heroe y lo imprime.
#Retorna: la ficha del heroe en forma de string.
def imprimir_ficha_heroe(heroe:dict):
    titulo = generar_encabezado('Principal')

    nombre = heroe["nombre"]
    iniciales_nombre = extraer_iniciales(nombre)
    formato_nombre = obtener_dato_formato(nombre)
    nombre_completo = f"NOMBRE DEL HÉROE: {formato_nombre} ({iniciales_nombre})"

    identidad = heroe["identidad"]
    formato_identidad = f"IDENTIDAD SECRETA: {obtener_dato_formato(identidad)}"

    empresa = heroe["empresa"]
    formato_empresa = f"CONSULTORA: {obtener_dato_formato(empresa)}"

    codigo = f"CÓDIGO DE HÉROE: {generar_codigo_heroe(heroe,heroe['id'])}"
#----------------------
    titulo_2 = generar_encabezado('Fisico')

    altura = float(heroe["altura"])
    formato_altura = f"ALTURA: {altura:.0f} cm."

    peso = float(heroe["peso"])
    formato_peso = f"PESO: {peso:.2f} kg."

    fuerza = int(heroe["fuerza"])
    formato_fuerza = f"FUERZA: {fuerza} N."
#----------------------
    titulo_3 = generar_encabezado('Senas Particulares')

    color_ojos = heroe["color_ojos"]
    formato_ojos = f"COLOR DE OJOS: {color_ojos}"
    
    color_pelo = heroe["color_pelo"]
    formato_pelo = f"COLOR DE PELO: {color_pelo}"

    informacion_heroe = f"\n{titulo}\n{nombre_completo}\n{formato_identidad}\n{formato_empresa}\n{codigo}\n{titulo_2}\n{formato_altura}\n{formato_peso}\n{formato_fuerza}\n{titulo_3}\n{formato_ojos}\n{formato_pelo}"
    return informacion_heroe

print(f"5.3 = {imprimir_ficha_heroe(lista_personajes[5])}")


#Recibe: una lista de heroes.
#Hace: imprime la ficha del primer heroe usando la funcion anterion, despues si toca 1 o 2 se muestran las otras fichas que hay en la lista y con el 3 se sale.
#Retorna: imprime la ficha del heroe que selecciones.
def stark_navegar_fichas(lista_heroes:list):
    id = 1
    for personaje in lista_heroes:
        if int(personaje["id"]) == id:
            print(imprimir_ficha_heroe(personaje))

    while True:
        opciones = int(input("\n1.Ir a la izquierda\n2.Ir a la derecha\n3.Salir\nElija una opcion:"))
        if opciones != 1 and opciones != 2 and opciones != 3: 
            print("Elegi uno de los valores disponibles")
            continue
        else:
            match opciones:
                case 1:
                    id -=1
                    if id > 0 and id < 25:
                        for personaje in lista_heroes:
                            if int(personaje["id"]) == id:
                                print(imprimir_ficha_heroe(personaje))
                    elif id < 1:
                        id = 24
                        for personaje in lista_heroes:
                            if int(personaje["id"]) == id:
                                print(imprimir_ficha_heroe(personaje))

                case 2:
                    id +=1
                    if id > 0 and id < 25:
                        for personaje in lista_heroes:
                            if int(personaje["id"]) == id:
                                print(imprimir_ficha_heroe(personaje))
                    elif id > 24:
                        id = 1
                        for personaje in lista_heroes:
                            if int(personaje["id"]) == id:
                                print(imprimir_ficha_heroe(personaje))
                                
                case 3:
                    break

print(f"5.4 = {stark_navegar_fichas(lista_personajes)}")




#Recibe: un dato que nosotros le pasemos.
#Hace: analiza si ese dato es apto para una de las opciones, si lo es, realiza la accion, y, si no lo es, te tira error.
#Retorna: la funcion que vos elijas en las opciones o un mensaje de error.
def menu_principal():
    while True:
        opciones = input(
            "\n1.Imprimir la lista de nombres junto con sus iniciales"
            "\n2.Imprimir la lista de nombres y el código del mismo"
            "\n3.Normalizar datos"
            "\n4.Imprimir índice de nombres"
            "\n5.Navegar fichas"
            "\n6.Salir"
            "\nElija una opcion:")
        if opciones == "1" or opciones == "2" or opciones == "3" or opciones == "4" or opciones == "5" or opciones == "6":
            opciones = int(opciones)
            match opciones:
                case 1:
                    print(stark_imprimir_nombres_con_iniciales(lista_personajes))

                case 2:
                    print(stark_generar_codigos_heroes(lista_personajes))

                case 3:
                    print(stark_normalizar_datos(lista_personajes))

                case 4:
                    print(stark_imprimir_indice_nombre(lista_personajes))

                case 5:
                    print(stark_navegar_fichas(lista_personajes))

                case 6:
                    break
        else:
            print("Ponga un numero de los que este entre las opciones para obtener una respuesta satisfactoria.")
            continue

print(f"6 = {menu_principal()}")












