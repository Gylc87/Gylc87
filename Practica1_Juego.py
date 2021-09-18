import os
import array
import random

arraysopechosos = ['Profesor','Intendente','Estudiante','Ardilla','El Guardia']
arraylugares = ['Edificio L','Patio','Biblioteca','Torniquetes','Gimnasio']
arrayarmas = ['Escoba','Regla','Pluma','Pistola','Aguacate']

sopechosos_des =[]
lugares_des = []
armas_des = []


historias_array = []
sospechoso_final = []
lugar_final = []
arma_final = []
sospecho_elegido = []
lugar_elegido = []
arma_elegido =[]
global oportunidades
mensaje=''

def inicia_des():
    sopechosos_des = arraysopechosos[random.randint(0,4)]
    lugares_des = arraylugares[random.randint(0,4)]
    armas_des = arrayarmas[random.randint(0,4)]
    return  sopechosos_des,lugares_des,armas_des

historias_array = inicia_des()
sospechosos_historia = historias_array[0]
lugares_historia = historias_array[1]
arma_historia = historias_array[2]

print(sospechosos_historia)
print(lugares_historia)
print(arma_historia)
print("Era un dia cualquiera en CETI COLOMOS en tiempos pandemicos cuando de pronto....\nTe tropiezas con un muertito\n"
    "Tendras que adivinar quien fue el asesino. Estas Listo?\n"
    "Existen 5 posibles Sospechosos\n"
    "Existen 5 posibles Lugares\n"
    "Existen 5 posibles Armas\n"
    "Ahora encuentra al Asesino!!!\n")
os.system("pause")

