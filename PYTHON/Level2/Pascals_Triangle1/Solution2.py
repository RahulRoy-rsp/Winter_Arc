"""
    Generate Pascals Triangle1
"""

n = int(input("Enter number of rows: "))


def pascalsTriangle_1(n):
    result = []

    for i in range(0, n):
        if i == 0:
            result.append([1])
        else:
            curr = []
            for x in range(0, i+1):
                if x == 0 or x == i:
                    curr.append(1)
                else:
                    to_add = result[i-1][x-1] + result[i-1][x]
                    curr.append(to_add)
            result.append(curr)

    return result


print(pascalsTriangle_1(n))