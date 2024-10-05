# Encryption
# 02/10/2024 - 03/10/2024

# 1. avançar cada letra três casas
    # a = ord('a') + 3
# 2. cada linha deve ser invertida
    # user_string = user_string[::1]
# 3. pegar o meio da string (truncar) e mover cada caractere uma casa à esquerda
    # (len(user_string))//2

original_str, encrypted_str = ([] for i in range(2))

# parte 1: (concluída)
for i in range(int(input())):
    user_string = input()
    for j in range(len(user_string)):
        original_str.append(chr(ord(user_string[j]) + 3))
    new_string = ''.join(map(str, original_str))
    encrypted_str.append(new_string)
    original_str.clear() # remover da lista os elementos da sessão anterior

# parte 2: (concluída)
encrypted_str_reversed = [i[::-1] for i in encrypted_str]

# parte 3:
string_size = len(encrypted_str_reversed)
print(string_size)