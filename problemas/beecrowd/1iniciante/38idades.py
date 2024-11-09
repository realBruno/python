# Idades
# 09/11/2024

toggle = True
ages_total, counter = 0, 0

while toggle:
    age = int(input())
    if age < 0:
        toggle = False
    else:
        ages_total += age
        counter += 1

print(f'{ages_total/counter:.2f}')
