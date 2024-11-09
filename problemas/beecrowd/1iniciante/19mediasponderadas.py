# Médias ponderadas
# 08/11/2024

for i in range(int(input())):
    n1, n2, n3 = map(float, input().split())
    print(f'{(n1*2+n2*3+n3*5)/10:.1f}')
    