import random

sopechosos = ['Profesor','Intendente','Estudiante','Ardilla','Fantasma']
armas = ['Graficadora','Regla','Pluma','Pistola','Cautin']
lugares = ['EdificioL','Patio','Biblioteca','Torniquetes','Gimnasio']

def solucion():
    return [sopechosos[random.randint(0,4)], armas[random.randint(0,4)], lugares[random.randint(0,4)]]

# print(solucion())

print("Era un dia cualquiera en CETI en tiempos antes de pandemia cuando de pronto....\n Te tropiezas con un muertito\n"
    "Tendras que adivinar quien fue el asesino. Estas Listo?\n"
    "\nAhora encuentra al Asesino!!!\n")


for preguntas_no in range(0,5):
    print("Elige una opcion?\n")
    pregunta = int(input(
        "\n1 - Interrogar a sopechoso\n"
        "\n2 - Revisar Arma\n"
        "\n3 - Revisar un Lugar\n"))    
    pass
#    print("ya sabes quien es? ahora Dimelo...")

    if pregunta == 1:
        print("\nA quien eliges?\n")
        sopechosos_n = int(input(
            "\n1 - Profesor\n"
            "\n2 - Intendente\n"
            "\n3 - Estudiante\n"
            "\n4 - Ardilla\n"
            "\n5 - Fantasma\n"))
        if sopechosos_n == 1:
            print("\nEl Profesor iba saludando a sus estudiantes e iba pensando en el altercado que tuvo con uno de ellos por la mañana \n"
             "se dirigia al Modulo L para sus clases, al pasar de frente a un Estudiante le vio una Graficadora en la mano, pero jamas vio al muertito\n")
        elif sopechosos_n == 2:
            print("\nEl intendente vio al Profesor por la mañana minutos despues del altercado con el Estudiante, vio la regla, pero no vio al muertito\n")
        elif sopechosos_n == 3:
            print("\nEl Estudiante se dirigia al Patio,iba de prisa por que llegaba tarde a clases"
                ", vio al muertito pero no vio el Arma homicida, se encontro en el camino al Profesor")
        elif sopechosos_n == 4:
            print("\nLa ardilla bajo de un arbol y vio una Regla al pie del arbol que estaba en el Patio.")



    elif pregunta == 2:
        print("Elige un arma:\n")
        armas_n = int(input(
            "\n1 - Graficadora\n"
            "\n2 - Regla\n"
            "\n3 - Pluma\n"
            "\n4 - Pistola\n"
            "\n5 - Cautin\n"))
    elif pregunta == 3:
        lugares_n = int(input())