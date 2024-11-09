# Dividindo x por y
# 09/11/2024

for _ in range(int(input())):
    x, y = map(int, input().split())
    try:
        print(f'{x/y:.1f}')
    except:
        print('divisao impossivel')