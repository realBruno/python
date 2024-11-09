# Tipo de combustível
# 09/11/2024

alcool, gasolina, diesel, toggle = 0, 0, 0, True

while toggle:
    entrada = int(input())

    if entrada not in range(1, 5):
        continue

    if entrada == 1:
        alcool += 1
    elif entrada == 2:
        gasolina += 1
    elif entrada == 3:
        diesel += 1
    else:
        toggle = False

print(f"""MUITO OBRIGADO
Alcool: {alcool}
Gasolina: {gasolina}
Diesel: {diesel}""")