# Quadrante
# 09/11/2024

toggle = True
while toggle:
    x, y = map(int, input().split())
    
    if x == 0 or y == 0:
        toggle = False
    else:
        if x > 0 and y > 0:
            print('primeiro')
        elif x > 0  and y < 0:
            print('quarto')
        elif x < 0 and y < 0:
            print('terceiro')
        else:
            print('segundo')