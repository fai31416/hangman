from random import shuffle

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ganados = 0
        self.numero = 0
        
    def gana (self):
        self.ganados+=1

def jugar():
    numeros=["1","2", "3", "4","5","6","7","8","9","10"]
    jugador1=Jugador(input("¿Nombre del jugador 1?: "))
    jugador2=Jugador(input("¿Nombre del jugador 2?: "))
    print("Jugar = s, Salir = q\n")
    shuffle(numeros)
    
    while len(numeros) > 1:
        jugador1.numero = numeros.pop()
        jugador2.numero = numeros.pop()
        if jugador1.numero > jugador2.numero:
            jugador1.gana()
            print("{} gana {} a {}".format(jugador1.nombre, jugador1.numero, jugador2.numero))
        else:
            jugador2.gana()
            print("{} gana {} a {}".format(jugador2.nombre, jugador2.numero, jugador1.numero))
        if input("¿Juego?\n")=="q":
            print ("¡Adiós!\n")
            return
        else:
            pass
    if jugador1.ganados > jugador2.ganados:
        print("Ha ganado {} {} a {}\n".format(jugador1.nombre,jugador1.ganados,jugador2.ganados))
    else:
        print("Ha ganado {} {} a {}\n".format(jugador2.nombre,jugador2.ganados,jugador1.ganados))
    

jugar()
