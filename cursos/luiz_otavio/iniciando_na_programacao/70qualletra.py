# while - Qual letra apareceu mais vezes na frase? (iterando strings com while)
# 07/10/2024, 08/10/2024

frase = 'O python é uma linguagem de programação multiparadigma. ' + \
        'Python foi criado por Guido van Rossum.'

frase = frase.replace(' ', '')
valores = []
for i in frase:
    valores.append(frase.count(i))

maior_valor_index = valores.index(max(valores))

print(f'A letra mais recorrente é \'{frase[maior_valor_index]}\', que aparece'
    f' um total de {max(valores)} vezes.')