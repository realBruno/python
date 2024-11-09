# Ultrapassando Z
# 09/11/2024

x = int(input())
z = int(input())

while x >= z:
    z = int(input())

counter = 1
for i in range(x, z):
    x += i
    counter += 1
    if x > z:
        break #### usei break :(

print(counter)