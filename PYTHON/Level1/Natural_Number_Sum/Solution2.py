"""
    Sum of Sums first n natural numbers
"""

n = int(input("Enter n: "))

def calc_sum1(n):
    result = n * (n + 1) * (n + 2) / 6

    return int(result)
    
print(f"Sum of sums of first {n} natural numbers is", calc_sum1(n))