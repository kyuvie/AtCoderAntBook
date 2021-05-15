from bisect import bisect_left

n = int(input())
c = []

ans = 0
for i in range(n):
    cc = int(input())
    if len(c) != 0:
        if c[-1] > cc:
            c.insert(bisect_left(c, cc), cc)
            ans += 1
        else:
            c.append(cc)
    else:
        c.append(cc)


print(ans)

