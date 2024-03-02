import requests
url = "http://localhost:8000/"

# GET consulta a la ruta /lista_estudiantes
ruta_get_lista_estudiantes = url + "lista_estudiantes"
get_response_lista_estudiantes = requests.get(ruta_get_lista_estudiantes)
print("GET /lista_estudiantes:")
print(get_response_lista_estudiantes.text)
print()

# GET consulta a la ruta /buscar_nombre
ruta_get_buscar_nombre = url + "buscar_nombre"
get_response_buscar_nombre = requests.get(ruta_get_buscar_nombre)
print("GET /buscar_nombre:")
print(get_response_buscar_nombre.text)
print()

# GET consulta a la ruta /contar_carreras
ruta_get_contar_carreras = url + "contar_carreras"
get_response_contar_carreras = requests.get(ruta_get_contar_carreras)
print("GET /contar_carreras:")
print(get_response_contar_carreras.text)
print()



# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post_agrega_estudiante = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingenieria Agronomica",
}
post_response_agrega_estudiante = requests.post(url=ruta_post_agrega_estudiante, json=nuevo_estudiante)
print("POST /agrega_estudiante:")
print(post_response_agrega_estudiante.text)

# GET consulta a la ruta /total_estudiantes
ruta_get_total_estudiantes = url + "total_estudiantes"
get_response_total_estudiantes = requests.get(ruta_get_total_estudiantes)
print("GET /total_estudiantes:")
print(get_response_total_estudiantes.text)
print()