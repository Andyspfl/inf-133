def render_book_list(books):
    #Representa una lista de libros como una lista de diccionarios
    return [
        {
            "id":book.id,
            "title": book.title,
            "edition": book.edition,
            "disponibility": book.disponibility
        }
        for book in books
    ]

def render_book_detail(book):
    return {
        "id":book.id,
        "title": book.title,
        "edition": book.edition,
        "disponibility": book.disponibility
    }