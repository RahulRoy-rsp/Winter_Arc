"""
    Reverse digits of a number
"""

n = int(input("Enter a number: "))

def reverseDigits(n):
    reversed_digits = []

    while n > 0:
        reversed_digits.append(str(n % 10))
        n //= 10
    return int(''.join(reversed_digits))



print(reverseDigits(n))