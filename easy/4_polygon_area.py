"""
/* Reto #4: ÁREA DE UN POLÍGONO
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""


def polygon_area(polygon: dict):
    if polygon["name"].lower() == "triangle":
        return (polygon["base"] * polygon["height"]) / 2

    if polygon["name"].lower() == "square":
        return polygon["side"] ** 2

    if polygon["name"].lower() == "rectangle":
        return polygon["length"] * polygon["width"]

    return "Figure not valid!"


triangle = {"name": "Triangle", "base": 2, "height": 3}
print(polygon_area(triangle))


square = {"name": "Square", "side": 3}
print(polygon_area(square))


rectangle = {"name": "Rectangle", "length": 2, "width": 3}
print(polygon_area(rectangle))
