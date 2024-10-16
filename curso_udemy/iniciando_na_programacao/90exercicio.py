# Exercício
# 15/10/2024

shopping_list = input().split()

while True:
    userInput = input('I would like to add/remove/list items (\'q\' to quit): ')
    
    if userInput.lower() == 'q':
        break
    
    if userInput.lower() == 'add':
        shopping_list.append(input())
        print('Item added!')
        continue
    elif userInput.lower() == 'remove':
        for index, item in enumerate(shopping_list):
            print(f'Position: {index}, item: {item}')
        remove = input()
        if remove.isdigit:
            del shopping_list[int(remove)]
            print('Item removed!')
        else:
            shopping_list.remove(remove)
            print('Item removed!')
        continue
    elif userInput.lower() == 'list':
        for index, item in enumerate(shopping_list):
            print(f'Position: {index}, item: {item}')
        continue
    else:
        print('Invalid option. Please, try again.')
        continue