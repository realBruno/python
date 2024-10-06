# Exercício guiado - Calculadora
# 06/10/2024

while True:
    num1, operador, num2 = input().split()
    resultado = eval(f'{num1}{operador}{num2}')

    print(f'{num1} {operador} {num2} = {resultado}')

    sair = input('Quer sair? s/n: ').lower().startswith('s')
    if sair:
        break