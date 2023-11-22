"""
/* Reto #1: ¿ES UN ANAGRAMA?
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""


def anagram(word1: str, word2: str):
    if word1 == word2:
        return "Both words are the same!"

    sorted1 = sorted(word1.lower())
    sorted2 = sorted(word2.lower())

    if sorted1 == sorted2:
        return "Yes, It is an anagram!"

    return "It is not an anagram!"


word1 = "RAZA"
word2 = "RAZA"
print(anagram(word1, word2))

word1 = "amor"
word2 = "roma"
print(anagram(word1, word2))

word1 = "España"
word2 = "Apañes"
print(anagram(word1, word2))

word1 = "España"
word2 = "Islandia"
print(anagram(word1, word2))
