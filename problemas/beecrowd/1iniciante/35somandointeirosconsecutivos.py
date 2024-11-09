# Somando Inteiros Consecutivos
# 09/11/2024

A, *N = map(int, input().split())
b = A
toggle = True
i = 0

while toggle:
    if N[i] > 0:
        number = N[i]
        toggle = False
    else:
        i += 1
A = 0
for i in range(number):
    A += b + i

print(A)