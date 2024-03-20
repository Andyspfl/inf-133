# # Leer los números X y Y
# x, y = map(int, input().split())
# # Imprimir los números en forma descendente
# for i in range((max(x, y)),(min(x, y)) - 1, -1):
#     print(i)

# a = b =0
# while a<101 and b <101:
#     a, b = map(int, input().split())
#     if a%b == 0 : 
#         print(f"{a} es divisible por {b}")
#     elif b%a == 0: 
#         print(f"{b} es divisible por {a}")
#     elif a ==0 or b==0:
#         print("-1")
#     else: 
#         print("-1")
def llenarV(v):
    n = int(input("Ingrese la cantidad de elementos del vector: "))
    v = []
    for i in range(n):
        v.append(int(input()))
    return v

def mostrarV(v):
    for i in range(len(v)):
        print(v[i])
        
n = int(input())
for i in range(n):
    v = []
    llenarV(v)  
    mostrarV(v)