# Encryption
# 02/10/2024

# 1. avançar cada letra três casas p/ frente
# 2. cada linha deve ser invertida
# 3. pegar o meio da string (truncar) e mover cada caractere uma casa à esquerda

vezesRodar = int(input())
varCtrl = 0
entradas = []

while varCtrl < vezesRodar:
    user_string = input()
    entradas.append(user_string)
    varCtrl += 1

i = 0
for entrada in entradas:
    entrada[i] = ord(entrada[i]) + 3
    i += 1 
