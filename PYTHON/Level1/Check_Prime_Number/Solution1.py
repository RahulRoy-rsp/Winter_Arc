"""
    Check if a number is a Prime Number
"""

n = int(input("Enter a number: "))

def checkPrimeNumber(n):
    message = "{n} is {not_param} Prime Number"

    if n <= 1:
        return message.format(n=n, not_param="not a")
    
    for i in range(2, n):
        if n % i == 0:
            return message.format(n=n, not_param="not a")

    return message.format(n=n, not_param="a")


print(checkPrimeNumber(n))