# Pares, ímpares, positivos e negativos
# 03/11/2024

numeros = []
for i in range(5):
    numero = int(input())
    numeros.append(numero)

pares, impares, positivos, negativos = [0 for i in range(4)]

for numero in numeros:
    if numero % 2 != 0:
        impares += 1
    else:
        pares += 1
    
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1


print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')
