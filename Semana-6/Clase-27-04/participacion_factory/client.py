import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

print("POST\n")
# POST /chocolates
new_chocolate_data = {
    "product_type": "bonbon",
    "weight": 50,
    "flavor": "hazelnut",
    "filling": "caramel"
}

response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())
# POST /chocolates
new_chocolate_data = {
    "product_type": "truffle",
    "weight": 50,
    "flavor": "hazelnut",
    "filling": "caramel"
}

response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "product_type": "tablet",
    "weight": 30,
    "flavor": "dark chocolate"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

print("GET\n")

# GET /chocolates
response = requests.get(url=url)
print(response.json())

print("PUT\n")

# PUT /chocolates/{chocolate_id}
updated_chocolate_data = {
    "filling": "peanut butter"
}
response = requests.put(f"{url}/1", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

print("GET\n")

# GET /chocolates
response = requests.get(url=url)
print(response.json())

print("DELETE\n")

# DELETE /chocolates/{chocolate_id}
response = requests.delete(f"{url}/3")
print("Chocolate eliminado:", response.json())

# POST /chocolates
new_chocolate_data = {
    "product_type": "truffle",
    "weight": 50,
    "flavor": "hazelnut",
    "filling": "caramel"
}

response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())
print("GET\n")

# GET /chocolates
response = requests.get(url=url)
print(response.json())