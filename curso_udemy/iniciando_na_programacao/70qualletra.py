# while - Qual letra apareceu mais vezes na frase? (iterando strings com while)
# 07/10/2024

frase = 'O python é uma linguagem de programação multiparadigma. ' + \
        'Python foi criado por Guido van Rossum.'
valores = []
ocorrencias = ''
for i in frase.replace(' ', ''):
    ocorrencias = frase.count(i)
    valores.append(ocorrencias)

print(f'{}', max(valores))