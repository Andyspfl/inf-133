from flask import Blueprint, request, jsonify
from models.candy_model import Candy
from views.candy_view import render_candy_detail, render_candy_list
from flask_jwt_extended import get_jwt_identity
from utils.decorators import roles_required, jwt_required

# Crear un blueprint para el controlador de dulces
candy_bp = Blueprint("candy", __name__)

# Ruta para obtener la lista de dulces
@candy_bp.route("/candies", methods=["GET"])
@roles_required(roles=["admin", "user"])
def get_candies():
    candies = Candy.get_all()
    return jsonify(render_candy_list(candies))

# Ruta para obtener un dulce específico por su ID
@candy_bp.route("/candies/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_candy(id):
    candy = Candy.get_by_id(id)
    if candy:
        return jsonify(render_candy_detail(candy))
    return jsonify({"error": "Dulce no encontrado"})

# Ruta para crear un nuevo dulce
@candy_bp.route("/candies", methods=["POST"])
@jwt_required
def create_candy():
    data = request.json
    brand = data.get("brand")
    weight = data.get("weight")
    flavor = data.get("flavor")
    origin = data.get("origin")
    
    if not (brand and weight and flavor and origin):
        return jsonify({"error": "Faltan datos requeridos"}), 400
    
    candy = Candy(brand=brand, weight=weight, flavor=flavor, origin=origin)
    candy.save()
    return jsonify(render_candy_detail(candy)), 201
    
# Ruta para actualizar un dulce existente por su ID
@candy_bp.route("/candies/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_candy(id):
    candy = Candy.get_by_id(id)
    if not candy:
        return jsonify({"error": "Dulce no encontrado"}), 404
    
    data = request.json 
    brand = data.get("brand")
    weight = data.get("weight")
    flavor = data.get("flavor")
    origin = data.get("origin")
    
    candy.update(brand=brand, weight=weight, flavor=flavor, origin=origin)
    
    return jsonify(render_candy_detail(candy))

# Ruta para eliminar un dulce existente por su ID
@candy_bp.route("/candies/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_candy(id):
    candy = Candy.get_by_id(id)
    if not candy:
        return jsonify({"error": "Dulce no encontrado"}), 404
    
    candy.delete()
    return "", 204
