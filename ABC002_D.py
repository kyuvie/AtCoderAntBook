from itertools import combinations
n, m = [int(i) for i in input().split()]

xy = []

for i in range(m):
    xx, yy = [int(j) for j in input().split()]
    xy.append((xx, yy))

# 完全グラフでグラフの内、頂点の数が最大のものを求める
# 完全グラフを判定するアルゴリズム
# あらかじめ、ビットで完全グラフである頂点の組み合わせを決め打ちして、確かめていく

comb = 1 << n

ans = 1

for pattern in range(comb):
    c = []
    for i in range(n):
        if pattern >> i & 1:
            c.append(i+1)
    c = list(combinations(c, 2))
    for s, e in c:
        if not (s, e) in xy:
            break
    else:
        ans_tmp = set()
        for cc in c:
            for ccc in cc:
                ans_tmp.add(ccc)
        ans = max(ans, len(ans_tmp))

print(ans)

"""
# 別解
import itertools as it


def main():
    n, m = [int(i) for i in input().split()]
    table = [[False for j in range(n)] for i in range(n)]
    for i in range(m):
        x, y = [int(j) for j in input().split()]
        table[x-1][y-1] = True
    # bit全探索(頂点の組み合わせを出す)
    ans = 0
    for i in range(1<<n):
        tmp = []
        for j in range(n):
            if i >> j & 1:
                tmp.append(j)
        if len(tmp) < 2:
            continue
        edges = it.combinations(tmp, 2)
        if all(map(lambda x: table[x[0]][x[1]], edges)):
            ans = max(ans, len(tmp))
    print(ans if ans != 0 else 1)


if __name__ == '__main__':
    main()

"""
