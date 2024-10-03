# Flags, is, is not e None
# 03/10/2024

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Passou no if')
else:
    print('Passou no else')

nome = 'Bruno'

print(passou_no_if, type(nome) is not str)

# is e is not são equivalentes a == e !=, respectivamente