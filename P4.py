"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(num):
    return str(num)[::-1] == str(num)


num1 = 999
num2 = 999

ran = 900
# 998001

largest_palindrome = 0
vals = (0, 0)

while num1 >= ran:

    while num2 > ran:
        if is_palindrome(num2 * num1) and (num2 * num1) > largest_palindrome:
            largest_palindrome = num2 * num1
            vals = (num1, num2)
        num2 -= 1

    num2 = 999
    num1 -= 1

print(largest_palindrome)
print(vals)
