# Lanche
# 03/11/2024

item, valor = map(int, input().split())

if item == 1:
    valor *= 4
elif item == 2:
    valor *= 4.5
elif item == 3:
    valor *= 5
elif item == 4:
    valor *= 2
else:
    valor *= 1.5
print(f'Total: R$ {valor:.2f}')