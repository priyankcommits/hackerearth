tests = int(raw_input())

for i in range(tests):
    cars = int(raw_input())
    speeds = map(int, raw_input().split())
    counter = 1
    speed = speeds[0]
    for j in range(1, cars):
        if speeds[j] <= speed:
            counter += 1
            speed = speeds[j]
    print counter

# answer is best answer
