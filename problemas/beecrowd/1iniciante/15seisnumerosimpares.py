# Seis números ímpares
# 03/11/2024

numero = int(input())

if numero % 2 == 0:
    numero += 1
    print(numero)
    for i in range(5):
        numero += 2
        print(numero)
else:
    print(numero)
    for i in range(5):
        numero += 2
        print(numero)