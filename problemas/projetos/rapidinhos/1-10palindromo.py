# 01/10/2024
# checar se uma determinada palavra é um palíndromo

user_string = input()
x = -1

chars_user_string = []
for i in range(0, len(user_string)):
    chars_user_string.append(user_string[x])
    x -= 1

user_string_reverse = ''.join(map(str, chars_user_string))

if(user_string.replace(' ', '')).lower() == (user_string_reverse.replace(' ', '')).lower():
    print('É palíndromo')
else:
    print('Não é palíndromo')