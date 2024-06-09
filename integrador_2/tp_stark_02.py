from data_stark_02 import lista_personajes

"""{
    "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
  },"""


"""
Para todas las funciones, documentarlas escribiendo que hacen, que parámetros que reciben (si es una lista,
un string, etc y que contendrá) y que es lo que retorna la función!
"""

#recibe por parametro una lista
#pasa el peso, altura y fuerza a int o float
#retorna false o true dependiendo de si ya estaban casteados o no
def stark_normalizar_datos(lista):#altura, peso, fuerza
    for personaje in lista:
        altura = personaje["altura"]#float()
        peso = personaje["peso"]#float()
        fuerza = personaje["fuerza"]#int()

        if type(altura) != float or type(peso) != float or type(fuerza) != int:
            altura = float(altura)
            peso = float(peso)
            fuerza = int(fuerza)
            
            return True #type(altura), type(peso), type(fuerza) 
        
        elif (type(altura) == float and type(peso) == float and type(fuerza) == int) or len(lista) < 1:
            return False

resultado = stark_normalizar_datos(lista_personajes)
print(f"{resultado}")  
if resultado == True:
    mensaje = "Datos Normalizados"
else:
    mensaje = "Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente"
print(f"{mensaje}") 



#1.1
#recibe por parametro un diccionario y un string
#valida que el diccionario no este vacio y que la key exista
#retorna false o true dependiendo de si se cumplen las condiciones o no
def obtener_dato(diccionario:dict, key:str):
    if len(diccionario) > 0 and diccionario[key] != "":
        return True
    else:
        return False

dsd = obtener_dato(lista_personajes[1], "altura")
print(f"1.1: {dsd}")


#1.2
#recibe por parametro un diccionario
#valida que el diccionario no este vacio y que el nombre exista
#retorna un string con el nombre del heroe o un false en caso de no encontrarlo
def obtener_nombre(diccionario:dict):
    if len(diccionario) > 0 and diccionario["nombre"] != "":
        nombre = diccionario["nombre"]
        formato_nombre = f"Nombre: {nombre}"
        return formato_nombre
    else:
        return False

shsh = obtener_nombre(lista_personajes[0])
print(f"1.2: {shsh}")

#2
#recibe por parametro un diccionario y un string
#valida que el diccionario no este vacio y te devuelve el nombre y, el dato y el valor que le hallas pasado por parametro
#retorna un falso en caso que no exista o un mensaje con el nombre y una clave con su respectivo valor
def obtener_nombre_y_dato(diccionario:dict, key:str):
    if len(diccionario) > 0:
        clave = diccionario[key]
        nombre = diccionario["nombre"]
        formato_mensaje = f"Nombre: {nombre} | {key}: {clave}"

        return formato_mensaje
    else:
        return False

ffff = obtener_nombre_y_dato(lista_personajes[2], "fuerza")
print(f"2: {ffff}")

#3.1
#recibe por parametro una lista y un string
#valida que la lista no este vacia y busca el mayor del dato que le pases
#retorna un false si esta vacio o es un string, o un true y la clave maxima si no esta vacia o es int o float
def obtener_maximo(lista:list, key:str):

    if len(lista) > 0:
        bandera = True
        for personaje in lista:

            if key == "fuerza":
                clave = int(personaje[key])
            elif key == "peso" or key == "altura":
                clave = float(personaje[key])
            else:
                clave = str(personaje[key])
            
            if type(clave) == float or type(clave) == int:

                if bandera == True or clave > clave_maxima:
                    clave_maxima = clave
                    bandera = False

            else:
                return False

        return True , clave_maxima
            
    else:
        return False

eioe = obtener_maximo(lista_personajes, "peso")
print(f"3.1: {eioe}")

#3.2
#recibe por parametro una lista y un string
#valida que la lista no este vacia y busca el menor del dato que le pases
#retorna un false si esta vacio o es un string, o un true y la clave minima si no esta vacia o es int o float
def obtener_minimo(lista:list, key:str):

    if len(lista) > 0:
        bandera = True
        for personaje in lista:

            if key == "fuerza":
                clave = int(personaje[key])
            elif key == "peso" or key == "altura":
                clave = float(personaje[key])
            else:
                clave = str(personaje[key])
            
            if type(clave) == float or type(clave) == int:

                if bandera == True or clave < clave_minima:
                    clave_minima = clave
                    bandera = False

            else:
                return False

        return True , clave_minima
            
    else:
        return False

