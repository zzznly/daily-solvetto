# 코드 트리
# 링크 : https://www.codetree.ai/missions/2/problems/The-2D-wind-blows?&utm_source=clipboard&utm_medium=text
import sys

n, m, q = tuple(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
copy = [[arr[i][j] for j in range(m)] for i in range(n)]
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(q)]


def final_mean(arr, i, j, n, m):
    count = 1
    check_sum = arr[i][j]
    if i - 1 >= 0:
        check_sum += arr[i - 1][j]
        count += 1
    if i + 1 < n:
        check_sum += arr[i + 1][j]
        count += 1
    if j - 1 >= 0:
        check_sum += arr[i][j - 1]
        count += 1
    if j + 1 < m:
        check_sum += arr[i][j + 1]
        count += 1
    return check_sum // count


for query in queries:
    r1, c1, r2, c2 = query
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    temp = arr[r1 + 1][c1]
    temp2 = arr[r1][c2 - 1]
    for i in range(c2 - 1, c1, -1):
        arr[r1][i] = arr[r1][i - 1]
    arr[r1][c1] = temp

    temp = temp2
    temp2 = arr[r2 - 1][c2]
    for i in range(r2 - 1, r1, -1):
        arr[i][c2] = arr[i - 1][c2]
    arr[r1][c2] = temp

    temp = temp2
    temp2 = arr[r2][c1 + 1]
    for i in range(c1 + 1, c2):
        arr[r2][i] = arr[r2][i + 1]
    arr[r2][c2] = temp

    temp = temp2
    for i in range(r1 + 1, r2):
        arr[i][c1] = arr[i + 1][c1]
    arr[r2][c1] = temp

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            copy[i][j] = final_mean(arr, i, j, n, m)

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            arr[i][j] = copy[i][j]


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
