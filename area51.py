# Lê o valor de T
T = int(input())

# Inicializa o vetor N de tamanho 1000
N = [0] * 1000

# Preenche o vetor com a sequência de 0 até T-1 repetidas vezes
for i in range(1000):
    N[i] = i % T

# Imprime o vetor conforme o formato solicitado
for i in range(1000):
    print(f'N[{i}] = {N[i]}')
