"""
    Generate Pascals Triangle2
"""

n = int(input("Enter number of rows: "))


def pascalsTriangle_2(n):
    result = [1]

    prev = 1
    for k in range(1, n + 1):
        next_val = prev * (n - k + 1) // k
        result.append(next_val)
        prev = next_val

    return result


print(pascalsTriangle_2(n))