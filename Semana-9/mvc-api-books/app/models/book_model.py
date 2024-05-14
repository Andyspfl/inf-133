from database import db

# Define la clase libro que hereda de db.Model
# "Book" representa la tabla "books" en la base de datos

class Book(db.Model):
    __tablename__ = "books"
    
    # Define las columnas de la tabla 'books'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    autor = db.Column(db.String, nullable=False)
    edition = db.Column(db.String, nullable=False)
    disponibility = db.Column(db.Boolean, nullable=False)
    
    
    def __init__(self, title, autor, edition, disponibility):
        self.title = title
        self.autor = autor
        self.edition = edition
        self.disponibility = disponibility
        
        
    # Guarda los datos
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    # Obtiene todos los libros de la base de datos
    @staticmethod
    def get_all():
        return Book.query.all()

    # Obtiene un libro por su ID
    @staticmethod
    def get_by_id(id):
        return Book.query.get(id)

    # Actualiza un libro en la base de datos
    def update(self, title=None, autor=None, edition=None, disponibility=None):
        if title is not None:
            self.title = title
        if autor is not None:
            self.autor = autor
        if edition is not None:
            self.edition = edition
        if disponibility is not None:
            self.disponibility = disponibility
        db.session.commit()
        
    # Elimina un libro de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()