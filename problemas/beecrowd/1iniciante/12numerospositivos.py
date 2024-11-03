# Números positivos
# 03/11/2024

numeros = []
for i in range(6):
    numero = float(input())
    numeros.append(numero)

counter = 0
for numero in numeros:
    if numero < 0:
        continue
    else:
        counter += 1

print(f'{counter} valores positivos')