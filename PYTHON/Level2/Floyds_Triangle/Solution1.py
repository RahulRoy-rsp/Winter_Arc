"""
    Generate Floyd's Triangle
"""

n = int(input("Enter number of rows: "))

def floydsTriangle(n):
    i, val = 0, 1
    while i < n:
        nums = 0
        while nums <= i:
            print(val, end=" ")
            val += 1
            nums += 1
        print()
        i += 1

floydsTriangle(n)
