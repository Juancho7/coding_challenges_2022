"""
/* Reto #9: CÓDIGO MORSE
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "-", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""


def morse_code(text: str):
    morse_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "CH": "----",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "Ñ": "--.---",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".---",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "---.-",
        ".": ".-.-.-",
        ",": "--.---",
        "?": "..-....",
        '"': ".-..-.",
        "/": "-..-.",
    }

    characters_morse = ".-"

    characters = text.replace(" ", "")

    translated_text = ""

    if all(character in characters_morse for character in characters):
        morse_codes = text.split("  ")

        for morse_code in morse_codes:
            letter_codes = morse_code.split()

            for letter_code in letter_codes:
                for character, morse_code in morse_dict.items():
                    if letter_code == morse_code:
                        translated_text += character
            translated_text += " "

        return translated_text.strip()
    else:
        words = text.upper().split()

        for word in words:
            for character in word:
                for natural_character, morse_code in morse_dict.items():
                    if character == natural_character:
                        translated_text += morse_code + " "
            translated_text += " "

        return translated_text.strip()


print(morse_code(".... --- .-.. .-  -- ..- -. -.. ---"))
print(morse_code("hola mundo"))
