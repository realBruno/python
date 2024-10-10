# Short Story Competition
# 06/10/2024, 08/10/2024
import re

def start():
    words, lines_per_page, char_per_page = map(int, input().split())
    
    story = input()
    story = re.split(r'(\s+)', story)

    chars = 0
    it = 0
    while chars < char_per_page:
        if chars + len(story[it]) > char_per_page:
            break

        else:
            chars += len(story[chars])
        it += 1
    print(chars, 'passou do while')
    
    start()
start()

""" 
O que queremos saber é, com base nas entradas, que determinam respectivamente a
a quantidade de palavras na história, a quantidade de linhas por página e a 
quantidade de caracteres por linha, qual a quantidade mínima de páginas que a
história de Machado vai ocupar.

        




"""