"""
/* Reto #6: INVIRTIENDO CADENAS
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""


# first way
def reversing_chains(chain: str):
    return chain[::-1]


chain = "Hola mundo"
print(reversing_chains(chain))


# other way
def reversing_chains(chain):
    reversed_chain = ""

    for i in range(len(chain) - 1, -1, -1):
        reversed_chain += chain[i]

    return reversed_chain


chain = "Hola mundo"
print(reversing_chains(chain))
