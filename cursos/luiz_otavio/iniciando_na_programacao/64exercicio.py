# Exercício guiado com while
# 06/10/2024

nome = 'Bruno Fernandes'

x = 0

while x < len(nome):
    try:
        new_var += '*'+nome[x]
    except:
        new_var = '*'+nome[x]
    x += 1
print(new_var)

# COM FOR

for i in nome:
    try:
        nova_variavel += '*'+i
    except:
        nova_variavel = '*'+i

print(nova_variavel)