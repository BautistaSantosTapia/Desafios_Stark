from data_stark import lista_personajes
#Bautista Santos Tapia

"""
{
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
  }
"""

while True:
    opciones = int(input("\n1.Mostrar todos los datos\n2.Mostrar la identidad y peso del superheroe de mayor fuerza\n3.Mostrar nombre e identidad del superhéroe más bajo\n4.Determinar el peso promedio de los superhéroes masculinos\n5.mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino\n6.Salir\nElija una opcion:"))
    match opciones:
        case 1:
            for super in lista_personajes:
                nombre = super["nombre"]
                identidad = super["identidad"]
                empresa = super["empresa"]
                altura = super["altura"]
                peso = super["peso"]
                genero = super["genero"]
                color_ojos = super["color_ojos"]
                color_pelo = super["color_pelo"]
                fuerza = super["fuerza"]
                inteligencia = super["inteligencia"]
                #print(f"{nombre} - {identidad} - {empresa} - {altura} - {peso} - {genero} - {color_ojos} - {color_pelo} - {fuerza} - {inteligencia}")
                print(f"{nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia}")

        case 2:
            bandera_fuerza = False
            fuerza_max = 0
            for super in lista_personajes:
                fuerza = int(super["fuerza"])
                if bandera_fuerza == False or fuerza > fuerza_max:
                    fuerza_max = fuerza
                    bandera_fuerza = True
                
            print(f"El maximo de fuerza es: {fuerza_max}")

            for super in lista_personajes:
                identidad = super["identidad"]
                peso = super["peso"]
                fuerza = int(super["fuerza"])
                if fuerza == fuerza_max:
                    print(f"\tIdentidad: {identidad} - Peso: {peso}")

        case 3:
            bandera_altura = False
            altura_min = 0
            for super in lista_personajes:
                altura = float(super["altura"])
                if bandera_altura == False or altura < altura_min:
                    altura_min = altura
                    bandera_altura = True
            
            print(f"El minimo de altura es: {altura_min}")

            for super in lista_personajes:
                altura = float(super["altura"])
                nombre = super["nombre"]
                identidad = super["identidad"]
                if altura == altura_min:
                    print(f"\tNombre: {nombre} - Identidad: {identidad}")            

        case 4:
            acumulador_peso = 0
            #lista_masc = []
            acumulador_masc = 0

            for super in lista_personajes:
                genero = super["genero"]
                peso = float(super["peso"])
                if genero == "M":
                    acumulador_peso += peso
                    #lista_masc.append(peso)
                    acumulador_masc += 1

            #if len(lista_masc) > 0:
            if acumulador_masc > 0:
                promedio_peso = acumulador_peso / acumulador_masc#len(lista_masc)
                print(f"El peso promedio de los masculinos es de: {promedio_peso}")
            else:
                print("La lista esta vacia")

        case 5:
            acumulador_fuerza = 0
            #lista_fem = []
            acumulador_fem = 0
            for super in lista_personajes:
                genero = super["genero"]
                fuerza = int(super["fuerza"])
                if genero == "F":
                    acumulador_fuerza += fuerza
                    #lista_fem.append(fuerza)
                    acumulador_fem += 1

            #if len(lista_fem) > 0:
            if acumulador_fem > 0:
                promedio_fuerza = acumulador_fuerza / acumulador_fem#len(lista_fem)
                print(f"La fuerza promedio de las feminas es de: {promedio_fuerza}")
            else:
                print("La lista esta vacia")

            for super in lista_personajes:
                nombre = super["nombre"]
                peso = float(super["peso"])
                fuerza = int(super["fuerza"])
                if fuerza > promedio_fuerza:
                    print(f"\tNombre: {nombre} - Peso: {peso}")

        case 6:
            break