#print(arraysopechosos[0])
oportunidades = 1
while oportunidades < 6:
    print("Elige una opcion?\n Tienes 5 oportunidades llevas:", oportunidades)
    pregunta = int(input(
         "1 - Ver sopechoso\n"
         "2 - Revisar Lugar\n"
         "3 - Revisar un Arma\n"))
    if pregunta == 1:
        print("\nQue Sospechoso eliges?\n")
        print("1 -",arraysopechosos[0])
        print("2 -",arraysopechosos[1])
        print("3 -",arraysopechosos[2])
        print("4 -",arraysopechosos[3])
        print("5 -",arraysopechosos[4])
        pregunta = int(input())
        sospecho_elegido = arraysopechosos[pregunta-1]
        if pregunta == 1: #Profesor
            if sospechosos_historia == sospecho_elegido:
                print(sospecho_elegido.upper()," dice que estuvo en Edificio L dando clases\n")
                print("Al parecer no se encontraron grabaciones de ",sospecho_elegido.upper(),"\n")
            else:
                print("Las camaras y/o personas registraron a ", sospecho_elegido.upper(), " caminando por el Edificio L\n")
        elif pregunta == 2: #Intendente
            if sospechosos_historia == sospecho_elegido:
                print(sospecho_elegido.upper()," vio a ", sospechosos_historia.upper()," caminando por los pasillos en la mañana minutos despues del altercado con el Estudiante, vio la Regla, pero no vio al muertito\n")
            else:
                print("Las camaras y/o personas registraron a ", sospecho_elegido.upper(), " caminando por el Edificio L\n")
        elif pregunta == 3: #Estudiante
            if sospechosos_historia == sospecho_elegido:
                print(sospecho_elegido.upper(),"se dirigia al Gimnasio, iba de prisa lo que levanto sospechas, dice que iba de prisa por que se le hacia tarde,\n"
                "vio al muertito pero no vio el arma homicida\n")
            else:
                print("Las camaras y/o personas registraron a Ardilla caminando por el Patio\n")
        elif pregunta == 4: #Ardilla
            if sospechosos_historia == sospecho_elegido:
                print(sospecho_elegido.upper()," desde un arbol entro a la Biblioteca, pero no vio la Pluma\n")
                print("Al parecer no se encontraron grabaciones de ",sospecho_elegido.upper(),"personas vieron pasar a ",sospechosos_historia.upper(),"\n")
            else:
                print("Las camaras y/o personas registraron a ", sospecho_elegido.upper(), " caminando por el Patio con un AGUACATE\n")
        elif pregunta == 5: #El Guardia
            if sospechosos_historia == sospecho_elegido:
                print(sospecho_elegido.upper()," dice que estuvo en los Torniquetes y vio una Pistola, pero no vio al muertito\n")
            else:
                print(sospechosos_historia.upper(),"vio el arma homicida, pero no vio a ",sospecho_elegido.upper(),"\n")
        
    elif pregunta ==2:
        print("Cual lugar eliges?\n")
        print("1 -",arraylugares[0])#Edificion L
        print("2 -",arraylugares[1])#Patio
        print("3 -",arraylugares[2])#Biblioteca
        print("4 -",arraylugares[3])#Torniquetes
        print("5 -",arraylugares[4])#Gimnasio
        pregunta = int(input())
        lugar_elegido = arraylugares[pregunta-1]
        if pregunta == 1: #Edificion L
            if lugares_historia == lugar_elegido:
                print("Las camaras de ",lugar_elegido.upper()," registraron a ", sospechosos_historia.upper(),"\n")
            else:
                print(sospechosos_historia.upper()," dice que estuvo en ",lugar_elegido.upper(),"\n")
        elif pregunta == 2: #Patio
            if lugares_historia == lugar_elegido:
                print("Las camaras y sensores no estaban activas en ",lugar_elegido.upper(),"\n"
                ,sospechosos_historia.upper()," dice que estuvo en ",lugar_elegido.upper(),"\n")
            else:
                print("En ",lugar_elegido.upper()," se vio el arma ", arma_historia.upper(),"\n")
        elif pregunta == 3: #Biblioteca
            if lugares_historia == lugar_elegido:
                print("Se vio a ",sospechosos_historia.upper()," en ",lugares_historia.upper()," las camaras detectaron el arma Pluma\n")
            else:
                print("Por desgracia, las grabaciones y/o sensores estaban deshabilitadas en ",lugares_historia.upper(),"\n")
        elif pregunta == 4: #Torniquetes
            if lugares_historia == lugar_elegido:
                print("Los sensores y personas detectaron en ",lugar_elegido.upper(),"a El Guardia\n")
            else:
                print("Se dice que en",lugares_historia.upper()," se encontraba el ESTUDIANTE\n"
                "las grabaciones no lo muestran\n")
        elif pregunta == 5: #Gimnasio
            if lugares_historia == lugar_elegido:
                print("El ESTUDIANTE dice estar en el ",lugar_elegido.upper(),"\n"
                "los testigos dicen verlo con un CAUTIN")
            else:
                print("Las personas que hacian deporte en ",lugares_historia.upper()," vieron un CAUTIN en el piso")

    if pregunta == 3:
        print("\Que Arma eliges?\n")
        print("1 -",arrayarmas[0])#Escoba
        print("2 -",arrayarmas[1])#Regla
        print("3 -",arrayarmas[2])#Pluma
        print("4 -",arrayarmas[3])#Pistola
        print("5 -",arrayarmas[4])#Aguacate
        pregunta = int(input())
        arma_elegido = arrayarmas[pregunta-1]
        if pregunta == 1:
            if arma_historia == arma_elegido:
                print("El PROFESOR vio ",arma_elegido.upper()," y dice que estuvo en EDIFICIO L dando clases\n")
                print("Al parecer no se encontraron grabaciones de ",arma_elegido.upper(),"\n")
            else:
                print("Las camaras y/o personas registraron a ", arma_elegido.upper(), " por el PATIO\n")
        elif pregunta == 2:
            if arma_historia == arma_elegido:
                print("El ESTUDIANTE vio a ",arma_elegido.upper()," por los pasillos en la mañana, pero no vio al muertito\n")
            else:
                print("Las camaras y/o personas registraron a ", arma_elegido.upper(), " por el EDIFICIO L\n")
        elif pregunta == 3:
            if arma_historia == arma_elegido:
                print("La ARDILLA vio a ",arma_historia.upper()," en la Biblioteca, los sensores detectaron a",arma_elegido.upper(),"\n")
            else:
                print("Las camaras y/o personas registraron a ", arma_elegido.upper(), " por el TORNIQUETES\n")
        elif pregunta == 4:
            if arma_historia == arma_elegido:
                print("La ARDILLA vio a",arma_elegido.upper()," desde un arbol entro a la Biblioteca\n")
                print("Al parecer no se encontraron grabaciones de ",arma_elegido.upper(),"\n")
            else:
                print("Las grabaciones si estaban operando en TORNIQUETES\n")
        elif pregunta == 5:
            if arma_historia == arma_elegido:
                print("La ARDILLA dice que estuvo en los TORNIQUETES y vio a", arma_elegido.upper()," pero no vio al muertito\n")
            else:
                print("El ",arma_historia.upper(),"se detecto en el PATIO\n")
   
    oportunidades = oportunidades + 1

    os.system("pause")
    if oportunidades == 6:
        print("Ahora que ya tienes tus sospechas te toca elegir:\n")
        print("Elige al sospechoso")
        print("1 -",arraysopechosos[0])
        print("2 -",arraysopechosos[1])
        print("3 -",arraysopechosos[2])
        print("4 -",arraysopechosos[3])
        print("5 -",arraysopechosos[4])
        pregunta = int(input())
        sospechoso_final = arraysopechosos[pregunta-1]

        print("Elige el lugar")
        print("1 -",arraylugares[0])
        print("2 -",arraylugares[1])
        print("3 -",arraylugares[2])
        print("4 -",arraylugares[3])
        print("5 -",arraylugares[4])
        pregunta = int(input())
        lugar_final = arraylugares[pregunta-1]

        print("Elige el arma")
        print("1 -",arrayarmas[0])
        print("2 -",arrayarmas[1])
        print("3 -",arrayarmas[2])
        print("4 -",arrayarmas[3])
        print("5 -",arrayarmas[4])
        pregunta = int(input())
        arma_final = arrayarmas[pregunta-1]
        
        if sospechoso_final == sospechosos_historia and lugar_final == lugares_historia and arma_final == arma_historia:
            print("EXCELENTE HAZ DADO CON LAS PISTAS ASESINAS, FELICIDADES!!!!!\n"
                "EL SOSPECHOSO FUE ",sospechoso_final.upper()," EN EL LUGAR ",lugar_final.upper()," CON EL ARMA ",arma_final.upper(),"\n")
        elif sospechoso_final != sospechosos_historia and lugar_final == lugares_historia and arma_final == arma_historia:
            print("FALLASTE, SOLO ATINASTE EL LUGAR Y EL ARMA!!, EL ARMA FUE: ",arma_final.upper()," EL ASESINO FUE: ",sospechoso_final.upper()," EL LUGAR FUE: ", lugar_final.upper(),"\n")
        elif sospechoso_final != sospechosos_historia and lugar_final != lugares_historia and arma_final == arma_historia:
            print("FALLASTE, SOLO ATINASTE EL ARMA!!,",arma_final.upper())
        elif sospechoso_final != sospechosos_historia and lugar_final != lugares_historia and arma_final != arma_historia:
            print("FALLASTE!! NO LOGRASTE ENCONTRAR LAS PISTAS ASESINAS"
            "LAS PISTAS CORRECTAS ERAN: ",sospechoso_final.upper()," - ",lugar_final.upper()," - ",arma_final.upper())
