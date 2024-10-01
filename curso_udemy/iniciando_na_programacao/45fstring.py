# formatação de strings com f-strings
# 01/10/2024

""" 
ADICIONANDO PADDING
> - Esquerda
< - Direita
^ - Centro

"""

nome = 'Bruno'
print(f'{nome: >10}.')# à esquerda
print(f'{nome: <10}.') # à direita
print(f'{nome: ^10}.') # ao centro

numero = 19232493849334.223234

numero_formatado = f'{numero:+2f}'

""" numero_formatado = numero_formatado.replace(',', ' ')
numero_formatado = numero_formatado.replace('.', ',')
numero_formatado = numero_formatado.replace(' ', '.') """
print(numero_formatado) 