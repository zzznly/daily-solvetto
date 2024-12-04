# CodeTree : 트로미노
# https://www.codetree.ai/missions/2/problems/tromino?&utm_source=clipboard&utm_medium=text
import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_sum = -1

for i in range(n):
    for j in range(m):
        if i + 2 < n:
            max_sum = max(max_sum, arr[i][j] + arr[i + 1][j] + arr[i + 2][j])

        if j + 2 < n:
            max_sum = max(max_sum, sum(arr[i][j : j + 3]))

        if i + 2 <= n and j + 2 <= n:
            max_sum = max(max_sum, arr[i][j] + arr[i + 1][j] + arr[i][j + 1])

        if i + 2 <= n and j + 2 <= n:
            max_sum = max(max_sum, arr[i][j] + arr[i + 1][j] + arr[i + 1][j + 1])

        if i + 2 <= n and j + 2 <= n:
            max_sum = max(max_sum, arr[i][j + 1] + arr[i + 1][j] + arr[i + 1][j + 1])

        if i + 2 <= n and j + 2 <= n:
            max_sum = max(max_sum, arr[i][j] + arr[i][j + 1] + arr[i + 1][j + 1])

print(max_sum)
