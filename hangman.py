import random
import string
import datetime
import time

def msj_hr():
    hora = datetime.datetime.now().hour
    if 5 <= hora < 12:
        return "¡Buenos días JUGADOR ESTRELLA! ¡Hora de jugar tu futuro!"
    elif 12 <= hora < 18:
        return "¡Buenas tardes JUGADOR ESTRELLA! ¿ready or no?"
    elif 18 <= hora < 22:
        return "¡Buenas noches JUGADOR ESTRELLA, disfruta tu estancia y recuerda las microtransacciones!"
    else:
        return "Ya es tarde, ya apágalo, u sweatie."

# Lista base de palabras
WORD_LIST = ["leon", "azul", "manzana", "jirafa", "platano", "verde", "tigre", "uva"]

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
    print("¡Bienvenido al juego del Ahorcado!")
    print(msj_hr())

    word = choose_word()
    guessed_letters = set()
    attempts = 0

    start_time = time.time()

    while not all(c in guessed_letters for c in word):
        display_state(word, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        attempts += 1  # Contamos cada intento
        if guess in word:
            print(f"✔ ¡'{guess}' está en la palabra!")
        else:
            print(f"✖ '{guess}' no está en la palabra.")

    end_time = time.time()
    duracion = end_time - start_time

    print(f"\n🎉 ¡Felicidades! Has adivinado la palabra: {word}")
    print(f"⏱ Tiempo total de juego: {duracion:.2f} segundos")
    print(f"🔢 Total de intentos: {attempts}")

if __name__ == "__main__":
    play()
def play_game():
    word = choose_word().upper()
    guessed_letters = set()
    attempts = 6

    print(msj_hr())
    print("¡Bienvenido al juego del Ahorcado!")

    while attempts > 0:
        display_state(word, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Letra incorrecta. Te quedan {attempts} intentos.")
        else:
            print("¡Bien! La letra está en la palabra.")

        if all(c in guessed_letters for c in word):
            print(f"¡Felicidades! Adivinaste la palabra: {word}")
            break
    else:
        print(f"Game Over. La palabra era: {word}")

if __name__ == "__main__":
    play_game()
