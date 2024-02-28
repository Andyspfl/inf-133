from zeep import Client
client = Client("http://localhost:8000")
result_saludo = client.service.Saludar(nombre="Andy Pansito")
print(result_saludo)

# Llamar al nuevo servicio NumberToDollars
result_dolares = client.service.NumberToDollars(dNum=6.0)
print(result_dolares)

result_suma = client.service.SumaDosNumeros(num1=12,num2=12)
print(result_suma)

# resultados del servicio para ver si una palabra es palindroma o no
result_pal = client.service.CadenaPalindromo(palabra="ana")
print(result_pal)
result_pal = client.service.CadenaPalindromo(palabra="hola")
print(result_pal)
