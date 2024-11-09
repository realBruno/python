# Exercícios
# 03/10/2024

# Exercício 1
numero = input()

try:
    numero.isdigit()
    if int(numero) % 2 == 0:
        print('É par')
    else:
        print('É ímpar')
except:
    print('Por favor, insira um número inteiro')

# Exercício 2

# esse código foi o que ficou mais legal
# ele permite que o usuário insira a hora no formato padrão ab:cd
# mas também é possível inputar somente inteiros: 23 ou 0, por ex.

hora = input()
try:
    hora = hora[0] + hora[1]
except:
    hora = hora[0]

hora = hora.replace(':', "")
hora = int(hora)

if hora >= 0 and hora <= 11:
    print('Bom dia')
elif hora >= 12 and hora <= 17:
    print('Boa tarde')
elif hora >= 18 and hora <= 23:
    print('Boa noite')
else:
    print('Por favor, insira uma hora válida. (formato ab:cd)')

# Exercício 3

nome = input()

if len(nome) <= 3:
    print('Seu nome é muito curto')
elif len(nome) >= 5 and len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')