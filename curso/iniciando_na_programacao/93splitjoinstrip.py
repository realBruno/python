# Split, join e strip
# 17/10/2024

#nome = 'Bruno\t\tSantos\t\tFernandes'
#print(nome)

# split divide a string em determinado caractere

#lista = nome.split()
#print(lista)

# strip serve para remover espaços no começo e no fim da string
# rstrip -> remove os da direita
# lstrip -> os da esquerda

#userInput = input()

#print(userInput.strip().lower())

# o join serve para unir uma string

lista = ['Bruno', 'Santos', 'Fernandes', 1, 2, 1.2, True]

nome = ' '.join(map(str, lista))
print(nome)