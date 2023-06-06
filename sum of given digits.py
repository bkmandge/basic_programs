'''
Sum of digits:- calculates sum of given number.

1. get remainder of given number - num % 10
2. sum the remainder of number
3. divide the number by 10 - num // 10

Trick:- num % 10 + sumofDigits(num / 10)

'''


def sumofDigits(num):
    assert int(num) >= 0, int(num) == num
    if num == 0:
        return 0
    else:
        return int(num % 10) + sumofDigits(int(num) / 10)


print(sumofDigits(11111))