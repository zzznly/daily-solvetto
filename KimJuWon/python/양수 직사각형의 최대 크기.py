# 양수 직사각형의 최대 크기
# https://www.codetree.ai/missions/2/problems/max-area-of-positive-rectangle?&utm_source=clipboard&utm_medium=text

import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def check_max_rectangle(arr, i, j, i2, j2):
    size = 0
    for x in range(i, i2 + 1):
        for y in range(j, j2 + 1):
            if arr[x][y] <= 0:
                return -1
            size += 1
    return size


max_size = -1
for i in range(n):
    for j in range(m):
        for i2 in range(i, n):
            for j2 in range(j, m):
                max_size = max(max_size, check_max_rectangle(arr, i, j, i2, j2))

print(max_size)
