
import requests
url = "http://localhost:8000"





print("GET estudiantes")
print()

response = requests.get(f"{url}/posts")
print(response.text)




print("POST ")
print()
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "/posts"
nuevo_post ={
    3:{
        "title": "Mi primera publicación",
        "content": "¡Hola mundo! Esta es mi primera publicación en el blog.",
    }
}
    
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_post)
print(post_response.text)


# print("GET estudiantes by numero")
# print()
# # GET filtrando por nombre con query params
# ruta_get = url + "posts"
# get_response = requests.request(method="PUT", url=ruta_get)
# print(get_response.text)

# PUT actualiza un estudiante por la ruta /estudiantes
print("actualiza ")
ruta_actualizar = url + "/posts/"
nuevo_post ={
    (id=1):{
        "title": "Mi primera publicación",
        "content": "¡Hola mundo! Esta es mi primera publicación en el blo.",
    }
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=nuevo_post
)
print(put_response.text)
# print("DELETE elimina estudiantes")
# print()
# # GET filtrando por nombre con query params
# ruta_get = url + "estudiantes"
# get_response = requests.request(method="DELETE", url=ruta_get)
# print(get_response.text)
