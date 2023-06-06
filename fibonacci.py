'''
Fibonacci - prints series of positive numbers only & series starts from 1.
eg:-    Fibonacci(5) - 1, 1, 2, 3, 5
        Fibonacci(7) - 1, 1, 2, 3, 5, 8, 13

'''

def fibonacci(num):
    assert num >= 0 and num == int(num), "Number must be positive only!"
    if num in [0, 1]:
        return num
    while num > 0:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(7))
print(fibonacci(5))