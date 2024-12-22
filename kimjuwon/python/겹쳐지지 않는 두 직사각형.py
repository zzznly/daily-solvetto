# 겹쳐지지 않는 두 직사각형
# 링크 : https://www.codetree.ai/missions/2/problems/non-overlapping-two-rectangles?&utm_source=clipboard&utm_medium=text
import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def in_row_range(x, y, n, m):
    return True if 0 <= x < n and 0 <= y < m else False


def sum_of_rectanlge(i, j, r, l, n, m):
    max_sum = 0
    if in_row_range(i + r, j + l, n, m):
        for x in range(i, i + r + 1):
            for y in range(j, j + l + 1):
                max_sum += arr[x][y]
        return max_sum
    else:
        return False


max_sum = -sys.maxsize

for i in range(n):
    for j in range(m):
        for r in range(n):
            for l in range(m):
                temp1 = sum_of_rectanlge(i, j, r, l, n, m)
                if temp1 is not False:
                    for x in range(n):
                        for y in range(m):
                            for r2 in range(n):
                                for l2 in range(m):
                                    if not (
                                        (x + r2 >= i and x <= i + r)
                                        and (y + l2 >= j and y <= j + l)
                                    ):
                                        temp2 = sum_of_rectanlge(x, y, r2, l2, n, m)
                                        if temp2 is not False:
                                            max_sum = max(max_sum, temp1 + temp2)

print(max_sum)
