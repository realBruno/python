# interpolação básica de strings
# 01/10/2024

""" 
d ou i - int
f - float
s - string
x ou X - hexadecimal ou HEXADECIMAL
"""

nome = 'Bruno'
preco = 100.4323423

print('%s, o preço total é de %.2f reais.' % (nome, preco))
print('O hexadecimal do preço é %x' % (int(preco)))

# a interpolação funciona como formatação por f-strings ou format
# cabe ao programador decidir qual prefere usar

bancoDados = {
    'carlos': 19,
    'lucas': 20,
    'luiz': 14,
}

for nome, idade in bancoDados.items():
    print('%s tem %i anos.' % (nome.title(), idade))