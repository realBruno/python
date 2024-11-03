# Intervalo 2
# 03/11/2024

in_intervalo, out = 0, 0

for i in range(int(input())):
    valor = int(input())

    if valor in range(10, 21):
        in_intervalo += 1
    else:
        out += 1

print(f'{in_intervalo} in\n{out} out')