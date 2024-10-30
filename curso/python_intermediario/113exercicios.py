# Exercícios com funções
# Exercício 1
# 29/10/2024

def mult(*args):
    global total, parameters
    total, parameters = 1, []

    for number in args:
        total *= number
        parameters.append(number)

    return total, parameters

print(mult(89, 90, 234, 5)[0])
print(f"{'*'.join(map(str, parameters))} is equal to {total}")

# Foi recomendado escrever os códigos em Inglês