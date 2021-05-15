n = int(input())
t = []
for i in range(n):
    t.append(int(input()))


def rec(i, a, b):
    if i == n:
        return max(a, b)
    ans = rec(i+1, a+t[i], b)
    ans = min(ans, rec(i+1, a, b+t[i]))
    return ans

print(rec(0, 0, 0))
    
