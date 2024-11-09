# Sequência lógica
# 09/11/2024

a = 1

for i in range(int(input())):
    b, c = a**2, a**3
    print(a, b, c)
    print(a, b + 1, c + 1)
    a += 1