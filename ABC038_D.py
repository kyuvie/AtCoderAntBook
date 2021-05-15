from bisect import bisect_left

n = int(input())
wh = []

for i in range(n):
    wh.append(list((int(j) for j in input().split())))

wh.sort(key=lambda x:x[1], reverse=True)
wh.sort(key=lambda x:x[0])

dp = [10**10 for i in range(n)]

for i in range(n):
    dp[bisect_left(dp, wh[i][1])] = wh[i][1]

print(bisect_left(dp, 10**10))
    
