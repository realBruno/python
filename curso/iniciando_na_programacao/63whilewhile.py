# while + while (laços internos)
# 04/10/2024

linhas = int(input())
colunas = int(input())

linha = 0

while linha < linhas:
    coluna = 0
    while coluna < colunas:
        print(linha)
        print(coluna)
        coluna += 1
    linha += 1