# Enumerate
# 16/10/2024

numeros = ['*'*i for i in range(1, 10)]

indices, conteudos = zip(*enumerate(numeros))

for indice, conteudo in zip(indices, conteudos):
    print(f'{indice}\t{conteudo}')
