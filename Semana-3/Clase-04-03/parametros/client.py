import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# GET filtrando por nombre con query params
print("\nBusqueda por nombre\n")

ruta_get = url + "estudiantes?nombre=Pedrito"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


print("\nBusqueda por apellido\n")
ruta_getA = url + "estudiantes?apellido=Garcia"
get_responseA = requests.request(method="GET", url=ruta_getA)
print(get_responseA.text)

print("\nBusqueda por apellido y nombre\n")
ruta_getB = url + "estudiantes?nombre=Juanito&apellido=Perea"
get_responseB = requests.request(method="GET", url=ruta_getB)
print(get_responseB.text)