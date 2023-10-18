"""
/* Reto #3: ¿ES UN NÚMERO PRIMO?
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""


def prime_number(number):
    counter_dividers = 2

    for num in range(2, number):
        if number % num == 0:
            counter_dividers += 1

    if counter_dividers == 2:
        return True


for number in range(1, 101):
    if prime_number(number):
        print(number)
