import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}
print("GET TACOS\n")
# GET /tacos
response = requests.get(url)
print(response.json())

print("POST TACOS\n")

# POST /tacos 
mi_taco = {
    "base": "arroz",
    "guiso": "pollo",
    "toppings": ["Fideo", "Carne"],
    "salsa": "rara"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

print("GET TACOS\n")

# GET /tacos
response = requests.get(url)
print(response.json())
print("PUT TACOS\n")

# PUT /tacos/1
edit_taco = {
    "base": "Grande",
    "guiso": "Delgada",
    "toppings": ["Fideo", "Carne"],
    "salsa": "rarita"
}
response = requests.post(url+"1", json=edit_taco, headers=headers)
print(response.json())
print("GET TACOS\n")

# GET /tacos
response = requests.get(url)
print(response.json())

# DELETE /tacos/1
print("DELETE TACOS\n")

response = requests.delete(url + "/1")
print(response.json())
print("GET TACOS\n")

# GET /tacos
response = requests.get(url)
print(response.json())