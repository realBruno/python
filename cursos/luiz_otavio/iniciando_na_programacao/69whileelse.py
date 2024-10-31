# While / else
# 07/10/2024

# quando o laço do while é executado por completo, o else é executado em seguida
# mas isso só ocorre o laço for executado e finalizado 'naturalmente', ou seja,
# sem que usemos break
x = 0
while x < 10:
    x += 1
    print(x)
else:
    print('Todos os valores de x de 1 a 10')