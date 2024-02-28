from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def Palindrome(palabra):
    if(palabra == palabra[::-1]):
        return "La palabra {} si es palindroma".format(palabra)
    else:
        return "La palabra {} NO es palindroma".format(palabra)

def saludar(nombre):
    return "Hola, {}!".format(nombre)


def number_to_dollars(dNum):
    return "$" + str(dNum)

def sumar_numeros(num1, num2):
    return "La suma es: {}".format(num1+num2)

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre":str},
)
dispatcher.register_function(
    "NumberToDollars",
    number_to_dollars,
    returns={"dolares": str},
    args={"dNum": float},
)

dispatcher.register_function(
    "SumaDosNumeros",
    sumar_numeros,
    returns={"suma": str},
    args={"num1": int, "num2": int},
)
dispatcher.register_function(
    "CadenaPalindromo",
    Palindrome,
    returns={"respuesta": str},
    args={"palabra":str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()

