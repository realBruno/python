# outra implementação do programa que calcula a quantidade de letras na frase

frase = 'O python é uma linguagem de programação multiparadigma. ' + \
        'Python foi criado por Guido van Rossum.'

frase = frase.replace(' ', '')

a = 0

for i in range(len(frase)):
    if a < frase.count(frase[i]):
        a = frase.count(frase[i])
        letra = frase[i]
print(f'A letra que apareceu mais vezes ({a}x) foi \'{letra}\'.')