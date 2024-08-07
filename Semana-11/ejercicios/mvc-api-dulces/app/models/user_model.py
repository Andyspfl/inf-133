from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import json

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    roles=db.Column(db.String(50), nullable=False)

    def __init__(self, username, password, roles=["user"]):
        self.username = username
        self.roles = json.dumps(roles)
        self.password_hash = generate_password_hash(password)

    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Esta funcion encuentra un usuario por su nombre de usuario
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
    
    def update(self, username=None, password_hash=None, roles=None):
        if username is not None:
            self.username = username
        if password_hash is not None:
            self.password_hash = password_hash
        if roles is not None:
            self.roles = json.dumps(roles)  # Convertir lista a cadena
        db.session.commit()
    
    # Elimina un dulce de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
