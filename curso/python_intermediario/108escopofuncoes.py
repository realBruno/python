# Escopo de funções
# 21/10/2024

# escopo refer-se ao local atingido pelo código

x = 1
 
def escopo():
   global x
   x = 1

print(x)

# global faz a variável do escopo externo ser a mesma no escopo interno