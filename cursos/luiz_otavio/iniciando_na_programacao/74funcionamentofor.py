# Como o for funciona
# 08/10/2024, 10/10/2024

"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

"""

""" 
Iterável é um elemento que tem um método chamado __iter__

"""

texto = 'Bruno'.__iter__()
print(texto)
texto = iter('Bruno') # mesma coisa do método __iter__()
print(texto)

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())

print(next(texto)) # mesma coisa do método __next__()