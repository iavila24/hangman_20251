import random
import string
import datetime 
import time
def msj_hr():
    hora = datetime.datetime.now().hour
    if 5 <= hora < 12:
        return "¡Buenos días player! ¡Hora de jugar tu futuro!"
    elif 12 <= hora < 18:
        return "¡Buenas tardes player! ¿ready or no?"
    elif 18 <= hora < 22:
        return "¡Buenas noches player disfrtua tu estancia y recuerda las microtransacciones! "
    else:
        return "Ya es tarde ya apagalo u sweatie"


# Base code hangman.py for project colaboration.
WORD_CATEGORIES = {
    "animales": ["leon", "elefante", "tigre", "jirafa", "mono"],
    "colores": ["rojo", "azul", "verde", "amarillo", "naranja"],
    "frutas": ["manzana", "platano", "uva", "fresa", "kiwi"]
}


def choose_word(category):
    return random.choice(WORD_CATEGORIES[category]).upper()

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

def get_category_choice():
    while True:
        print("\nElige una categoría:")
        for i, category in enumerate(WORD_CATEGORIES.keys()):
            print(f"{i + 1}. {category.capitalize()}")
        choice = input("Ingresa el número de tu elección: ").strip()
        try:
            choice_index = int(choice) - 1
            categories = list(WORD_CATEGORIES.keys())
            if 0 <= choice_index < len(categories):
                return categories[choice_index]
            else:
                print("→ Número inválido. Intenta de nuevo.")
        except ValueError:
            print("→ Entrada inválida. Ingresa un número.")

def play():
    print("¡Bienvenido al juego del Ahorcado!")
    category = get_category_choice()
    word = choose_word(category)
    guessed_letters = set()

    print("¡Bienvenido al juego del Ahorcado!")
    print(msj_hr())
    start_time = time.time(
    # Sigue hasta adivinar todas las letras
    while not all(c in guessed_letters for c in word):
        display_state(word, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        if guess in word:
            print(f"✔ ¡'{guess}' está en la palabra!")
        else:
            print(f"✖ '{guess}' no está en la palabra.")
    end_time = time.time()
    duracion = end_time - start_time
    print(f"\n🎉 ¡Felicidades! Has adivinado la palabra: {word}")
    print(f"Tiempo total de juego:{duracion:.2f}segundos")

if __name__ == "__main__":
    play()
    