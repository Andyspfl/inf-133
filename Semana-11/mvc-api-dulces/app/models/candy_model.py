from database import db

# Define la clase Candy que hereda de db.Model
# "Candy" representa la tabla "candies" en la base de datos
class Candy(db.Model):
    __tablename__ = "candies"
    
    # Define las columnas de la tabla 'candies'
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    flavor = db.Column(db.String, nullable=False)
    origin = db.Column(db.String, nullable=False)
    
    def __init__(self, brand, weight, flavor, origin):
        self.brand = brand
        self.weight = weight
        self.flavor = flavor
        self.origin = origin
    
    # Guarda los datos
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    # Obtiene todos los dulces de la base de datos
    @staticmethod
    def get_all():
        return Candy.query.all()
    
    # Obtiene un dulce por su ID
    @staticmethod
    def get_by_id(id):
        return Candy.query.get(id)
    
    # Actualiza un dulce en la base de datos
    def update(self, brand=None, weight=None, flavor=None, origin=None):
        if brand is not None:
            self.brand = brand
        if weight is not None:
            self.weight = weight
        if flavor is not None:
            self.flavor = flavor
        if origin is not None:
            self.origin = origin
        db.session.commit()
    
    # Elimina un dulce de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
