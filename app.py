
import random

elementos = ["piedra", "papel", "tijeras"]
puntuacion = 0
rondas = 0

def elegir_oponente():
    return random.choice(elementos)

def elegir_jugador():
    while True:
        jugador = input("Elige piedra, papel o tijeras: ").lower()
        if jugador in elementos:
            return jugador
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def comparar(jugador, oponente):
    if jugador == oponente:
        return "Empate"
    elif (jugador == "piedra" and oponente == "tijeras") or (jugador == "tijeras" and oponente == "papel") or (jugador == "papel" and oponente == "piedra"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    global puntuacion
    oponente = elegir_oponente()
    jugador = elegir_jugador()
    resultado = comparar(jugador, oponente)
    print(f"El oponente eligió {oponente}. {resultado}!")
    if resultado == "Ganaste":
        puntuacion += 1
        rondas += 1

while True:
    jugar()
    print(f"Rondas jugadas: {rondas}. Tu puntuación es {puntuacion}.")
    respuesta = input("¿Quieres jugar de nuevo? (s/n): ").lower()
    if respuesta != "s":
        break
