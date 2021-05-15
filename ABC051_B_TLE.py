k, s = [int(i) for i in input().split()]

ans = 0

for i in range(0, k+1):
    for j in range(0, k+1):
        for kk in range(0, k+1):
            if i + j + kk == s:
                ans += 1

print(ans)
