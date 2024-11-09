# Sequência IJ 3
# 08/11/2024

I, J, x = 1, 7, 0
j = J
toggle = True

while toggle:
    if I == 9 and J == 13:
        toggle = False

    if x < 3:
        print(f'{I=} {J=}')
        J -= 1
        x += 1
    else:
        I += 2
        j += 2
        J = j
        x = 0

    