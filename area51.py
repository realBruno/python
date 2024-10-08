linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1


""" 
    linha = 1
    enquanto linha <= linhas
    a coluna será igual a 1
        enquanto coluna <= colunas
            print(linha, coluna) # 1 1
            coluna += 1 (coluna = 2)

        roda mais uma vez
        enquanto coluna <= colunas:
            print(linha, coluna) 1 2

    ...

    print final = 11
                  12
                  21
                  22

 """