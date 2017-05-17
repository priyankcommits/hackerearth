processes = int(raw_input())
calling = map(int, raw_input().split())
ideal = map(int, raw_input().split())

time = 0

for num in ideal:
    while num != calling[0]:
        calling = calling[1:] + [calling[0]]
        time += 1
    time += 1
    calling = calling[1:]
print time

# similar to best answer