eioe_2 = obtener_minimo(lista_personajes, "fuerza")
print(f"3.2: {eioe_2}")

#3.3
#recibe por parametro una lista, un numero y un string
#valida si los pesonajes tienen una clave con un valor mayor al pedido 
#retorna una lista con los personajes que cumplan la condicion
def obtener_dato_cantidad(lista:list,numero:int,key:str):
    lista_cumplidores = []
    for personaje in lista:
        clave = int(personaje[key])
        if clave > numero:
            lista_cumplidores.append(personaje)

    return lista_cumplidores
            
ghgh = obtener_dato_cantidad(lista_personajes,70,"fuerza")
print(f"3.3: {ghgh}")


#3.4
#recibe por parametro una lista
#recorre todos los datos de los personajes de la lista
#retorna todos los datos de los personajes de la lista o un false si esta vacia
def stark_imprimir_heroes(lista:list):
    if len(lista) > 0:
        for personaje in lista:
            nombre = personaje["nombre"]
            identidad = personaje["identidad"]
            empresa = personaje["empresa"]
            altura = personaje["altura"]
            peso = personaje["peso"]
            genero = personaje["genero"]
            color_ojos = personaje["color_ojos"]
            color_pelo = personaje["color_pelo"]
            fuerza = personaje["fuerza"]
            inteligencia = personaje["inteligencia"]
            print(f"{nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia}")
    else:
        return False

print(f"3.4: {stark_imprimir_heroes(lista_personajes)}")



#4.1
#recibe por parametro una lista y un string
#valida que cada heroe sea de tipo diccionario y que no este vacio y los va sumando
#retorna la suma de los datos o false en caso de que no se pueda
def sumar_dato_heroe(lista:list,key:str):
    suma_key = 0
    for i in lista:
        #print(len(i))#10
        if type(i) == dict and len(i) > 0 and i[key] != "":
            
            if key == "fuerza":
                clave = int(i[key])
            elif key == "peso" or key == "altura":
                clave = float(i[key])
            else:
                return False

            suma_key += clave

        else:
            return False

    return suma_key

yryry = sumar_dato_heroe(lista_personajes,"fuerza")
print(f"4.1: {yryry}")

#4.2
#recibe por parametro dos numeros
#valida que el divisor no sea 0 y hace la division
#retorna la division de los numeros o false en caso de que no se pueda
def dividir(dividendo, divisor):

    if divisor == 0:
        return False
    else:
        respuesta = dividendo / divisor
        return respuesta
    
sddd = dividir(125,5)
print(f"4.2: {sddd}")

#4.3
#recibe por parametro una lista y un string
#valida que la lista no este vacia y saca el promedio de un valor entre todos los personajes de la lista
#retorna el promedio del dato pasado o false en caso de que la lista este vacia
def calcular_promedio(lista:list,key:str):
    acumulador = 0
    if len(lista) > 0:
        for i in lista:

            if key == "fuerza":
                clave = int(i[key])
            elif key == "peso" or key == "altura":
                clave = float(i[key])
            else:
                return False
            
            acumulador += clave

        promedio = acumulador / len(lista)
        return promedio
    else:
        return False
    
wewe = calcular_promedio(lista_personajes,"fuerza")
print(f"4.3: {wewe}")

#4.4
#recibe por parametro una lista y un string
#valida que la lista no este vacia y saca el promedio de un valor entre todos los personajes de la lista
#retorna el promedio del dato pasado o false en caso de que la lista este vacia
def mostrar_promedio_dato(lista:list,key:str):
    acumulador = 0
    if len(lista) > 0:
        for i in lista:

            if key == "fuerza":
                clave = int(i[key])
            elif key == "peso" or key == "altura":
                clave = float(i[key])
            else:
                return False
            
            acumulador += clave

        promedio = acumulador / len(lista)
        return promedio
    else:
        return False
    
uju = mostrar_promedio_dato(lista_personajes,"altura")
print(f"4.4: {uju}")



