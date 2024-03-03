import requests
url = "http://localhost:8000/"

# GET consulta a la ruta /lista_estudiantes
ruta_get_lista_estudiantes = url + "estudiantes"
get_estudiantes = requests.get(ruta_get_lista_estudiantes)
print("GET /estudiantes:")
print(get_estudiantes.text)
print()

# DELETE consulta a la ruta /eliminar_estudiantes
ruta_eliminar = url+"estudiantes"
eliminar_response = requests.request(method="DELETE",
                                     url = ruta_eliminar)
print("DELETE /estudiante:")

print(eliminar_response.text)



# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post_agrega_estudiante = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
post_response_agrega_estudiante = requests.post(url=ruta_post_agrega_estudiante, json=nuevo_estudiante)
print("POST /estudiante:")
print(post_response_agrega_estudiante.text)

#PUT actualiza un estudiante 
ruta_actualizar = url + "estudiantes"
estudiante_actualizado ={
    "id": 1,
    "nombre": "Juan",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
put_response = requests.request(
    method="PUT", url = ruta_actualizar,
    json=estudiante_actualizado
)
print("PUT /estudiante:")

print(put_response.text)