import pytest

# Tests para el controlador de productos


def test_get_candies(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener la lista de productos
    response = test_client.get("/api/candies", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_candie(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder crear un nuevo producto de confitería
    data = {
        "brand": "ChocoBrand",
        "weight": 50,
        "flavor": "Chocolate",
        "origin": "Choco Factory",
    }
    
    response = test_client.post("/api/candies", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["brand"] == "ChocoBrand"
    assert response.json["weight"] == 50
    assert response.json["flavor"] == "Chocolate"
    assert response.json["origin"] == "Choco Factory"


def test_get_candy(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder obtener un producto específico
    # Este test asume que existe al menos un producto en la base de datos
    response = test_client.get("/api/candies/1", headers=admin_auth_headers)
    assert response.status_code == 200
    assert "brand" in response.json


def test_get_nonexistent_candy(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar obtener un producto inexistente
    response = test_client.get("/api/candies/91", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Dulce no encontrado"


def test_create_candie_invalid_data(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar crear un producto sin datos requeridos
    data = {"brand": "Laptop"}  # Falta description, price y stock
    response = test_client.post("/api/candies", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_candie(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder actualizar un producto existente
    data = {
        "brand": "ChocoBranda",
        "weight": 50,
        "flavor": "Chocolate",
        "origin": "Choco Factory",
    }
    response = test_client.put("/api/candies/1", json=data, headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["brand"] == "ChocoBranda"
    assert response.json["weight"] == 50
    assert response.json["flavor"] == "Chocolate"
    assert response.json["origin"] == "Choco Factory"


def test_update_nonexistent_product(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar actualizar un producto inexistente
    data = {
        "brand": "ChocoBranda",
        "weight": 50,
        "flavor": "Chocolate",
        "origin": "Choco Factory",
    }
    response = test_client.put(
        "/api/candies/999", json=data, headers=admin_auth_headers
    )
    assert response.status_code == 404
    assert response.json["error"] == "Dulce no encontrado"


def test_delete_candy(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería poder eliminar un producto existente
    response = test_client.delete("/api/candies/1", headers=admin_auth_headers)
    assert response.status_code == 204

    # Verifica que el producto ha sido eliminado
    response = test_client.delete("/api/candies/1", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Dulce no encontrado"


def test_delete_nonexistent_candy(test_client, admin_auth_headers):
    # El usuario con el rol de "admin" debería recibir un error al intentar eliminar un producto inexistente
    response = test_client.delete("/api/candies/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Dulce no encontrado"
