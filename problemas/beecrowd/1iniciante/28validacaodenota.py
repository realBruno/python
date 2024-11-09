# Validação de nota
# 09/11/2024

toggle = True
media, x = 0, 0
while toggle:
    
    nota = float(input())

    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        media += nota
        x += 1
        if x == 2:
            toggle = False

print(f'media = {media/2:.2f}')