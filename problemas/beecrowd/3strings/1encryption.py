# Encryption
# 02/10/2024

# 1. avançar cada letra três casas
    # a = ord('a') + 3
# 2. cada linha deve ser invertida
    # user_string = user_string[::1]
# 3. pegar o meio da string (truncar) e mover cada caractere uma casa à esquerda
    # (len(user_string))//2

for _ in range(int(input())):
    user_string = input()