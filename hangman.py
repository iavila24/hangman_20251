
# commit de mensajitos odiosos del dia 

import random
import string
import datetime 

def msj_hr():
    hora = datetime.datetime.now().hour
    if 5 <= hora < 12:
        return "¡Buenos dias player! ¡Hora de jugar tu futuro!"
    elif 12 <= hora < 18:
        return "¡Buenas tardes player! ¿ready or no?"
    elif 18 <= hora < 22:
        return "¡Buenas noches player disfruta tu estancia y recuerda las microtransacciones!"
    else:
        return "Ya es tarde ya apagalo u sweatie"

# Base code hangman.py for project colaboration.
WORD_LIST = [
    "python", "desarrollo", "colaboracion", "github", "ahorcado",
    "programacion", "funcion", "variable", "algoritmo", "repositorio"
]

def choose_word():
    return random.choice(WORD_LIST).upper()

def display_state(word, guessed_letters):
    display = " ".join(c if c in guessed_letters else "_" for c in word)
    print(f"\nPalabra: {display}")
    print(f"Letras adivinadas: {', '.join(sorted(guessed_letters))}")

def get_guess(guessed_letters):
    while True:
        guess = input("Adivina una letra: ").strip().upper()
        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("→ Ingresa UNA sola letra A–Z.")
        elif guess in guessed_letters:
            print("→ Ya probaste esa letra.")
        else:
            return guess

def play():
    word = choose_word()
    guessed_letters = set()
    lives = 6

    print("Bienvenido al juego del Ahorcado")
    print(msj_hr())

    while lives > 0 and not all(c in guessed_letters for c in word):
        display_state(word, guessed_letters)
        print(f"Vidas restantes: {lives}")
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        if guess in word:
            print(f"'{guess}' esta en la palabra")
        else:
            lives -= 1
            print(f"'{guess}' no esta en la palabra. Pierdes una vida")

    if all(c in guessed_letters for c in word):
        print(f"\nFelicidades. Has adivinado la palabra: {word}")
    else:
        print(f"\nHas perdido. La palabra era: {word}")

if __name__ == "__main__":
    play()
