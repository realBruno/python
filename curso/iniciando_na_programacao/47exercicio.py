# 01/10/2024

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if ((nome != "") and (idade != "")):
    print('Seu nome é %s' % nome)
    print('Seu nome invertido é %s' % nome[::-1])

    if ' ' in nome:
        print('O nome tem espaços')
    else:
        print('O nome não tem espaços')

    print(f'Seu nome tem {len(nome.replace(" ", ""))} letras')
    print('A primeira letra do seu nome é %s' % nome[0])
    print('A última letra do seu nome é %s' % nome[-1])
else:
    print('Desculpe, você deixou os campos vazios.')
    