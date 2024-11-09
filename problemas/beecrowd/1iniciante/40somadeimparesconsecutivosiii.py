# Soma de ímpares consecutivos III

lst = []
for i in range(int(input())):
    n1, n2 = map(int, input().split())
    
    n2 = n2*2

    for k in range(n1, n1 + n2):
        if k % 2 != 0:
            lst.append(k)

    print(sum(lst))
    lst.clear()