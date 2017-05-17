tests = int(raw_input())
result = "Tie"
for i in range(0, tests):
    arr_size = int(raw_input())
    rupam = map(int, raw_input().split())
    ankit = map(int, raw_input().split())
    for j in range(0, arr_size-1):
        number = max(rupam)
        if rupam.count(number) > ankit.count(number):
            result = "Rupam"
            break
        elif rupam.count(number) < ankit.count(number):
            result = "Ankit"
            break
        else:
            rupam.pop(rupam.index(max(rupam)))
            continue
    print result

# best answer
#  t = int(input())
#  for _ in range(t):
#      n = int(input())
#      Rupam = map(int,raw_input().split())
#      Ankit = map(int,raw_input().split())
#      R = sorted(set(Rupam))[::-1]
#      m1, mitem1 = 0,0
#      A = sorted(set(Ankit))[::-1]
#      m2, mitem2 = 0,0
#      for item in R:
#          c = Rupam.count(item)
#          if c > m1:
#              m1 = c
#              mitem1 = item
#      for item in A:
#          c = Ankit.count(item)
#          if c > m2:
#              m2 = c
#              mitem2 = item
#
#      if mitem1 == mitem2: print 'Tie'
#      else: print 'Rupam' if mitem1>mitem2 else 'Ankit'
