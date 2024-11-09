# Divisores I
# 09/11/2024

number = int(input())

for i in range(1, number + 1):
    if number % i == 0:
        print(i)