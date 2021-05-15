"""
三角形の成立条件は
a + b > c かつ b + c > a かつ c + a > b
c - b < a かつ a < b + c かつ b - c < a
これより |b-c| < a < b+c が導かれる
"""
n = int(input())
l = [int(i) for i in input().split()]

ans = 0

for i in range(len(l)):
    for j in range(i+1, len(l)):
        for k in range(j+1, len(l)):
            if l[i] != l[j] and l[j] != l[k] and l[i] != l[k] and abs(l[i] - l[j]) < l[k] < l[i] + l[j]:
                ans += 1

print(ans)

