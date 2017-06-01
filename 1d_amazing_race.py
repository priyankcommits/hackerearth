RI = lambda: map(int, raw_input().split())

I = 1000010000
M = 1000000007

for _ in range(input()):
    n = input()
    h = [I] + RI() + [I]
    l = [0] * (n + 2)
    r = [n + 1] * (n + 2)
    for i in range(1, n + 1):
        l[i] = i - 1
        while h[i] > h[l[i]]:
            l[i] = l[l[i]]
    for i in range(n, 0, -1):
        r[i] = i + 1
        while h[i] > h[r[i]]:
            r[i] = r[r[i]]
    # print h
    # print l
    # print r
    u, v = 1, 0
    for i in range(1, n + 1):
        x = (min(n, r[i]) - max(l[i], 1)) * i % M
        # print i, x
        if x > v:
            u, v = i, x
    print u
