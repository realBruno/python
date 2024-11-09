# Crescente e decrescente
# 08/11/2024

toggle = True

while toggle:
    x, y = map(int, input().split())
    
    if x == y:
        toggle = False
    else:
        if x > y:
            print('Decrescente')
        else:
            print('Crescente')