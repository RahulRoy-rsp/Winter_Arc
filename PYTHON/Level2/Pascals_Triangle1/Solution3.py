"""
    Generate Pascals Triangle1
"""

n = int(input("Enter number of rows: "))


def pascalsTriangle_1(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle


print(pascalsTriangle_1(n))