# Múltiplos de 13
# 09/11/2024

x = int(input())
y = int(input())

if x > y:
    aux = x
    x = y
    y = aux

soma = 0

for i in range(x, y + 1):
    if i % 13 == 0:
        continue
    else:
        soma += i

print(soma)