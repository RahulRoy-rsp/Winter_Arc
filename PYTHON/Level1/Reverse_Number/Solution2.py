"""
    Reverse digits of a number
"""

n = int(input("Enter a number: "))

def reverseDigits(n):
    reversed_num = 0

    while(n > 0):
        a = n % 10
        reversed_num = reversed_num * 10 + a
        n = n // 10
    
    return reversed_num



print(reverseDigits(n))