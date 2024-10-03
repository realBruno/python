# Exercício 1
numero = input()

try:
    numero.isdigit() == True
    if int(numero) % 2 == 0:
        print('É par')
    else:
        print('É ímpar')
except:
    print('Por favor, insira um número inteiro')