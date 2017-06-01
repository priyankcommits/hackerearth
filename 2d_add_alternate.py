odd_sum = 0
even_sum = 0
arr = map(int, raw_input().split())
for i in xrange(len(arr)):
    if i % 2 != 0:
        odd_sum += arr[i]
    else:
        even_sum += arr[i]
print even_sum
print odd_sum

# best asnwer is
#  a = raw_input().split()
#  a = map(int, a)
#
#  print sum(a[::2])
#  print sum(a[1::2])
