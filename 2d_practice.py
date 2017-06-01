a, b = map(int, raw_input().split())
m = []
for _ in range(a):
    m.append(raw_input().split())
for i in range(b):
    c = ""
    for j in range(a):
        c += m[j][i]+" "
    print(c)
