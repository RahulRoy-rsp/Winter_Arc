"""
    Generate Floyd's Triangle
"""

n = int(input("Enter number of rows: "))

def floydsTriangle(n):
    val = 1
    for i in range(1, n + 1): 
        for j in range(i):
            print(val, end=" ")
            val += 1
        print()


floydsTriangle(n)
