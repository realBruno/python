# Encryption
# 02/10/2024, 03/10/2024, 05/10/2024
# CONSEGUI FAZERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR!!!!!!!!!!!!!!!!

orig_str_lst, str_mid_lst, encrypted_str = ([] for i in range(3))

for i in range(int(input())):
    string = input()
    
    for j in range(len(string)):
        if ord(string[j]) in range (65, 91) or \
            ord(string[j]) in range (97, 123):
            orig_str_lst.append(chr(ord(string[j]) + 3))
        else:
            orig_str_lst.append(string[j])

    orig_str_lst = orig_str_lst[::-1]

    str_mid = len(orig_str_lst)//2

    for k in orig_str_lst[str_mid:]:
        str_mid_lst.append(chr(ord(k) - 1))

    new_string = ''.join(map(str, orig_str_lst[:str_mid] + str_mid_lst))
    encrypted_str.append(new_string)
    
    orig_str_lst.clear()
    str_mid_lst.clear()

for item in encrypted_str:
    print(item)