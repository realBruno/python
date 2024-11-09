# Substituição em vetor I
# 09/11/2024

X = []

for i in range(10):
    number = int(input())
    if number <= 0:
        X.append(1)
    else:    
        X.append(number)
    
for i in range(len(X)):
    print(f'X[{i}] = {X[i]}')
