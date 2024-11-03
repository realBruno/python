# Pares entre cinco números
# 03/11/2024

numeros = []
for i in range(5):
    numero = int(input())
    numeros.append(numero)

counter = 0
for numero in numeros:
    if numero % 2 != 0:
        continue
    else:
        counter += 1

print(f'{counter} valores pares')