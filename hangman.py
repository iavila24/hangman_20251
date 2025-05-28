# Ahorcado con categorías de palabras
import random
import time
import datetime

# Mensaje según hora del día
def msj_hr():
    hora = datetime.datetime.now().hour
    if hora < 12:
        return "¡Buenos días! Ya ponte a jugar >:("
    elif hora < 18:
        return "Ya comiste, ya jugaste, ¡ya ponte a trabajar!"
    else:
        return "Ya es tarde, ya apágalo uwu sweatie"

# Diccionario de categorías
WORD_CATEGORIES = {
    "animales": ["leon", "elefante", "tigre", "jirafa", "mono"],
    "colores": ["rojo", "azul", "verde", "amarillo", "naranja"],
    "frutas": ["manzana", "platano", "uva", "fresa", "kiwi"]
}

# Elegir palabra de una categoría
def choose_word(category):
    return random.choice(WORD_CATEGORIES[category]).upper()

# Mostrar el estado actual de la palabra
def display_state(word, guessed_letters):
    display = " ".join(c if c in guessed_letters else "_" for c in word)
    print(f"\nPalabra: {display}")

# Obtener letra del jugador
def get_guess(guessed_letters):
    while True:
        guess = input("Adivina una letra: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("→ Ingresa solo una letra válida.")
        elif guess in guessed_letters:
            print("→ Ya la adivinaste. Intenta con otra.")
        else:
            return guess

# Elegir categoría
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

# Juego principal
def play():
    print("¡Bienvenido al juego del Ahorcado!")
    print(msj_hr())
    category = get_category_choice()
    word = choose_word(category)
    guessed_letters = set()

    start_time = time.time()

    while not all(c in guessed_letters for c in word):
        display_state(word, guessed_letters)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

    display_state(word, guessed_letters)
    print("\n🎉 ¡Felicidades, adivinaste la palabra!")
    
    duration = time.time() - start_time
    print(f"⏱️ Tiempo total: {round(duration, 2)} segundos")

# Ejecutar el juego
if __name__ == "__main__":
    play()
