def render_candy_list(candies):
    # Representa una lista de dulces como una lista de diccionarios
    return [
        {
            "id": candy.id,
            "brand": candy.brand,
            "weight": candy.weight,
            "flavor": candy.flavor,
            "origin": candy.origin
        }
        for candy in candies
    ]

def render_candy_detail(candy):
    # Representa los detalles de un dulce como un diccionario
    return {
        "id": candy.id,
        "brand": candy.brand,
        "weight": candy.weight,
        "flavor": candy.flavor,
        "origin": candy.origin
    }
