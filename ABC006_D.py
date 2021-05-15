from bisect import bisect_left

# 最小の手数は、部分増加列に入っていないカードの枚数である

n = int(input())
c = []

ans = 0

for i in range(n):
    c.append(int(input()))

dp = [10**10 for i in range(10**5)]

for i in range(n):
    dp[bisect_left(dp, c[i])] = c[i]

print(n-bisect_left(dp, 10**10))

