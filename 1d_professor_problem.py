n = int(raw_input())

arr = raw_input().split()

q = int(raw_input())

for i in xrange(q):
    swaps = map(int, raw_input().split())
    temp = arr[swaps[0]-1]
    arr[swaps[0]-1] = arr[len(arr)-swaps[0]]
    arr[len(arr)-swaps[0]] = temp
    temp = arr[swaps[1]-1]
    arr[swaps[1]-1] = arr[len(arr)-swaps[1]]
    arr[len(arr)-swaps[1]] = temp
print " ".join(arr)

# best asnwer is
#  import sys
#  n=int(sys.stdin.readline())
#  l=[0]+list(map(int, sys.stdin.readline().split()))
#  b=[]
#  temp=0
#  for i in xrange(0,n+2):
#      b.append(0)
#  q=int(sys.stdin.readline())
#  for i in xrange(0,q):
#      l1,r=map(int, sys.stdin.readline().split())
#      b[l1]+=1
#      b[r+1]-=1
#  for i in xrange(2,n+1):
#      b[i]+=b[i-1]
#  for i in xrange(1,n+1):
#      if b[i]%2!=0:
#          temp=l[i]
#          l[i]=l[n-i+1]
#          l[n-i+1]=temp
#  for i in range(1,n+1):
#      p=str(l[i])
#      sys.stdout.write(p)
#      sys.stdout.write(" ")
