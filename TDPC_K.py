from bisect import bisect_left
n = int(input())

"""
LIS は Longest Increasing Subseqnece の 略。通称、最長増加部分列。
"""

xr = []

for i in range(n):
    x, r = [int(j) for j in input().split()]
    xr.append((x-r, x+r))

xr.sort(key=lambda x: x[0], reverse=True)
xr.sort(key=lambda x: x[1], reverse=True)

dp = [10**15 for i in range(n)]

for i in range(len(xr)):
    dp[bisect_left(dp, xr[i][0])] = xr[i][0]

print(bisect_left(dp, 10**15))

