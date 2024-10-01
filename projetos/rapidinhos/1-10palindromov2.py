# 01/10/2024
# versão dois do progama anterior

user_string = input()
if (user_string.replace(' ', '')).lower() == (user_string[::-1].replace(' ', '')).lower():
    print('É palíndromo')
else:
    print('Não é palíndromo')