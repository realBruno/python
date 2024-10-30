# Guess What: Password Generator
# 19/10/2024

import string, random

lenPw = int(input())

password = ''

var = string.ascii_letters + str(string.digits) + string.punctuation

for i in range(lenPw):
    password += random.choice(var)

print(password)