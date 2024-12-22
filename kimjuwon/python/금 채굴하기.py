# 코드트리 : 금채굴하기
# https://www.codetree.ai/missions/2/problems/gold-mining?&utm_source=clipboard&utm_medium=text
import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

possible_k = n if sum([row.count(1) for row in arr]) > 0 else 0
ans = 1 if possible_k > 0 else 0

for i in range(n):
    for j in range(n):
        count = arr[i][j]
        for k in range(1, possible_k + 1):
            for x in range(k):
                y = k - x
                if x == 0 or y == 0:
                    t = max(x, y)
                    if i + t < n:
                        if arr[i + t][j] == 1:
                            count += 1
                    if i - t >= 0:
                        if arr[i - t][j] == 1:
                            count += 1
                    if j - t >= 0:
                        if arr[i][j - t] == 1:
                            count += 1
                    if j + t < n:
                        if arr[i][j + t] == 1:
                            count += 1

                else:
                    if i + x < n and j + y < n:
                        if arr[i + x][j + y] == 1:
                            count += 1

                    if i + x < n and j - y >= 0:
                        if arr[i + x][j - y] == 1:
                            count += 1
                    if i - x >= 0 and j + y < n:
                        if arr[i - x][j + y] == 1:
                            count += 1

                    if i - x >= 0 and j - y >= 0:
                        if arr[i - x][j - y] == 1:
                            count += 1

            if m * count - (k**2 + (k + 1) ** 2) >= 0:
                ans = max(count, ans)

print(ans)
