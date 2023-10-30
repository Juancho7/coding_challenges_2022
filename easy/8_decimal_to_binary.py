"""
/* Reto #8: DECIMAL A BINARIO
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""


def decimal_to_binary(number):
    binary = ""

    quotient = number
    while quotient > 0:
        remainder = quotient % 2
        binary = str(remainder) + binary
        quotient = quotient // 2

    return f"{number} is {binary} when converted into a binary."


print(decimal_to_binary(28))
print(decimal_to_binary(10))
print(decimal_to_binary(72))
print(decimal_to_binary(11))
print(decimal_to_binary(21))
