size = input()
a = raw_input().split()
b = raw_input().split()
c = []
for i in range(0, len(a)):
    c.append(str(int(a[i]) + int(b[i])))
print " ".join(c)

# best answer

#  n=input()
#  a=map(int,raw_input().split())
#  b=map(int,raw_input().split())
#  for i in range(n):
#      print a[i]+b[i],
