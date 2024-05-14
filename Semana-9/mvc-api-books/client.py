import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Obtener la lista de todos los libros
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print("\nLista de libros:")
print(response.json())

# Crear un nuevo libro
url = f"{BASE_URL}/books/create"
nuevo_libro = {
    "title": "El señor de los anillos",
    "autor": "J.R.R. Tolkien",
    "edition": "Primera",
    "disponibility": True
}
response = requests.post(url, json=nuevo_libro, headers=headers)
print("\nCreando un nuevo libro:")
print(response.json())

# Obtener la lista de todos los libros actualizada
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print("\nLista de libros actualizada:")
print(response.json())

# Obtener un libro específico por su ID (por ejemplo, ID=1)
id_libro = 1
url = f"{BASE_URL}/books/{id_libro}"
response = requests.get(url, headers=headers)
print(f"\nDetalles del libro con ID {id_libro}:")
print(response.json())

# Actualizar un libro existente por su ID (por ejemplo, ID=1)
id_libro = 1
url = f"{BASE_URL}/books/{id_libro}/update"
datos_actualizacion = {"title": "El hobbit", "autor": "J.R.R. Tolkien", "edition": "Segunda", "disponibility": True}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print(f"\nActualizando el libro con ID {id_libro}:")
print(response.json())

# Obtener la lista de todos los libros actualizada después de la actualización
url = f"{BASE_URL}/books"
response = requests.get(url, headers=headers)
print("\nLista de libros actualizada después de la actualización:")
print(response.json())

# Eliminar un libro existente por su ID (por ejemplo, ID=1)
id_libro = 1
url = f"{BASE_URL}/books/{id_libro}/delete"
response = requests.delete(url, headers=headers)
print(f"\nEliminando el libro con ID {id_libro}:")
if response.status_code == 204:
    print(f"Libro con ID {id_libro} eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")
