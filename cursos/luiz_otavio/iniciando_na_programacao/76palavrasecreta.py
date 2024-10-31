# Exercício - jogo da palavra secreta
# 10/10/2024

palavra_secreta = 'banana'
tentativas = 0
while True:
    tentativas += 1
    entrada = input()
    if entrada.isalpha() == False:
        print('Por favor, insira apenas letras.')
    
    if len(entrada) != 1 and entrada != palavra_secreta:
        print('Digite uma letra.')
    
    if entrada.lower() == palavra_secreta.lower():
        print(f'{palavra_secreta.title()} é a resposta correta. Parabéns.', \
            end='')
        break
    elif entrada.lower() in palavra_secreta.lower():
        print(entrada)
    else:
        print('*')
    
if tentativas == 1:
    print(f' Você tentou {tentativas} vez.')
else:
    print(f' Você tentou {tentativas} vezes.')