# Versão 2 do jogo da palavra secreta
# 10/10/2024, 14/10/2024

import re
import os
import time

segredo = 'perfume'
formatada = '*'*len(segredo)

print(formatada)

tentativas = 0

while True:
    if formatada == segredo:
        print('Você acertou. Fim de jogo. ' \
            f'{tentativas} tentativas.')
        print('Limpando o terminal em:')
        print('3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1...')
        time.sleep(1)
        os.system('clear')
        break
    
    userInput = input()

    tentativas += 1
    
    if userInput.isalpha() == False or len(userInput) != 1:
        print('Digite uma letra.')
        continue

    posicoes = [m.start() for m in re.finditer(userInput, segredo)]
    
    lista_formatada = list(formatada)

    if userInput in segredo:
        for posicao in posicoes:
            lista_formatada[posicao] = userInput
        formatada = ''.join(map(str, lista_formatada)) 
        print(formatada)
    else:
        print(f'\'{userInput}\' não está na palavra secreta.')
        continue

# o problema que estava enfrentando era ter usado o método replace.
# ele substitui todas as ocorrências de um caracter na string pelo outro
# caracter informado. assim, mesmo que tivesse informado a posição do caracter
# que queria substituir, ele substituía todos os * pelo caracter dado.
