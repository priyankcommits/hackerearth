for _ in range(input()):
    n = input()
    a = [0] * (n * 2 + 10)
    s = raw_input()
    k = s.count('K')
    for i in range(n):
        a[i + 1] = a[i] + (s[i] == 'K')
    for i in range(n):
        a[n + i + 1] = a[n + i] + (s[i] == 'K')
    ans = 0
    for i in range(k, n * 2 + 1):
        ans = max(ans, a[i] - a[i - k])
    print k - ans

# best is answer is same(copied), could not get a logic for this
