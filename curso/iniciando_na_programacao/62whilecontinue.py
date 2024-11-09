# while + continue - pulando alguma repetição

contador = 0
primos = []
while contador < 100:
    contador += 1

    if contador%2 == 0:
        pass
    else:
        primos.append(contador)

for k in primos:
    print(k)

# o continue serve para fazer a estrutura de repetição ser executada do início,
# ignorando quaisquer linhas de código após e que se encontram dentro de tal
# estrutura.