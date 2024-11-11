# Preenchimento de vetor II
# 09/11/2024

number = int(input())

N = []
counter = 0
for i in range(1000):
    N.append(counter)
    counter += 1
    if counter >= number:
        counter = 0
    
for i in range(len(N)):
    print(f'N[{i}] = {N[i]}')