# Def
# 21/10/2024

def soma(a, b):
    return a + b

print(soma(1, 34))

# parâmetros são as variáveis definidas dentro da função
# argumentos são os valores atribuídos às variáveis no momento de execução

# argumento posicional
print(soma(1, 1))

# argumento nomeado
print(soma(a=1, b=2))

print(1, 2, 3, sep='-')
print(soma(1, None))