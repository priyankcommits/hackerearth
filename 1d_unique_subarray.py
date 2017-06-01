tests = int(raw_input())
for i in xrange(tests):
    n = int(raw_input())
    a = map(int, raw_input().split())
    counter = 0
    init = 0
    score = 0
    for j in xrange(len(a)):
        if a[j] != a[j-1]:
            counter += 1
        else:
            init = j
            break
        count = 1
        for k in xrange(1, len(a[init:counter])+1):
            score += k * count
    print score

# best answer is
#  for cas in xrange(input()):
#      n = input()
#      arr = map(int, raw_input().strip().split())
#      s = set()
#      i = 0;j=0; ans = 0
#      while i< n:
#          while j < n and arr[j] not in s:
#              s.add(arr[j])
#              j += 1
#          t = j - i
#          ans = ans + (t*(t+1))/2
#          s.remove(arr[i])
#          i += 1
#      print ans
