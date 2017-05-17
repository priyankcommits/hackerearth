entries = int(raw_input())
arr = [0 for i in range(1000000)]
max = 0
maxelement = 0
numberSet = raw_input()
numberSet = numberSet.split(' ')
numberSet = map(int, numberSet)
for i in range(entries):
    arr[numberSet[i]] = arr[numberSet[i]]+1
    if max < arr[numberSet[i]]:
        maxelement = numberSet[i]
        max = arr[numberSet[i]]

    elif max == arr[numberSet[i]]:
        if maxelement > numberSet[i]:
            maxelement = numberSet[i]
        max = arr[numberSet[i]]
print maxelement

# best asnwer same answer
