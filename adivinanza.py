import random

#Funcion que verifica que se ingrese un entero
def get_int(leyenda):
    while True:
        try:
            entero=int(input(leyenda))
            return entero
        except ValueError:
            print("Por favor ingrese un entero")
        else:
            break

#Se inicializan las variables y se asigna un numero aleatorio entre 0 y 100
objetivo=random.randrange(0,101) 
numIntentos=0
intentosMax=5

#Se imprime en pantalla
print("""Juguemos a la adivinanzas
Adivina el numero entero entre 0 y 100, tienes 5 intentos
Inicia el juego!
      """)

#Se consulta al usuario el primer numero, se castea a int y se verifica que sea entero
print("Intento N°: ",(numIntentos+1),":")
numero=get_int("\tQue numero elige\t")

#Se inicia el bucle para las sucesivas consultas
while numero!=objetivo:
    #Se imprime si el numero es mayor o menor que el objetivo
    if objetivo>numero:
        print("Tu numero es menor")
    else:
        print("Tu numero es mayor")

    #Se indica la cantidas de intentos restantes y la finalizacion del juego
    if numIntentos==(intentosMax-1):
        print("Te quedaste sin intentos! El numero era ", objetivo,"! Vuelve a jugar!")
        break
    elif numIntentos==3:
        print("Ultimo intento")
    else:
        print("Te quedan ",intentosMax-numIntentos-1,"intentos")

    numIntentos+=1

    #Se consulta por un nuevo numero
    print("\nIntento N°: ",(numIntentos+1),":")
    numero=get_int("\tQue numero elige\t")

#Se imprime en pantalla si los numero coinciden
if numero==objetivo:
    print("Felicitaciones! Adivinaste el numero, era el numero ",objetivo)  