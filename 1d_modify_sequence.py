n = int(raw_input())
arr = map(int, raw_input().split())

num = arr[0]
result = "YES"
for i in range(1, n):
    if arr[i] != num:
        result = "NO"
        break
print result

# dint understand the question, lol best asnwer is

#  n = int(raw_input())
#  a = list(map(int, raw_input().split()))
#
#  for i in xrange(n-1):
#          if a[i] > a[i+1]:
#                  a[i] = a[i] - a[i+1]
#                  a[i+1] = 0
#          else:
#                  a[i+1] = a[i+1] - a[i]
#                  a[i] = 0
#
#  print 'YES' if all([a[i]==0 for i in xrange(n)]) else 'NO'
