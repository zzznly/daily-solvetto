# 1차원 젠가
# https://www.codetree.ai/missions/2/problems/jenga-1d?&utm_source=clipboard&utm_medium=text
import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
s1, e1 = map(int, sys.stdin.readline().split())
s2, e2 = map(int, sys.stdin.readline().split())

temp = []
for i in range(len(arr)):
    if i < s1 - 1 or i > e1 - 1:
        temp.append(arr[i])
arr = []
for ele in temp:
    arr.append(ele)
temp = []
for i in range(len(arr)):
    if i < s2 - 1 or i > e2 - 1:
        temp.append(arr[i])

print(len(temp))
if temp:
    for ele in temp:
        print(ele)