#5.1
#no recibe nada por parametro
#crea una variable y le pasa un string
#retorna la variable
def imprimir_menu():
    menu = (
            "elija una opcion:\n"
            "1. Normalizar datos\n"
            "2. Nombre de cada superhéroe de género NB\n"
            "3. Superhéroe más alto de género F\n"
            "4. Superhéroe más alto de género M\n"
            "5. Superhéroe más débil de género M\n"
            "6. Superhéroe más débil de género NB\n"
            "7. Fuerza promedio de los Superhéroes de género NB\n"
            "8. Cuántos Superhéroes tienen cada tipo de color de ojos\n"
            "9. Cuántos Superhéroes tienen cada tipo de color de pelo\n"
            "10. Listar todos los Superhéroes agrupados por color de ojos\n"
            "11. Listar todos los Superhéroes agrupados por tipo de inteligencia\n"
            "12. Salir\n"
            )
    return menu

respuesta = imprimir_menu()
print(f"5.1: {respuesta}")


#5.2
#recibe un string por parametro
#valida que sea un numero
#retorna true o false segun si es un numero o no
def validar_entero(numero:str):
    if numero.isdigit(): 
        return True
    else:
        return False

klkl = validar_entero("22")
print(f"5.2: {klkl}")

#5.3
#no recibe nada por parametro 
#imprime el menu, pregunta por un numero y lo pasa a entero y valida que el numero sea correcto
#retorna el numero o false segun si es valido o no
def stark_menu_principal():
    imprimir_menu()
    respuesta = input("ingrese un numero")
    if validar_entero(respuesta):
        respuesta = int(respuesta)
        if respuesta > 12 or respuesta < 1:
            respuesta = False
    else:
        respuesta = False
    return respuesta

cvcv = stark_menu_principal()
print(f"5.3: {cvcv}")



