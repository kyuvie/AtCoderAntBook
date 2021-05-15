s = list(input())
n = len(s)

# ns := new string
def rec(i, ns):
    ans = 0
    if i == n-1:
        # print(ns+s[i])
        return eval(ns + s[i])
    ans += rec(i+1, ns + s[i] + '+')
    ans += rec(i+1, ns + s[i])
    return ans

print(rec(0, ''))

