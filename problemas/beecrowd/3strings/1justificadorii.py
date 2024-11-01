# Justificador II
# 01/11/2024

n = 0
linhas = []
nova_lista = []
while n < 1:

    qtd_linhas = int(input())

    if qtd_linhas == 0:
        n += 1
        
    else:
        for i in range(qtd_linhas):
            entrada = input()
            linhas.append(entrada)

        for i in range(len(linhas)):
            linhas[i] = ' '.join(map(str, linhas[i].split()))
            
        margem = len(max(linhas, key=len))

        for i in range(len(linhas)):
            linhas[i] = linhas[i].rjust(margem, ' ')
        linhas.append('')
        nova_lista += linhas.copy()
        linhas.clear()

nova_lista.pop()
for linha in nova_lista:
    print(linha)