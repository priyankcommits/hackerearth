tests = int(raw_input())

for i in xrange(tests):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    if arr.count(min(arr)) % 2 == 0:
        print "Unlucky"
    else:
        print "Lucky"

# best answer is same
