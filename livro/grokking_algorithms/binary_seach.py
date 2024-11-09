# Binary search algorithm

numbers = [i for i in range(1, 101)]

toggle = True
i = 0
while toggle:
    if numbers[i] == 50:
        print('That\'s the number.')
        toggle = False
    i += 1

print(f'The program ran {i} times.')