def micro_array():
    tests = int(raw_input())
    for i in range(tests):
        inp = raw_input().split()
        n = int(inp[0])
        k = int(inp[1])
        arr = raw_input().split()[:n]
        for i in arr:
            arr[arr.index(i)] = int(i)
        minimum = min(arr)
        if k < minimum:
            print 0
        else:
            print k - minimum
micro_array()

# best answer

#  t=input()
#  for i in range(0,t):
#      n,k=map(int,raw_input().split())
#      a=[]
#      a=map(int,raw_input().split())
#      x=min(a)
#      if x<k:
#          print k-x
#      else:
#          print "0"
