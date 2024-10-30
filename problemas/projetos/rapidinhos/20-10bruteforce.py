# Programa que quebra senhas
# 20/10/2024, 21/10/2024

import random, string, time, math
start = time.time()

password = 'rigesa12'
wordlist = {'',}
counter, result = 0, ''

while result != password:
    result = ''.join(random.choices(string.ascii_letters + string.digits + \
        string.punctuation, k=len(password)))
    if result in wordlist:
        continue
    else:
        wordlist.add(result)
    counter += 1
    print(result)

end = time.time()
time = end-start

if time < 60:
    time = math.floor(time)
    medida = 'segundos'
elif time >= 60 and time < 3600:
    time = time//60
    medida = 'minutos'
else:
    time = time//3600
    medida = 'horas'

print(f'Sua senha, \'{result}\', foi quebrada. O programa levou {time}' + \
    f' {medida} para executar, rodando um total de {counter} vezes')
print(f'Tamanho da lista: {len(wordlist)}')

# Esse programa, ao lidar com uma senha de 8 dígitos, busca um valor entre
# 4.702.525.276.151.521 de valores.
# Cerca de 1269 anos para processar todos os valores.