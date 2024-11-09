# Soma de ímpares consecutivos II
# 08/11/2024

for i in range(int(input())):
    n1, n2 = map(int, input().split())
    
    if n2 < n1:
        aux = n1
        n1 = n2
        n2 = aux
        del aux
    
    if n1 % 2 == 0:
        print(sum(range(n1 + 1, n2, 2)))
    else:
        print(sum(range(n1 + 2, n2, 2)))
