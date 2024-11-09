# Exercício guiado - Calculadora
# 06/10/2024, 07/10/2024

while True:
    num1, operador, num2 = input().split()
    operadores_permitidos = '+/-*'
    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print('Um ou ambos os valores inputados são inválidos.')
        continue
    
    if len(operador) == 1 and operador in operadores_permitidos:
        resultado = eval(f'{num1}{operador}{num2}')
        print(f'{num1} {operador} {num2} = {resultado}')
    else:
        print('Você inseriu mais de um operador ou um operador inválido. \n'\
            'Operadores válidos: + - / *')
        continue

    sair = input('Quer sair? s/n: ').lower().startswith('s')
    if sair:
        break