# Preenchimento de vetor I
# 09/11/2024

N = []
number = int(input())
N.append(number)
for i in range(9):
    N.append(N[i]*2)

for i in range(len(N)):
    print(f'N[{i}] = {N[i]}')