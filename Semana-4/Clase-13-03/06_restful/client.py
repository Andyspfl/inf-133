import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
print("GET estudiantes")
print()
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


print("POST estudiantes")
print()
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)


print("GET estudiantes by nombre")
print()
# GET filtrando por nombre con query params
ruta_get = url + "estudiantes?nombre=Pedrito"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# PUT actualiza un estudiante por la ruta /estudiantes
print("actualiza estudiante")
ruta_actualizar = url + "estudiantes/1"
estudiante_actualizado = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Arqutectura",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=estudiante_actualizado
)
print(put_response.text)
print("DELETE elimina estudiantes")
print()
# GET filtrando por nombre con query params
ruta_get = url + "estudiantes"
get_response = requests.request(method="DELETE", url=ruta_get)
print(get_response.text)