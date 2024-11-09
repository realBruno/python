# check if a number is prime

number = int(input())

x = 2
prime = True
while x < number: 
    
    if number % x == 0:
        x = number
        prime = False
    x += 1
    
print('Number is prime:', prime)