# Tipo tuplas
# 15/10/2024

nomes = 'Bruno', 'David', 'João', 'Priscila'

nome1, nome2, *outros_nomes = nomes
print(nome1, tuple(outros_nomes))
outros_nomes = tuple(outros_nomes)
print(outros_nomes)
outros_nomes = list(tuple(outros_nomes))
print(outros_nomes)