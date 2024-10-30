# High Order Functions
# 29/10/2024

def my_function(x):
    return x

print(my_function(7))

my_other_function = my_function
print(my_other_function('hello'))


def func(msg):
    return msg

def execute(function, msg):
    return function(msg)

print(execute(func, 'hello'))