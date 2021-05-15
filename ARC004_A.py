import math
n = int(input())
x = []
y = []

for i in range(n):
    xx, yy = [int(i) for i in input().split()]
    x.append(xx); y.append(yy)

ans = -1
for i in range(n):
    for j in range(n):
        ans = max(ans, math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))

print(ans)
