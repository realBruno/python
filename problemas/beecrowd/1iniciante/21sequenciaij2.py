# Sequência IJ 2
# 08/11/2024

I, J, x = 1, 7, 0
toggle = True

while toggle:
    if I == 9 and J == 5:
        toggle = False

    if x < 3:
        print(f'{I=} {J=}')
        J -= 1
        x += 1
    else:
        I += 2
        J = 7
        x = 0