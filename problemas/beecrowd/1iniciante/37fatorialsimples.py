# Fatorial simples
# 09/11/2024

def fat(n):
    if n == 1:
        return 1
    else:
        return n*fat(n-1)
    
print(fat(int(input())))