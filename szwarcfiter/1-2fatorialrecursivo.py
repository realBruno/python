# Algoritmo 1.2: Fatorial Recursivo
# 24/10/2024

def fat(i):
    if i <= 1:
        return 1
    else:
        return i*fat(i-1)