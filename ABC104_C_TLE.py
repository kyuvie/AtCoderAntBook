d, g = [int(i) for i in input().split()]
p = []; c = []

for i in range(d):
    pp, cc = [int(j) for j in input().split()]
    p.append(pp); c.append(cc)

p = list(reversed(p))
c = list(reversed(c))


def rec(i, point, ans):
    if i == d:
        if point >= g:
            return ans
        return 10**10
    ret = 10**10
    if point >= g:
        return rec(i+1, point, ans)
    ret = min(ret, rec(i+1, point, ans))
    for j in range(1, p[i]):
        # ポイントに、問題の解いた数を足す
        ret = min(ret, rec(i+1, point + (d-i) * j * 100, ans + j))
    ret = min(ret, rec(i+1, point + p[i] * (d-i) * 100 + c[i], ans + p[i]))
    return ret

print(rec(0, 0, 0))
