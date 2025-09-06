"""
    Sum of Sums first n natural numbers
"""

n = int(input("Enter n: "))

def calc_sum1(n):
    result = 0
    
    for i in range(1, n+1):
        result += i*((i + 1)/2)

    return int(result)
    
print(f"Sum of sums of first {n} natural numbers is", calc_sum1(n))