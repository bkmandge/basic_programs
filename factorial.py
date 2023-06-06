'''
Factorial:- Calculates product of all positive numbers less than or equal to the given number.
          - Denoted by '!' sign
          - eg:- 5! -> 1 * 2 * 3 * 4 * 5

'''

def factorial(num):
    assert int(num) == num & int(num) >= 0, "Enter only positive numbers!"
    if num in [0, 1]:
        return 1
    while num > 0:
        return num * factorial(num - 1)


print(factorial(5))