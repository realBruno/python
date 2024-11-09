# fatiamento de strings e função len
# 01/10/2024

minha_string = 'Meu nome completo é...' # string original

x = -1
nova_string = []
for i in range(0, len(minha_string)):
    nova_string.append(minha_string[x])
    # itera todos os índices da string iniciando a partir do último e os guarda
    # na lista nova_string
    x -= 1
string = ''.join(map(str, nova_string)) # convertendo nova_string para string
print(string)

##### parte dois do programa: string inputada pelo usuário

""" user_string = input()

y = - 1
nova_user_string = []
for i in range(0, len(user_string)):
    nova_user_string.append(user_string[y])
    y -= 1

user_gnirts = ''.join(map(str, nova_user_string))
print(user_gnirts) """

### parte tres

meu_nome = 'Bruno Santos Fernandes'
print(meu_nome[::-1])