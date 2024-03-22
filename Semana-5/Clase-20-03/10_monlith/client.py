import requests
url = "http://localhost:8000"
print("GET\n")
response = requests.get(f"{url}/posts")
print(response.json())

print("POST\n")
new_post = {
    "title": "Título de la nueva publicación",
    "content": "Contenido de la nueva publicación"
}

response = requests.post(f"{url}/posts", data=new_post)
print(response.json())

response = requests.get(f"{url}/posts")
print(response.text)

print("PUT\n")
new_put = {
    "title": "Título de la nueva publicación",
    "content": "Hola mundo como estan espero que esten muy bien :3"
}

response = requests.put(f"{url}/post/1", data=new_put)
print(response.json())

print("GET\n")
response = requests.get(f"{url}/posts")
print(response.json())


print("DELETE\n")
response = requests.delete(f"{url}/post/2")

print("GET\n")
response = requests.get(f"{url}/posts")
print(response.json())