"""
    Generate Pascals Triangle1
"""

n = int(input("Enter number of rows: "))


def pascalsTriangle_1(n):
    if n == 0:
        return []

    ans = [[1]]

    for i in range(1, n):
        prev = ans[-1]
        new = [1]

        for j in range(1, len(prev)):
            new.append(prev[j-1] + prev[j])

        new.append(1)
        ans.append(new)
    
    return ans


print(pascalsTriangle_1(n))