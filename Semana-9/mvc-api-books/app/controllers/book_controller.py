from flask import Blueprint, request, jsonify
from models.book_model import Book
from views.book_view import render_book_detail, render_book_list

# Crear un blueprint para el controlador de animales
book_bp = Blueprint("book",__name__)

# Ruta para obtener la lista de animales
@book_bp.route("/books", methods=["GET"])
def get_books():
    books=Book.get_all()
    return jsonify(render_book_list(books))

@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.get_by_id(id)
    if book:
        return jsonify(render_book_detail(book))
    return jsonify({"error":"Libro no encontrado"})
        

@book_bp.route("/books", methods=["POST"])
def create_book():
    data=request.json
    title= data.get("title")
    autor= data.get("autor")
    edition= data.get("edition")
    disponibility= data.get("disponibility")
    
    if not(title and autor and edition and disponibility):
        return jsonify({"error":"Faltan datos requeridos"}), 400
    
    book = Book(title=title,autor=autor,edition=edition,disponibility=disponibility)
    book.save()
    return jsonify(render_book_detail(book)), 201
    
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.get_by_id(id)
    if not book:
        return jsonify({"error" : "Libro no encontrado"}), 404
    data = request.json 
    title = data.get("title")
    autor = data.get("autor")
    edition = data.get("edition")
    disponibility = data.get("disponibility")
    
    book.update(title=title,autor=autor, edition=edition, disponibility=disponibility)
    
    return jsonify(render_book_detail(book))

@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.get_by_id(id)
    if not book:
        return jsonify({"error":"Libro no encontrado"}), 404
    book.delete()
    
    return "",204