#6
#recibe por parametro una lista
#se encarga de imprimir el menu, tomar el dato que le pidas, verificar que hayas normalizado y realiza las funciones
#retorna la funcion pedida o nada en caso de que no hayas normalizado antes
def stark_marvel_app(lista:list):
    normalizado = False
    bandera = False
    while True:
        if bandera == False:
            print(imprimir_menu())
            bandera = True
        respuesta = stark_menu_principal()
        #print(respuesta)

        if respuesta == 1:
            numero = stark_normalizar_datos(lista_personajes)
            #print(numero)
            if numero == True:
                mensaje = "Datos Normalizados"
            else:
                mensaje = "Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente"
            print(f"{mensaje}") 
            
            if mensaje == "Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente":
                break

            #print(imprimir_menu())
            print("elegi una opcion: ")
            #print(respuesta)

            normalizado = True
        elif respuesta != 1 and respuesta > 1 and respuesta < 13 and normalizado == True:

            match respuesta:
                case 2:
                    "B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB"

                    def nombre_nb(lista:list):
                        if len(lista) > 0:
                            lista_nb = []
                            for personaje in lista:
                                nombre = personaje["nombre"]
                                genero = personaje["genero"]
                                if genero == "NB":
                                    lista_nb.append(nombre)
                            return lista_nb
                        else:
                            return False

                    print(f"si elige el 2: {nombre_nb(lista_personajes)}")

                case 3:
                    "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F"

                    def max_alt_fem(lista:list):
                        if len(lista) > 0:
                            bandera = True
                            for personaje in lista:
                                altura = float(personaje["altura"])
                                genero = personaje["genero"]
                                if genero == "F":
                                    if bandera == True or altura > altura_max:
                                        altura_max = altura
                                        bandera = False
                            return altura_max

                        else:
                            return False
                    
                    print(f"si elige el 3: {max_alt_fem(lista_personajes)}")

                case 4:
                    "D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M"

                    def max_alt_masc(lista:list):
                        if len(lista) > 0:
                            bandera = True
                            for personaje in lista:
                                altura = float(personaje["altura"])
                                genero = personaje["genero"]
                                if genero == "M":
                                    if bandera == True or altura > altura_max:
                                        altura_max = altura
                                        bandera = False
                            return altura_max

                        else:
                            return False
                    
                    print(f"si elige el 4: {max_alt_masc(lista_personajes)}")

                case 5:
                    "E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M"

                    def min_debil_masc(lista:list):
                        if len(lista) > 0:
                            bandera = True
                            for personaje in lista:
                                fuerza = int(personaje["fuerza"])
                                genero = personaje["genero"]
                                if genero == "M":
                                    if bandera == True or fuerza < fuerza_min:
                                        fuerza_min = fuerza
                                        bandera = False
                            return fuerza_min

                        else:
                            return False
                    
                    print(f"si elige el 5: {min_debil_masc(lista_personajes)}")

                case 6:
                    "F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB"

                    def min_debil_nb(lista:list):
                        if len(lista) > 0:
                            bandera = True
                            for personaje in lista:
                                fuerza = int(personaje["fuerza"])
                                genero = personaje["genero"]
                                if genero == "NB":
                                    if bandera == True or fuerza < fuerza_min:
                                        fuerza_min = fuerza
                                        bandera = False
                            return fuerza_min

                        else:
                            return False

                    print(f"si elige el 6: {min_debil_nb(lista_personajes)}")

                case 7:
                    "G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB"

                    def fuer_prom_nb(lista:list):
                        if len(lista) > 0:
                            suma_prom = 0
                            contador = 0
                            for personaje in lista:
                                fuerza = int(personaje["fuerza"])
                                genero = personaje["genero"]
                                if genero == "NB":
                                    suma_prom += fuerza
                                    contador += 1

                            promedio_fuerza = suma_prom / contador

                            return promedio_fuerza

                        else:
                            return False

                    print(f"si elige el 7: {fuer_prom_nb(lista_personajes)}")

                case 8:
                    "H. Determinar cuántos superhéroes tienen cada tipo de color de ojos."

                    """lista_ojos = []
                    for personaje in lista_personajes:
                        ojos = personaje["color_ojos"]
                        lista_ojos.append(ojos)
                        print(ojos)
                    print(len(lista_ojos))#24
                    ojos_seteados = set(lista_ojos)
                    print(ojos_seteados) #9"""

                    def color_ojos(lista:list):
                        contador_silver = 0
                        contador_blue = 0
                        contador_yellow = 0
                        contador_green = 0
                        contador_hazel = 0
                        contador_brown = 0
                        contador_red = 0

                        if len(lista) > 0:
                            for personaje in lista:
                                ojos = personaje["color_ojos"]
                                ojos = ojos.lower()
                                ojos = ojos.split()
                                ojos = ojos[0]
                                if ojos == "silver":
                                    contador_silver += 1
                                elif ojos == "blue":
                                    contador_blue += 1
                                elif ojos == "yellow":
                                    contador_yellow += 1
                                elif ojos == "green":
                                    contador_green += 1
                                elif ojos == "hazel":
                                    contador_hazel += 1
                                elif ojos == "brown":
                                    contador_brown += 1
                                elif ojos == "red":
                                    contador_red += 1

                            
                            return f"Tienen los ojos:\n Amarillos: {contador_yellow}\n Azules: {contador_blue}\n Plateados: {contador_silver}\n Verdes: {contador_green}\n Avellana: {contador_hazel}\n Marrones: {contador_brown}\n Rojos: {contador_red}"

                        else:
                            return False

                    print(f"si elige el 8: {color_ojos(lista_personajes)}")

                case 9:
                    "I. Determinar cuántos superhéroes tienen cada tipo de color de pelo."

                    """lista_pelos = []
                    for personaje in lista_personajes:
                        pelo = personaje["color_pelo"]
                        lista_pelos.append(pelo)
                        print(pelo)
                    print(len(lista_pelos)) #24
                    pelos_seteados = set(lista_pelos)
                    print(pelos_seteados) """
                    
                    def color_pelo(lista:list):
                        contador_desconocido = 0
                        contador_brown = 0
                        contador_white = 0
                        contador_auburn = 0
                        contador_red = 0
                        contador_yellow = 0
                        contador_black = 0
                        contador_brown_white = 0
                        contador_sin_pelo = 0
                        contador_blond = 0
                        contador_green = 0
                        contador_red_orange = 0

                        if len(lista) > 0:
                            for personaje in lista:
                                pelo = personaje["color_pelo"]
                                pelo = pelo.lower()
                                if pelo == "":
                                    contador_desconocido += 1
                                elif pelo == "brown":
                                    contador_brown += 1
                                elif pelo == "white":
                                    contador_white += 1
                                elif pelo == "auburn":
                                    contador_auburn += 1
                                elif pelo == "red":
                                    contador_red += 1
                                elif pelo == "yellow":
                                    contador_yellow += 1
                                elif pelo == "black":
                                    contador_black += 1
                                elif pelo == "brown / white":
                                    contador_brown_white += 1
                                elif pelo == "no hair":
                                    contador_sin_pelo  += 1
                                elif pelo == "blond":
                                    contador_blond += 1
                                elif pelo == "green":
                                    contador_green += 1
                                elif pelo == "red / orange":
                                    contador_red_orange += 1

                            
                            return f"Tienen el pelo:\n Desconocido: {contador_desconocido}\n Marron: {contador_brown}\n Blanco: {contador_white}\n Auburn: {contador_auburn}\n Rojo: {contador_red}\n Amarillo: {contador_yellow}\n Negro: {contador_black}\n Marron y Blanco: {contador_brown_white}\n Sin Pelo: {contador_sin_pelo}\n Blond: {contador_blond}\n Verdes: {contador_green}\n Rojo y Naranja: {contador_red_orange}"

                        else:
                            return False

                    print(f"si elige el 9: {color_pelo(lista_personajes)}")

                case 10:
                    "J. Listar todos los superhéroes agrupados por color de ojos."

                    def personajes_ojos(lista:list):
                        lista_silver = []
                        lista_blue = []
                        lista_yellow = []
                        lista_green = []
                        lista_hazel = []
                        lista_brown = []
                        lista_red = []

                        if len(lista) > 0:
                            for personaje in lista:
                                ojos = personaje["color_ojos"]
                                ojos = ojos.lower()
                                ojos = ojos.split()
                                ojos = ojos[0]
                                if ojos == "silver":
                                    lista_silver.append(personaje)
                                elif ojos == "blue":
                                    lista_blue.append(personaje)
                                elif ojos == "yellow":
                                    lista_yellow.append(personaje)
                                elif ojos == "green":
                                    lista_green.append(personaje)
                                elif ojos == "hazel":
                                    lista_hazel.append(personaje)
                                elif ojos == "brown":
                                    lista_brown.append(personaje)
                                elif ojos == "red":
                                    lista_red.append(personaje)

                            
                            return f"Estos son todos los personajes con los ojos:\n Amarillos: {lista_yellow}\n Azules: {lista_blue}\n Plateados: {lista_silver}\n Verdes: {lista_green}\n Avellana: {lista_hazel}\n Marrones: {lista_brown}\n Rojos: {lista_red}"

                        else:
                            return False

                    print(f"si elige el 10: {personajes_ojos(lista_personajes)}")

                case 11:
                    "K. Listar todos los superhéroes agrupados por tipo de inteligencia"

                    """lista_inteligencia = []
                    for personaje in lista_personajes:
                        inteligencia = personaje["inteligencia"]
                        lista_inteligencia.append(inteligencia)
                        print(inteligencia)
                    print(len(lista_inteligencia)) #24
                    pelos_seteados = set(lista_inteligencia)
                    print(pelos_seteados)#4"""

                    def personajes_inteligencia(lista:list):
                        lista_desconocido = []
                        lista_average = []
                        lista_high = []
                        lista_good = []

                        if len(lista) > 0:
                            for personaje in lista:
                                inteligencia = personaje["inteligencia"]
                                inteligencia = inteligencia.lower()
                                if inteligencia == "good":
                                    lista_good.append(personaje)
                                elif inteligencia == "high":
                                    lista_high.append(personaje)
                                elif inteligencia == "average":
                                    lista_average.append(personaje)
                                elif inteligencia == "":
                                    lista_desconocido.append(personaje)

                            
                            return f"Los personajes segun su inteligencia son:\n Media: {lista_average}\n Buena: {lista_good}\n Alta: {lista_high}\n Desconocido: {lista_desconocido}"

                        else:
                            return False

                    print(f"si elige el 11: {personajes_inteligencia(lista_personajes)}")

                case 12:
                    break

        else:
            print("Primero normalize los datos para avanzar en las opciones")
            break

beb = stark_marvel_app(lista_personajes)
print(f"6: {beb}")











