# introdução ao try e except para capturar erros
# 02/10/2024

numero = input()

try:
    numero = int(numero)
    print(f'O dobro de {numero} é {numero*2}')
except:
    print('Por favor, insira um número válido.')

# resumidamente, o python tenta executar o código em try,
# mas se encontrar algum erro no processo, ele executa o 
# código em except