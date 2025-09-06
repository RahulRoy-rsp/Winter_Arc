"""
    Generate Pascals Triangle1
"""

n = int(input("Enter number of rows: "))


def pascalsTriangle_1(n):
    result = []

    for i in range(1, n+1):
        if i == 1:
            result.append([1])
        else:
            curr = []
            for x in range(1, i+1):
                if x == 1 or x == i:
                    curr.append(1)
                else:
                    to_add = result[i-2][x-2] + result[i-2][x-1]
                    curr.append(to_add)
            result.append(curr)

    return result


print(pascalsTriangle_1(n))