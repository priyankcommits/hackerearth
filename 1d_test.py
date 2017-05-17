n = raw_input()
a = []
for i in range(0, int(n)):
    n = raw_input()
    a.append(int(n))
for i in a[::-1]:
    print(i)
