# Exercício - gerar o primeiro digito de um CPF
# 19/10/2024

digito_um, decremente = 0, 10

cpf = '746.824.890'; copia_cpf = cpf

# obtém valores dentro do objeto map e coloca-os em uma lista
cpf = [numero for numero in map(int, cpf.replace('.','').replace('-', ''))]

for i in range(len(cpf)):
    digito_um += cpf[i]*decremente
    decremente -= 1

digito_um *= 10; digito_um %= 11
digito_um = digito_um if digito_um <= 9 else 0

copia_cpf += f'-{digito_um}'

# ENCONTRAR SEGUNDO DÍGITO

cpf = copia_cpf; copia_cpf = list(copia_cpf)

for i in copia_cpf:
    if i.isdigit() == False:
        copia_cpf.remove(i) # remove os caracteres '.' e '-'

copia_cpf = [eval(i) for i in copia_cpf] # transforma elementos da lista em int

digito_dois, decremente = 0, 11

for i in range(len(copia_cpf)):
    digito_dois += copia_cpf[i]*decremente
    decremente -= 1

digito_dois *= 10; digito_dois %= 11
digito_dois = digito_dois if digito_dois <= 9 else 0

cpf += f'{digito_dois}'

print(cpf)