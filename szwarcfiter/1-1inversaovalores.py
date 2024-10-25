# Algoritmo 1.1: Inversão de Valores em uma Sequência
# 24/10/2024

import math

numeros = [numero for numero in range(1, 101)]
tamanho = len(numeros)

for i in range(math.ceil(tamanho/2)):
    temp = numeros[i]
    numeros[i] = numeros[tamanho - i - 1]
    numeros[tamanho - i - 1] = temp

print(numeros)
