n = int(input())
bs = list(map(int,input().split()))

a = 1
for b in bs:
    a = ( a * 2 ) - b
    if a < 0:
        print('error')
        break
else:
    print(a % 1000000007)