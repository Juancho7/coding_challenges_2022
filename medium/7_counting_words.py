"""
/* Reto #7: CONTANDO PALABRAS
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""
import re


# first way
def counting_words(text: str) -> dict:
    if not text:
        return "The text is empty!"

    puntuaction_marks = r"[.,;:()¿?¡!\-_ ]"

    words = re.split(puntuaction_marks, text)

    words = [word.lower() for word in words if word]

    words_amount = {}

    for word in words:
        if word in words_amount.keys():
            words_amount[word] += 1
        else:
            words_amount[word] = 1

    return words_amount


print("Using the first way:")
text = "Hola, ¿cómo estás? Yo estoy bien, gracias... hola mundo, yo estoy feliz de que estás bien."
print(counting_words(text))

text = ""
print(counting_words(text))


# other way
def counting_words(text: str):
    if not text:
        return "The text is empty!"

    pattern = r"\w+"
    words = re.findall(pattern, text)

    words = [word.lower() for word in words]

    words_amount = {}

    for word in words:
        if word in words_amount.keys():
            words_amount[word] += 1
        else:
            words_amount[word] = 1

    return words_amount


print("Using the other way:")
text = "Hola, ¿cómo estás? Yo estoy bien, gracias... hola mundo, yo estoy feliz de que estás bien."
print(counting_words(text))
