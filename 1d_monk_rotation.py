tests = int(raw_input())

for i in xrange(tests):
    input = map(int, raw_input().split())
    arr = raw_input().split()
    if(input[1] > input[0]):
        input[1] = input[1] % input[0]
    print ' '.join(arr[-(input[1]):]),
    print ' '.join(arr[:-input[1]])

# best answer is same
