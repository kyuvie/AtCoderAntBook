n, y = [int(i) for i in input().split()]

# i := 10000 円札の数
# j := 5000 円札の数
# 1000 円札は N が決まっているので残ったものから算出(n-i-j)
switch = False
for i in range(n+1):
    for j in range(n-i+1):
        if 10**4 * i + 5 * 10**3 * j + 10**3 * (n - i - j) == y:
            switch = True
            print(i, j, n-i-j)
            break
    if switch:
        break
else:
    print(-1, -1, -1)

