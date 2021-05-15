abcd = list(input())


# ns := new string
def rec(i, ns):
    ans = None
    if i == 3:
        if eval(ns + abcd[3]) == 7:
            return ns + abcd[3] +'=7'
        return None
    ans = rec(i+1, ns + abcd[i] + '-')
    ret1 = rec(i+1, ns + abcd[i] + '+')
    if ret1:
        ans = ret1
    return ans

print(rec(0, ''))
        
