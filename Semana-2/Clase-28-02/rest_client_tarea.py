import requests
url = "http://localhost:8000/"

# GET consulta a la ruta /carreras -- Agrega la ruta para mostrar todas laas carreras
ruta_carreras = url + "carreras"
get_carreras = requests.get(ruta_carreras)
print("GET /carreras")
print(get_carreras.text)

# POST agrega dos estudiantes de la carrera de economia
ruta_economia = url + "economia"
nuevo_estudiante = {
    "nombre": "Marcelo",
    "apellido": "Pelaez",
}
post_response_agrega_estudiante = requests.post(url=ruta_economia, json=nuevo_estudiante)

# Estudiante--2

post_economia = url + "economia"
nuevo_estudiante = {
    "nombre": "Arasaka",
    "apellido": "Zylvetty",
}
post_response_agrega_estudiante = requests.post(url=ruta_economia, json=nuevo_estudiante)


# Lista todos los estudiantes de la carrera de Economia
ruta_economia = url + "economia"
get_economia = requests.get(ruta_economia)
print("GET /economia")
print(get_economia.text)

# GET consulta a la ruta /estudiantes
ruta_estudiantes = url + "estudiantes"
get_estudiantes = requests.get(ruta_estudiantes)
print("GET /estudiantes")
print(get_estudiantes.text)